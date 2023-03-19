from django.db import models

# Create your models here.
class all_base_data(models.Model):
    user_id = models.CharField("用户账号", max_length=30,default='')
    name = models.CharField("名字", max_length=11, default='')
    date = models.CharField("日期", max_length=20, default='')
    time = models.IntegerField("时间", default='')
    term = models.IntegerField("期数", default='')
    is_delete = models.BooleanField("是否已删除", default=True)
    class Meta:
        db_table = 'base_data'
        verbose_name = '基础信息'
        verbose_name_plural = verbose_name

class change_data(models.Model):
    user_id = models.CharField("用户账号", max_length=30, default='')
    name = models.CharField("名字", max_length=11, default='')
    old_date = models.CharField("原研学日期", max_length=20, default='')
    old_time = models.IntegerField("原研学时间", default='')
    new_date = models.CharField("新研学日期", max_length=20, default='')
    new_time = models.IntegerField("新研学时间", default='')
    reason = models.CharField("原因", max_length=50, default='')
    is_delete = models.BooleanField("是否已删除", default=True)

    class Meta:
        db_table = 'change_data'
        verbose_name = '调换信息'
        verbose_name_plural = verbose_name

class leave_data(models.Model):
    user_id = models.CharField("用户账号", max_length=30, default='')
    name = models.CharField("名字", max_length=11, default='')
    old_date = models.CharField("原研学日期", max_length=20, default='')
    old_time = models.IntegerField("原研学时间", default='')
    reason = models.CharField("原因", max_length=50, default='')
    is_delete = models.BooleanField("是否已删除", default=True)

    class Meta:
        db_table = 'leave_data'
        verbose_name = '请假信息'
        verbose_name_plural = verbose_name

class test2(models.Model):
    date = models.DateTimeField("时间")
