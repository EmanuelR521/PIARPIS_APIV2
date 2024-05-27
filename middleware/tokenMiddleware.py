from datetime import datetime, timedelta, timezone
import jwt 
from config import config

conf = config()
def generate_token(username):
    try:
       payload = {
           'username':username,
           'exp': datetime.now(timezone.utc) + timedelta(hours=1)
       }
       secret_key = conf.jwt_secret
       token = jwt.encode(payload, secret_key, algorithm='HS256')
       return token
    except Exception as e:
        print(f"Error generating token ----> {e}\n\n")
        raise e
    


def decode_token(token):
    try:
        data = jwt.decode(token, conf.jwt_secret, algorithms=["HS256"])
        return data
    except jwt.ExpiredSignatureError:
        return None  # El token ha expirado
    except jwt.InvalidTokenError:
        return None  # Token inválido