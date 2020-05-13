
from pymongo import MongoClient

client = MongoClient()


class MongoDb (object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client['demo']['test4']

    def insert_db(self, item):
        try:
            if isinstance(item, dict):
                self.db.insert_one(item)
            elif isinstance(item, list):
                item = {str(i): i for i in item}
            else:
                print(type(item))
        except Exception as e:
            print("插入数据库报错:", e)


if __name__ == '__main__':
    mg = MongoDb()
    mg.insert_db([11, 22])
    # mg.insert_db({'user': 'jr'})
