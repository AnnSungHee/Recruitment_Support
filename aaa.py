import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# User-Agent 설정
headers = {
    "User-Agent": "Mozilla/5.0"
}

# 결과 저장용 리스트
all_jobs = []

# 몇 페이지까지 수집할지 설정
max_page = 5  # 원하는 만큼 변경 가능

for page in range(1, max_page + 1):
    url = f"https://www.saramin.co.kr/zf_user/jobs/list/job-category?page={page}"
    print(f"▶ {page}페이지 요청 중...")

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    jobs = soup.select(".item_recruit")
    if not jobs:
        print("❌ 공고를 찾을 수 없습니다.")
        break

    for job in jobs:
        title_tag = job.select_one(".job_tit a")
        company_tag = job.select_one(".corp_name a")

        if title_tag and company_tag:
            title = title_tag.text.strip()
            company = company_tag.text.strip()
            link = "https://www.saramin.co.kr" + title_tag['href']
            print(f"[{company}] {title} → {link}")
            all_jobs.append([company, title, link])

    # 1~3초 랜덤 대기
    wait_time = random.uniform(1, 3)
    print(f"⏳ {wait_time:.1f}초 대기...\n")
    time.sleep(wait_time)

# CSV로 저장
with open("saramin_jobs.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["회사명", "공고명", "링크"])
    writer.writerows(all_jobs)

print(f"\n✅ 총 {len(all_jobs)}개의 공고를 수집하고 CSV로 저장했습니다.")
