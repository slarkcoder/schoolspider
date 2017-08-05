# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *

db = MySQLDatabase("school", host='localhost', user="root", passwd="password", charset="utf8")

class EdulistItem(scrapy.Item):
    name = scrapy.Field()
    area = scrapy.Field()
    property = scrapy.Field()
    professional = scrapy.Field()
    belong_to = scrapy.Field()
    is_211 = scrapy.Field()
    is_985 = scrapy.Field()
    is_keypoint = scrapy.Field()
    is_independent = scrapy.Field()
    is_direct = scrapy.Field()
    is_graduate = scrapy.Field()
    level = scrapy.Field()
    category = scrapy.Field()
    phone = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    address = scrapy.Field()
    postcode = scrapy.Field()
    desc = scrapy.Field()


class EdulistModel(Model):

    id = PrimaryKeyField()
    name = CharField(verbose_name="学校名称", null=False, unique=False)
    area = CharField(verbose_name="所在地区", null=True, default='')
    property = CharField(verbose_name="学校性质", null=True, default='')
    professional = CharField(verbose_name="专业类型", null=True, default='')
    belong_to = CharField(verbose_name="隶属于", null=True, default='')
    is_keypoint = CharField(verbose_name="国家重点学科", null=True, default='')
    is_211 = CharField(verbose_name="是否为211", null=True, default='')
    is_985 = CharField(verbose_name="是否为985", null=True, default='')
    is_independent = CharField(verbose_name="独立学院", null=True, default='')
    is_direct = CharField(verbose_name="教育部直属", null=True, default='')
    is_graduate = CharField(verbose_name="是否包含研究生院", null=True, default='')
    level = CharField(verbose_name="学校级别", null=True, default='')
    category = CharField(verbose_name="学校类型", null=True, default='')
    phone = CharField(verbose_name="招生电话", null=True, default='')
    email = CharField(verbose_name="邮箱", null=True, default='')
    website = CharField(verbose_name="网站", null=True, default='')
    address = CharField(verbose_name="地址", null=True, default='')
    postcode = CharField(verbose_name="邮编", null=True, default='')
    desc = TextField(verbose_name="简介", null=True, default='')

    class Meta:
        database = db