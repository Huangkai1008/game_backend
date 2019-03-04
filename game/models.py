from django.db import models


# Create your models here.

class Game(models.Model):
    """
    游戏
    """
    name = models.CharField('游戏中文名', max_length=120)
    foreign_name = models.CharField('游戏外文名', max_length=50)
    language = models.CharField('游戏语言', max_length=256)
    tags = models.CharField('游戏标签', max_length=256)
    company = models.CharField('制作公司', max_length=40)
    type = models.CharField('游戏类型', max_length=20)
    desc = models.TextField('游戏简介')


