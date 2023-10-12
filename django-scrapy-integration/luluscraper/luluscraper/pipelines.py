# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class LuluscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Price data clean
        price_field = adapter.get('price')
        adapter['price'] = price_field[0]

        return item


class SaveProductPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1234',
            database='lulu'
        )

        ## Create cursor, used to execute commands
        self.cur = self.conn.cursor()

        ## Create books table if none exists
        self.cur.execute(
            """
                CREATE TABLE IF NOT EXISTS products
                (
                    id int NOT NULL auto_increment,
                    title text,
                    price VARCHAR(255),
                    PRIMARY KEY (id)
                )
            """
        )

    def process_item(self, item, spider):
        ## Define insert statement
        self.cur.execute(
            """ INSERT INTO products 
            (
                title,
                price
            ) values 
            (
                %s,
                %s
            )
            """,
            (
                str(item["title"]),
                item["price"]
            )
        )

        ## Execute insert of data into database

        self.conn.commit()

        return item

    def close_spider(self, spider):
        ## Close cursor & connection to database
        self.cur.close()
        self.conn.close()

