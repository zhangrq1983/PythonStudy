
from pymongo import MongoClient
from bson.objectid import ObjectId

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

    def find_db(self, *args, **kwargs):
        item = None
        if args:
            print(args, type(args))
            item = self.db.find_one({'_id': ObjectId(args[0])})
        else:
            item = self.db.find()
        return item

    def delete_one(self, item):
        if isinstance(item, dict):
            self.db.delete_one(item)
        else:
            print('lei xing cuo wu')

    def delete_many(self, item):
        if isinstance(item, dict):
            self.db.delete_many(item)
        else:
            print('lei xing cuo wu')


    def update_one(self, ite, item):
        if isinstance(ite, dict) and isinstance(item, dict):
            self.db.update_one(ite, {'$set': item})
        else:
            print('lei xing cuo wu')

    def update_many(self, item):
        if isinstance(item, dict):
            self.db.update_many({}, {'$set': item})
        else:
            print('lei xing cuo wu')


if __name__ == '__main__':
    mg = MongoDb()
    # mg.insert_db([11, 22])
    # mg.insert_db({'user': 'jr'})

    # item = mg.find_db('5ebc1814a97aea3db76bd2d7')
    # print(item, type(item))

    # item = mg.find_db()
    # for i in item:
    #     print(i, type(i))

    # mg.delete_one({'user': 'jr'})
    #
    item = mg.find_db()

    for i in item:
        print(i, type(i))

    # mg.update_one({'user': 'jr'}, {'user': 'jr1'})

    mg.update_many({'user': 'jr1'})
