# webdriver를 사용하기 위한 selinum 모듈
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 페이지 로딩을 기다리는데 사용할 time 모듈
import time
import os

# 1. 웨일 실행파일 경로 (본인 PC 경로로 수정!)
WHALE_PATH = "C:/Program Files/Naver/Naver Whale/Application/whale.exe"

# 2. ChromeDriver 경로
CHROMEDRIVER_PATH = "./Driver/chromedriver.exe"

# 3. 웨일 실행을 위한 옵션 설정
options = Options()
options.binary_location = WHALE_PATH

# 🔽 사용자 데이터 디렉토리 임시폴더로 지정
user_data_dir = os.path.abspath("whale_user_data")
options.add_argument(f"--user-data-dir={user_data_dir}")

# 🔽 중복 실행 방지 옵션 (선택)
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")

# 4. 드라이버 실행
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# 5. ChatGPT 웹사이트 열기
driver.get("https://chat.openai.com/")

# 6. 로그인 수동 진행 (자동화 가능하지만 복잡하므로 생략)
input("🔐 로그인 완료 후 Enter를 누르세요...")

# 7. 질문 입력 및 전송
question = "웨일로도 Selenium 자동화가 잘 되나요?"
textarea = driver.find_element(By.TAG_NAME, "textarea")
textarea.send_keys(question)
textarea.send_keys(Keys.ENTER)

# 8. 응답 대기
print("⏳ ChatGPT 응답 기다리는 중...")
time.sleep(10)  # 상황에 따라 더 늘릴 수도 있음

# 9. 응답 추출
responses = driver.find_elements(By.CLASS_NAME, "markdown")
if responses:
    print("✅ ChatGPT 응답:", responses[-1].text)
else:
    print("❌ 응답을 찾을 수 없습니다.")
