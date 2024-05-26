import yaml


#a basic mongo-like testing db for development
class MongoClient:
    def __init__(self, uri):
        self.uri = uri
        yaml_data = yaml.safe_load(open('db.yaml'))
        self.db = {}
        for collection in yaml_data:
            self.db[collection] = Collection(yaml_data, collection)
         
    def __getitem__(self, key):
        return self.db

    def __setitem__(self, key, value):
        self.db = value

    def __delitem__(self, key):
        return
    
class Collection:
    def __init__(self, db, collection):
        self.db = db
        self.collection = collection
        self.data = self.db[self.collection]
        
    def find_one(self, query):
        #search the first element where each key in query is in the data
        for item in self.data:
            found = True
            for key in query:
                if key not in item or item[key] != query[key]:
                    found = False
                    break
            if found:
                return item
        return None
        
    def insert_one(self, data):
        self.data.append(data)
        yaml.safe_dump(self.db, open('db.yaml', 'w'))
        
    def delete_one(self, query):
        #delete the first element where each key in query is in the data
        for item in self.data:
            found = True
            for key in query:
                if key not in item or item[key] != query[key]:
                    found = False
                    break
            if found:
                self.data.remove(item)
                yaml.safe_dump(self.db, open('db.yaml', 'w'))
                return True
        

if __name__ == '__main__':
    import pandas as pd
    client = MongoClient('db.yaml')
    database = client['db']
    users_collection = database['Usr']
    usr_df = pd.DataFrame(users_collection.data)
    usr_df.to_csv('users.csv')
    parking_collection = database['Parkings']
    park_df = pd.DataFrame(parking_collection.data)
    park_df.to_csv('parkings.csv')
    
    #testing collections methods
    print(users_collection.find_one({'name': 'admin'}))
    print(users_collection.find_one({'name': 'admin1'}))
    print(parking_collection.find_one({'name': 'civic con portatil'}))
    
    #testing insert
    users_collection.insert_one({'name': 'test', 'password': 'test'})
    print(users_collection.find_one({'name': 'test'}))
    


    