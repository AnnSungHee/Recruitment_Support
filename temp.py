import requests
from bs4 import BeautifulSoup

url = "https://www.saramin.co.kr/zf_user/search?loc_mcd=101000%2C102000%2C108000&cat_kewd=84%2C87%2C89%2C101&exp_cd=1%2C2&exp_max=1&edu_min=6&edu_max=11&edu_none=y&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y&recruitPage=1&recruitSort=closing_dt&recruitPageCount=40&inner_com_type=&searchword=&show_applied=&quick_apply=&except_read=&ai_head_hunting=&mainSearch=n"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")  # lxml 파서 사용

jobs = soup.select(".item_recruit")

for job in jobs:
    title_tag = job.select_one(".job_tit a")
    company_tag = job.select_one(".corp_name a")
    if title_tag and company_tag:
        print(f"[{company_tag.text.strip()}] {title_tag.text.strip()}")
