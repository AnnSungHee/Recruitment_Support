# 채용지원 프로그램 만들기
### 


### Conda 환경 생성
```
conda create -n Recruitment_Support python=3.10
```

### Conda 환경 활성화
```
conda activate Recruitment_Support
```

# 인터프리터 선택
- VScode에서 중앙 상단에 input 박스 누르고 "> Interpreter 히기

### 의존성 추출
```
pip freeze > requirements.txt
```

### 의존성 설치
```
pip install -r requirements.txt 