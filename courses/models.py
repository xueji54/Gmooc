from datetime import datetime

from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name="课程名")
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=5)
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    students_num = models.IntegerField(default=0, verbose_name="学习人数")
    fav_num = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="封面图", max_length=100)
    cilck_num = models.IntegerField(default=0, verbose_name="点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name