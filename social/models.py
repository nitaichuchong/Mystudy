from django.db import models


class Swiped(models.Model):
    '''滑动记录'''
    FLAGS = (
        ('superlike', '上滑'),
        ('like', '左滑'),
        ('dislike', '右滑'),
    )
    uid = models.IntegerField(verbose_name='滑动者的uid')
    sid = models.IntegerField(verbose_name='被滑动者的uid')
    flag = models.CharField(max_length=10, choices=FLAGS)
    dtime = models.DateTimeField(auto_now=True)


class Friend(models.Model):
    '''好友关系'''
    uid1 = models.IntegerField()
    uid2 = models.IntegerField()