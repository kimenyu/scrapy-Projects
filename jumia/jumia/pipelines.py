# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class JumiaPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = 'Boyfaded7552',
            database = 'jumia'
        )
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS jumia_tb""")
        self.curr.execute("""CREATE TABLE jumia_tb(
            name VARCHAR(250),
            price VARCHAR(250)
            )""")
    
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        for i in range(len(item['name'])):
            self.curr.execute("""INSERT INTO jumia_tb VALUES (%s, %s)""",(
            item['name'][i],
            item['price'][i]
        ))
    
        self.conn.commit()