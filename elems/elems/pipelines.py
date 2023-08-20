from itemadapter import ItemAdapter
import mysql.connector
import copy, json

class GroupElements:

    def __init__(self):
        self._elems = {}

    def process_item(self, item, spider):
        chemical_group = item['chemical_group']

        if chemical_group not in self._elems:
            self._elems[chemical_group] = {"element_count": 0,
                                           "elements": []}

        item_copy = copy.deepcopy(item)
        del item_copy['chemical_group']

        self._elems[chemical_group]['elements'].append(dict(item_copy))
        self._elems[chemical_group]['element_count'] += 1

        return item

    def close_spider(self, spider):

        with open("elements.json", 'w') as f:
            json.dump(self._elems, f)


class SaveToMySQL:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def __init__(self, settings):

        self.conn = mysql.connector.connect(

            host = settings.get('MYSQL_HOST'),
            user = settings.get('MYSQL_USER'),
            password = settings.get('MYSQL_PASSWORD'),
            port = settings.get('MYSQL_PORT'),
            database = settings.get('MYSQL_DATABASE')

        )

        self.cur = self.conn.cursor()

    def process_item(self, item, spider):

        self.cur.execute("""
            INSERT INTO periodic_elements (
                symbol, name, atomic_number, atomic_mass, chemical_group
            ) VALUES (
                %s, %s, %s, %s, %s
            )""", (item['symbol'], item['name'], item['atomic_number'],
                   item['atomic_mass'], item['chemical_group'])
        )

        self.conn.commit()

        return item

    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()