# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

class DiscountPipeline(object):
    def process_item(self, item, spider):
        return item



class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('jd.json', 'wb', encoding='utf-8')
        self.file.write('{\n"item":[\n')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.write('{}\n]\n}')
        self.file.close()