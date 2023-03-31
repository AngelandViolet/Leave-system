from django.db import models

# Create your models here.
# 存储所有管理员账号和密码
class managerIdPass(models.Model):
    manager_id = models.CharField("管理员账号", max_length=20, default='')
    manager_pass = models.CharField("管理员密码", max_length=100, default='')

    class Meta:
        db_table = 'manager_log_information'
        verbose_name = '管理员的登录信息'
        verbose_name_plural = verbose_name
