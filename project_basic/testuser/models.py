from django.db import models

# Create your models here.
class testuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'test_user'
        verbose_name = '사용자'
        
        # 관리자페이지에서 모델명은 복수형을 쓰게되는데 그것을 변경하게하는것
        verbose_name_plural = '사용자'