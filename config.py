import yaml

class config:
    def __init__(self) -> None:
        with open('config.yaml') as file:
            config = yaml.load(file, Loader=yaml.FullLoader)
            self.mongo_uri = config['mongo']['mongo_uri']
            self.mongo_db = config['mongo']['mongo_db']
            self.ia_ip = config['ia']['ip']
            self.ia_port = config['ia']['port']
            self.ia_token = config['ia']['token']
            self.flask_secret = config['flask']['secret']
            
            
            
            