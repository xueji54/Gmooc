from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nick_name=models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday=models.DateField(verbose_name="生日",null=True,blank=True)
    gender=models.CharField(choices=(("male","男"),("female","女")),default="female",max_length=5)
    address=models.CharField(max_length=100,default="")
    mobile=models.CharField(max_length=20,default="",null=True,blank=True)
    head_image=models.ImageField(upload_to="image/head/%Y/%m",default="image/default.png",max_length=100)

    class Meta:
        verbose_name="用户信息"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.username