import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

url = 'https://www.saramin.co.kr/zf_user/search'
params = {
    'loc_mcd': '101000,102000,108000',
    'cat_kewd': '84,87,89,101',
    'exp_cd': '1,2',
    'exp_max': '1',
    'edu_none': 'y',
    'edu_min': '6',
    'edu_max': '11',
    'search_optional_item': 'y',
    'panel_count': 'y',
    'recruitSort': 'closing_dt',
    'recruitPageCount': 10,
    'recruitPage': 1
}

headers = {'User-Agent': 'Mozilla/5.0'}

res = requests.get(url, headers=headers, params=params)
soup = BeautifulSoup(res.text, 'html.parser')
job_posts = soup.select('.item_recruit')

data = []

for post in job_posts:
    title_tag = post.select_one('.job_tit a')
    company_tag = post.select_one('.corp_name a')
    condition_tags = post.select('.job_condition span')
    deadline_tag = post.select_one('.job_date')

    title = title_tag.text.strip() if title_tag else ''
    company = company_tag.text.strip() if company_tag else ''
    link = 'https://www.saramin.co.kr' + title_tag['href'] if title_tag else ''
    location = condition_tags[0].text.strip() if len(condition_tags) > 0 else ''
    education = condition_tags[1].text.strip() if len(condition_tags) > 1 else ''
    experience = condition_tags[2].text.strip() if len(condition_tags) > 2 else ''
    deadline = deadline_tag.text.strip() if deadline_tag else ''

    # 상세페이지 요청
    detail_res = requests.get(link, headers=headers)
    detail_soup = BeautifulSoup(detail_res.text, 'html.parser')

    # 상세 공고 내용 (간단한 설명만 추출)
    detail_content = detail_soup.select_one('.user_content')
    detail_text = detail_content.get_text(separator='\n').strip() if detail_content else '내용 없음'

    data.append({
        '회사명': company,
        '공고제목': title,
        '링크': link,
        '근무지': location,
        '학력': education,
        '경력': experience,
        '마감일': deadline,
        '상세내용': detail_text  
    })

    time.sleep(random.uniform(1.5, 2.5))  # 서버 차단 방지

# 저장
df = pd.DataFrame(data)
df.to_csv('saramin_상세공고포함.csv', index=False, encoding='utf-8-sig')

print("✅ 상세 채용공고 포함 CSV 저장 완료: saramin_상세공고포함.csv")
