from django.db import models
from django.conf import settings

class PortFolio(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    awards = models.TextField()
    image = models.ImageField()
    git = models.CharField(max_length=200)
    date = models.DateTimeField()
    

    # model에 의해 새로운 객체가 생성될 때 이름을 title로 지정한다.
    def __str__(self):
        return self.title