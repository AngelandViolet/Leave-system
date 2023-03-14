from django.db import models

# Create your models here.
class invitationCodes(models.Model):
    invitation_code = models.CharField('邀请码', max_length=20, default='')

    class Meta:
        db_table = 'invitation_codes'
        verbose_name = '邀请码列表'
        verbose_name_plural = verbose_name
class logAndsign(models.Model):
    user_id = models.CharField("用户账号", max_length=30, default='')
    password = models.CharField("用户密码", max_length=30, default='')
    the_sector = models.CharField("用户方向", max_length=20, default='')
    number_of_session = models.CharField("用户届数", max_length=5, default='')

    class Meta:
        db_table = 'user_data'
        verbose_name = '用户账号和密码'
        verbose_name_plural = verbose_name
        ordering = ['number_of_session']