import pymongo

# client = pymongo.MongoClient("mongodb+srv://kevin_miner_test:Peerless123@cluster0.458zxp3.mongodb.net/?retryWrites=true&w=majority")
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
my_db = my_client['miner_tx']
my_col = my_db['miner_tx_offline']
my_col_user = my_db['miner_tx_users']


class Miner:
    def __init__(self, ip, model, result, memo):
        self.ip = ip
        self.model = model
        self.result = result
        self.memo = memo


class User:
    def __init__(self, name, password, position):
        self.name = name
        self.password = password
        self.position = position


def get_data():
    myquery = {}
    result_x = my_col_user.find(myquery)
    for x in result_x:
        print(x)


def insert_users():
    av_user = User('kevin', 'root', 'root')
    query = {'name': av_user['name']}

    my_col_user.insert_one(av_user.__dict__)


def insert_data():
    av_item = Miner('10.1.55.22', 'S19j-94T', 'Empty Miner', "")
    # my_col.insert_one(av_item.__dict__)


if __name__ == "__main__":
    #insert_users()
    get_data()
