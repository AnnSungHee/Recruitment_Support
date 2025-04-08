import requests

url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?view_type=search&rec_idx=50187111&location=ts&searchType=search&paid_fl=n&search_uuid=45073240-4bf9-4882-b41f-4f2763c8b075"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

# 파일로 저장
with open("saramin_job_detail_49942466.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print("✅ 상세 공고 HTML 저장 완료!")
