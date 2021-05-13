from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)     # 최대길이가 30인 char를 담는 필드
    content = models.TextField()                # 문자열 길이 제한이 없음
    
    created_at = models.DateTimeField(auto_now=True)         # 월, 일, 시, 분, 초를 기록해주는 필드
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'[{self.pk}]{self.title}'       # pk는 각 레코드에 대한 고유값