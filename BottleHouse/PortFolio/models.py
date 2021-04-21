from django.db import models
from django.conf import settings

class PortFolio(models.Model):
    title = models.CharField(max_length=200)    # 이름
    term = models.CharField(max_length=200)   # 기간
    summary = models.TextField()    # 프로젝트 개요
    contents = models.TextField()   # 설계 주안점
    development_environment = models.CharField(max_length=200)   # 개발환경
    development_language = models.CharField(max_length=200) # 개발언어
    library = models.CharField(max_length=500) # 라이브러리
    tool = models.CharField(max_length=500)   # 개발도구
    equipment = models.CharField(max_length=500)   # 개발장비
    role = models.TextField()    # 주요역할 및 담당
    awards = models.TextField() # 받은 상
    image = models.ImageField() # 이미지
    git = models.CharField(max_length=200)  # git 주소
    date = models.DateTimeField()   # 종결날짜
    
    # model에 의해 새로운 객체가 생성될 때 이름을 title로 지정한다.
    def __str__(self):
        return self.title