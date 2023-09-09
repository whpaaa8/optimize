from django.contrib.auth.hashers import make_password, check_password
from django.db import models
import hashlib


# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20, verbose_name="账号", unique=True)
    password = models.CharField(max_length=20, verbose_name="密码")
    uname = models.CharField(max_length=20, verbose_name="用户名")

    class Meta:
        verbose_name = '用户信息'
        ordering = ['username']

    def set_password(self):
        self.password = make_password(self.password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # # md5 = hashlib.md5()
        # # md5.update(self.password.encode())
        # self.password = md5.hexdigest()
        self.set_password()
        super(UserInfo, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
