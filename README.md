# Docker compose 컨테이너 환경 구축

### 0. 개요
- Django + nginx + gunicorn + postgresql
    
### 1. 실습 환경
- Python 3.8
- Postgresql9.6
- vscode
- Code formatter: black

### 2. 실습 목표
- Backend 스킬 향상을 위한 Toy Project

### 3. 실습 내용
- User 생성 기능 구현 (JWT 인증방식 사용)
- 블로그 CRUD REST API 구현
- Celery 비동기 태스크 큐를 활용한 이메일 발송서비스 구현
  : main branch에 push 이벤트 발생 시 email 발송 

- Dockerfile + Docker-compose.yml + django-entrypoint.sh 배포
    - Git
        - https://github.com/zusdn90/docker-django.git