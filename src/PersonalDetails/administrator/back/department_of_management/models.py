from django.db import models

# Create your models here.
class managementIdpassword(models.Model):
    manager_id = models.CharField("管理端用户账号", max_length=30, default='')
    password = models.CharField("管理端密码", max_length=30, default='')

    class Meta:
        db_table = 'manager_data'
        verbose_name = '管理端账号和密码'
        verbose_name_plural = verbose_name