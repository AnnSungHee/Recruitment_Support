import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 크롤링 대상 URL
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
    'recruitPageCount': 40,
    'recruitPage': 1
}

headers = {
    'User-Agent': 'Mozilla/5.0'
}

# 2. 요청 및 파싱
res = requests.get(url, headers=headers, params=params)
soup = BeautifulSoup(res.text, 'html.parser')

job_posts = soup.select('.item_recruit')

data = []
for post in job_posts:
    title_tag = post.select_one('.job_tit a')
    company_tag = post.select_one('.corp_name a')
    condition_tags = post.select('.job_condition span')
    deadline_tag = post.select_one('.job_date')

    data.append({
        '회사명': company_tag.text.strip() if company_tag else '',
        '공고제목': title_tag.text.strip() if title_tag else '',
        '링크': 'https://www.saramin.co.kr' + title_tag['href'] if title_tag else '',
        '근무지': condition_tags[0].text.strip() if len(condition_tags) > 0 else '',
        '학력': condition_tags[1].text.strip() if len(condition_tags) > 1 else '',
        '경력': condition_tags[2].text.strip() if len(condition_tags) > 2 else '',
        '마감일': deadline_tag.text.strip() if deadline_tag else ''
    })

# 3. pandas로 저장
df = pd.DataFrame(data)

# 4. CSV 저장 (로컬 저장 경로 수정 가능)
df.to_csv('saramin_jobs_page1.csv', index=False, encoding='utf-8-sig')

print("✅ CSV 저장 완료: saramin_jobs_page1.csv")
