from django.db import models
from django.conf import settings

class PortFolio(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    image = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add = True) # 레코드 생성시 현재 시간으로 자동 생성

    # model에 의해 새로운 객체가 생성될 때 이름을 title로 지정한다.
    def __str__(self):
        return self.title