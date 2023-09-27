import pymongo
from datetime import datetime


def get_mongodb_remote():
    client_url = "mongodb+srv://kevin_miner_test:Peerless123@cluster0.458zxp3.mongodb.net/?retryWrites=true&w=majority"
    db_client = pymongo.MongoClient(client_url)
    return db_client


if __name__ == '__main__':
    coll_zero = get_mongodb_remote()['db_where_is_my_money_user_manager']['db_where_is_my_money_user_manager_coll']
    result = list(coll_zero.find())
    # str_time = (datetime.now().strftime("%d_%b_%Y_%H_%M_%S"))
    #  result = coll_zero.insert_one({"email": "peerelss@gmail.com", 'password': "password", 'date': str_time})
    for r in result:
        print(r)
