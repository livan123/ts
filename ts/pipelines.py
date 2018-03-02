# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TsPipeline(object):

    def __init__(self):
        #首先执行的文件
        self.fh = open("F:/python_workspace/ts/file/ts.txt", "a")

    def process_item(self, item, spider):
        print(item["title"])
        print(item["link"])
        print(item["stu"])
        print("---------------------------------")
        self.fh.write(item["title"][0]+"\n"+item["link"][0]+"\n"+item["stu"][0]+"\n"+"-----------------------"+"\n")
        return item

    def close_spider(self):
        #默认最后执行的方法：
        self.fh.close()
