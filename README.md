# ![ai](https://github.com/user-attachments/assets/0183c7fc-c7a7-479b-8108-4c68de3dffa7) 생성형 AI Streaming Server<br><br>

## 📋 프로젝트 설명

### 다양한 생성형 AI 모델의 스트리밍 서비스를 제공하는 서버
- Mistral Large
- Llama3.3
- HCX-003
- Gemini 1.5 Pro
- GPT 3.5 Turbo
  <br><br>

## 📅 프로젝트 기간
<b>2025. 01. 26 ~ 2025. 01. 28</b>
<br><br>

## ![Image](https://github.com/user-attachments/assets/1838d6b9-69ff-43fe-80b1-b1e39709cef9) 모델 추가 및 리팩터링
<b>2025. 01. 30</b>
<br><br>

## 👫 구성원

### 성효빈
- 서버 개발, 배포 및 관리
  <br>

## 📚 관련 URL
- [서버 API](https://hyobin-llm.duckdns.org/docs)
  <br><br>

## 🛠️ Skills

## Back-End
- Python
- LangChain
- FastAPI
- Starlette
  <br>

## AI Model Packages
- ChatMistralAI
- SambaNovaCloud
- ChatClovaX
- ChatGoogleGenerativeAI
- ChatOpenAI

## DevOps

### Interpretation
- Pipenv

### WAS
- Uvicorn

### Server
- NCP Server
  <br>

## Tools

### IDE
- PyCharm

### Issue Tracking
- Jira

<br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/27

### 하위 작업

[LCSV-3](https://langchain.atlassian.net/browse/LCSV-3) Pipfile 생성

[LCSV-4](https://langchain.atlassian.net/browse/LCSV-4) LangChain 설치

[LCSV-5](https://langchain.atlassian.net/browse/LCSV-5) LangChain OpenAI 패키지 설치

[LCSV-6](https://langchain.atlassian.net/browse/LCSV-6) LangChain Llama3.2 패키지 설치

[LCSV-7](https://langchain.atlassian.net/browse/LCSV-7) LangChain HCX-003 패키지 설치

[LCSV-8](https://langchain.atlassian.net/browse/LCSV-8) LangChain Community 패키지 설치

[LCSV-9](https://langchain.atlassian.net/browse/LCSV-9) Formatter 패키지 설치

[LCSV-10](https://langchain.atlassian.net/browse/LCSV-10) Dotenv 패키지 설치

[LCSV-11](https://langchain.atlassian.net/browse/LCSV-11) .env 파일 추가

[LCSV-12](https://langchain.atlassian.net/browse/LCSV-12) uvicorn 패키지 설치

[LCSV-13](https://langchain.atlassian.net/browse/LCSV-13) fastapi 패키지 설치

[LCSV-14](https://langchain.atlassian.net/browse/LCSV-14) app.py 추가

[LCSV-16](https://langchain.atlassian.net/browse/LCSV-16) LLM 타입과 템플릿, 변수 목록, 시크릿 키를 통한 클라이언트 요청

[LCSV-17](https://langchain.atlassian.net/browse/LCSV-17) 클라이언트 시크릿 키 인증

[LCSV-18](https://langchain.atlassian.net/browse/LCSV-18) LLM 서비스 요청 비즈니스 로직

[LCSV-19](https://langchain.atlassian.net/browse/LCSV-19) 200 status code 응답

[LCSV-21](https://langchain.atlassian.net/browse/LCSV-21) 서버 API 설명

[LCSV-22](https://langchain.atlassian.net/browse/LCSV-22) 엔드포인트 설명

[LCSV-23](https://langchain.atlassian.net/browse/LCSV-23) 파라미터 샘플값 적용

[LCSV-25](https://langchain.atlassian.net/browse/LCSV-25) 네이버 클라우드에 서버 인스턴스 생성

[LCSV-26](https://langchain.atlassian.net/browse/LCSV-26) 서버 인스턴스에 애플리케이션 클론

[LCSV-27](https://langchain.atlassian.net/browse/LCSV-27) .env의 key 업데이트

[LCSV-28](https://langchain.atlassian.net/browse/LCSV-28) pyenv 설치

[LCSV-29](https://langchain.atlassian.net/browse/LCSV-29) pyenv 환경변수 설정

[LCSV-30](https://langchain.atlassian.net/browse/LCSV-30) python 3.9.6 설치

[LCSV-31](https://langchain.atlassian.net/browse/LCSV-31) pip 설치

[LCSV-32](https://langchain.atlassian.net/browse/LCSV-32) pipenv 설치

[LCSV-33](https://langchain.atlassian.net/browse/LCSV-33) pipenv 의존성 업데이트

[LCSV-34](https://langchain.atlassian.net/browse/LCSV-34) 배포 서버에 Llama3.2 설치

[LCSV-35](https://langchain.atlassian.net/browse/LCSV-35) Fast API 서버 실행

[LCSV-37](https://langchain.atlassian.net/browse/LCSV-37) SSL/TLS 인증서 발급

[LCSV-38](https://langchain.atlassian.net/browse/LCSV-38) FastAPI 애플리케이션 실행 시 인증서 적용

### 스토리

[LCSV-15](https://langchain.atlassian.net/browse/LCSV-15) 클라이언트는 LLM 타입과 템플릿, 변수 목록, 시크릿 키를 전송해 LLM 서버를 이용할 수 있다

[LCSV-20](https://langchain.atlassian.net/browse/LCSV-20) 클라이언트는 Swagger 문서를 통해 LLM 서버 이용 가이드를 확인할 수 있다

[LCSV-24](https://langchain.atlassian.net/browse/LCSV-24) 클라이언트는 공용 엔드포인트를 통해 LLM 서버를 이용할 수 있다

[LCSV-36](https://langchain.atlassian.net/browse/LCSV-36) 클라이언트는 LLM 서버를 신뢰하고 요청을 암호화해 전송할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-2](https://langchain.atlassian.net/browse/LCSV-2) 초기 환경 설정

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/27-2

### 하위 작업

[LCSV-41](https://langchain.atlassian.net/browse/LCSV-41) LLM 서비스 응답을 토큰화하여 수신

[LCSV-42](https://langchain.atlassian.net/browse/LCSV-42) LLM 서비스 요청과 클라이언트 응답을 Streaming 방식으로 변경

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가

[LCSV-40](https://langchain.atlassian.net/browse/LCSV-40) 클라이언트는 스트리밍을 통한 빠른 응답을 제공 받을 수 있다
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/28

### 하위 작업

[LCSV-44](https://langchain.atlassian.net/browse/LCSV-44) SSE를 통해 서버로부터 토큰을 지속적으로 Push 받을 수 있는 엔드포인트\(/streaming/sse\) 추가

[LCSV-45](https://langchain.atlassian.net/browse/LCSV-45) 기존 엔드포인트의 리소스명을 streaming으로 변경

[LCSV-46](https://langchain.atlassian.net/browse/LCSV-46) 기존 엔드포인트와 추가된 엔드포인트의 공통 예외를 처리하기 위한 global\_exception\_handler 추가

[LCSV-48](https://langchain.atlassian.net/browse/LCSV-48) CORS 활성화

### 스토리

[LCSV-43](https://langchain.atlassian.net/browse/LCSV-43) 클라이언트는 엔드포인트로부터 최소 토큰 단위의 Stream 데이터를 지속적으로 Push 받을 수 있다

[LCSV-47](https://langchain.atlassian.net/browse/LCSV-47) 클라이언트는 브라우저를 통해 LLM 서버 엔드포인트를 이용할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가
<br><br>

## 릴리스 정보 - LangChain Service - LlmApiServerRelease01/30

### 하위 작업

[LCSV-50](https://langchain.atlassian.net/browse/LCSV-50) API 키 발급

[LCSV-51](https://langchain.atlassian.net/browse/LCSV-51) ChatGoogle 패키지 설치

[LCSV-52](https://langchain.atlassian.net/browse/LCSV-52) gemini-1.5-pro 모델 적용

[LCSV-54](https://langchain.atlassian.net/browse/LCSV-54) API 키 발급

[LCSV-55](https://langchain.atlassian.net/browse/LCSV-55) SambaNovaCloud 패키지 설치

[LCSV-56](https://langchain.atlassian.net/browse/LCSV-56) Llama-3.3-70B-Instruct 모델 적용

[LCSV-57](https://langchain.atlassian.net/browse/LCSV-57) ChatOllama 패키지 제거

[LCSV-58](https://langchain.atlassian.net/browse/LCSV-58) ChatOllama 기반 Llama3.2 서비스 제거

[LCSV-59](https://langchain.atlassian.net/browse/LCSV-59) 기본 모델을 HCX-003에서 Llama3.3으로 변경

[LCSV-61](https://langchain.atlassian.net/browse/LCSV-61) LLM 서비스 인스턴스 생성 모듈 분리 -> llm\_generator

[LCSV-62](https://langchain.atlassian.net/browse/LCSV-62) 기본 모델 설정 함수 분리

[LCSV-63](https://langchain.atlassian.net/browse/LCSV-63) .env 파일의 환경변수 순서 정리

[LCSV-65](https://langchain.atlassian.net/browse/LCSV-65) API 키 발급

[LCSV-66](https://langchain.atlassian.net/browse/LCSV-66) ChatMistralAI 패키지 설치

[LCSV-67](https://langchain.atlassian.net/browse/LCSV-67) mistral-large-latest 모델 적용

[LCSV-68](https://langchain.atlassian.net/browse/LCSV-68) mistral-large-latest를 기본 모델로 사용하도록 변경

[LCSV-69](https://langchain.atlassian.net/browse/LCSV-69) Swagger 문서 업데이트

[LCSV-71](https://langchain.atlassian.net/browse/LCSV-71) variables 키를 options로 변경

[LCSV-72](https://langchain.atlassian.net/browse/LCSV-72) 0 ~ n 개의 여러 옵션들을 각각 키와 배열값 형태로 제공할 수 있도록 변경

[LCSV-73](https://langchain.atlassian.net/browse/LCSV-73) LLM 모델과 옵션을 전송하지 않아도 작동하도록 변경

[LCSV-74](https://langchain.atlassian.net/browse/LCSV-74) Swagger 문서 업데이트

### 스토리

[LCSV-49](https://langchain.atlassian.net/browse/LCSV-49) 클라이언트는 gemini-1.5-pro 모델 API를 사용할 수 있다

[LCSV-53](https://langchain.atlassian.net/browse/LCSV-53) 클라이언트는 ChatOllama 대신 SambaNovaCloud를 통해 Llama3.3 모델 API를 사용할 수 있다

[LCSV-64](https://langchain.atlassian.net/browse/LCSV-64) 클라이언트는 mistral-large 모델 API를 사용할 수 있다

[LCSV-70](https://langchain.atlassian.net/browse/LCSV-70) 사용자는 LLM 서비스 요청 시 여러 옵션들을 Key: Array Value 형태로 전송할 수 있다

### 에픽

[LCSV-1](https://langchain.atlassian.net/browse/LCSV-1) LLM API Server 구현

### 작업

[LCSV-39](https://langchain.atlassian.net/browse/LCSV-39) README.md 추가

[LCSV-60](https://langchain.atlassian.net/browse/LCSV-60) llm\_picker 모듈 리팩터링
