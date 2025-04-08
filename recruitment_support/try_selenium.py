from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

CHROMEDRIVER_PATH = "C:/Users/d9801/Downloads/chromedriver-win64/chromedriver.exe"

url = "https://www.saramin.co.kr/zf_user/jobs/relay/view?rec_idx=49942466"

options = Options()
# options.add_argument("--headless")  # 🔥 끄는 걸 추천
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# 봇 탐지 우회
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

driver.get(url)
time.sleep(5)  # 충분히 기다리기

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

title = soup.select_one("h1")
company = soup.select_one(".company_name a")
content = soup.select_one(".user_content")

data = {
    "공고제목": title.get_text(strip=True) if title else "없음",
    "회사명": company.get_text(strip=True) if company else "없음",
    "상세내용": content.get_text(separator="\n", strip=True) if content else "없음"
}

df = pd.DataFrame([data])
df.to_csv("saramin_detail.csv", index=False, encoding="utf-8-sig")
print("✅ 상세 공고 내용 저장 완료!")
