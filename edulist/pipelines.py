# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from edulist.items import EdulistModel

class EdulistPipeline(object):
    def process_item(self, item, spider):
        if EdulistModel.table_exists() == False:
            EdulistModel.create_table()

        school = EdulistModel(
            name=item['name'],
            area=item['area'],
            property=item['property'],
            professional=item['professional'],
            belong_to=item['belong_to'],
            is_keypoint=item['is_keypoint'],
            is_211=item['is_211'],
            is_985=item['is_985'],
            is_independent=item['is_independent'],
            is_direct=item['is_direct'],
            is_graduate=item['is_graduate'],
            level=item['level'],
            category=item['category'],
            phone=item['phone'],
            email=item['email'],
            website=item['website'],
            address=item['address'],
            postcode=item['postcode'],
            desc=item['desc']
                              )
        school.save()

        return item