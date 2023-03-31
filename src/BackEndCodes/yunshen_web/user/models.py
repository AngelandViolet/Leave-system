from django.db import models

# Create your models here.
# 存储所有随机生成的邀请码
class invitationCode(models.Model):
    invitation_codes = models.CharField('邀请码', max_length=20, default='')

    class Meta:
        db_table = 'invitation_codes'
        verbose_name = '邀请码列表'
        verbose_name_plural = verbose_name
# 存储用户的注册和登录信息
class SignLog(models.Model):
    user_id = models.CharField("用户账号", max_length=20, default='')
    user_pass = models.CharField("用户密码", max_length=100, default='')
    user_name = models.CharField("用户姓名", max_length=10, default='')
    user_sector = models.CharField("用户部门方向", max_length=10, default='')
    user_period = models.IntegerField("用户期数", max_length=7)

    class Meta:
        db_table = 'user_sign_log_information'
        verbose_name = '用户注册和登录信息'
        verbose_name_plural = verbose_name

# 存储所有的基本研学信息
class theStudy(models.Model):
    user_id = models.CharField("用户账号", max_length=20, default='')
    study_date = models.CharField("用户研学日期", max_length=20, default='')
    study_class = models.IntegerField("用户研学大节")
    is_change = models.BooleanField("是否已调换", default=0)
    is_leave = models.BooleanField("是否已请假", default=0)

    class Meta:
        db_table = 'base_study_data'
        verbose_name = '用户的基础研学信息'
        verbose_name_plural = verbose_name

# 存储所有的调换研学信息
class changeData(models.Model):
    user_id = models.CharField("用户账号", max_length=20, default='')
    old_time = models.CharField("原研学日期", max_length=20, default='')
    old_class = models.IntegerField("原研学大节")
    new_time = models.CharField("调换后研学日期", max_length=20, default='')
    new_class = models.IntegerField("调换后研学大节")
    change_reason = models.CharField("调换原因", max_length=50, default='')
    is_delete = models.BooleanField("是否已被删除", default=0)

    class Meta:
        db_table= 'users_change_data'
        verbose_name = '用户的调换研学信息'
        verbose_name_plural = verbose_name

# 存储所有的研学请假信息
class leaveData(models.Model):
    user_id = models.CharField("用户账号", max_length=20, default='')
    leave_time = models.CharField("请假的研学日期", max_length=20, default='')
    leave_class = models.IntegerField("请假的研学大节")
    leave_reason = models.CharField("请假原因", max_length=50, default='')
    is_delete = models.BooleanField("是否已被删除", default=0)

    class Meta:
        db_table = 'user_leave_data'
        verbose_name = '用户的研学请假信息'
        verbose_name_plural = verbose_name

# 存储所有用户的操作次数
class operateTime(models.Model):
    user_id = models.CharField("用户账号", max_length=20, default='')
    operate_time = models.IntegerField("用户操作次数", default=0)

    class Meta:
        db_table = 'users_operate_times'
        verbose_name = '用户的操作次数'
        verbose_name_plural = verbose_name
