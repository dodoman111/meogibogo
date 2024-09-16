# meogibogo
먹이보고 푸드 커뮤니티
# MyProject (먹이보고)

## 프로젝트 설명
먹이보고는 사용자가 음식 리뷰를 커뮤니티에 공유할 수 있는 Django 기반의 웹 애플리케이션입니다.

## 환경 설정

이 프로젝트는 `pyenv`와 `Poetry`를 사용하여 Python 환경을 관리합니다.

### 1. 요구사항
- `pyenv` (Python 버전 관리)
- `Poetry` (패키지 관리 및 의존성 관리)
- Python 3.11.x

### 2. pyenv 설치 및 Python 버전 설정

```bash
# pyenv 설치
curl https://pyenv.run | bash
# 설치 후 아래 명령어로 환경 변수 설정
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc

# 프로젝트에 사용할 Python 버전 설치 및 설정
pyenv install 3.11.4
pyenv local 3.11.4

