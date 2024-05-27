#flask api
import requests
from flask import Flask, request, jsonify, Response
from pymongo import MongoClient
from flask_pymongo import PyMongo
import pymongo
import json
from config import config
from functools import wraps
from datetime import datetime as dt
from flask_cors import CORS
import hashlib
from bson import json_util, ObjectId
import jwt
from datetime import datetime, timedelta, timezone
import api
from api import mongo
import middleware.tokenMiddleware as tokenMiddleware
import bcrypt
conf = config()

def login(): #Add user to session
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        token = request.headers.get('token')
        if(token):
            return jsonify({'message': 'user already logged in'}), 401
        if checkPassword(username,password):
            token = tokenMiddleware.generate_token(username)
            print(f"------------------User {username} logged in as {token}------------------\n\n")
            #session.append(token)
            return jsonify({'token': token}), 200
        else:
            return jsonify({'message': 'login failed'}), 401
    except Exception as e:
        print(f"Error logging in ----> {e}\n\n")
        return jsonify({'message': 'error in route login'}), 500
    
def checkPassword(username,password) -> bool: # check if the password is correct
    try:
        userFound = mongo.db.users.find_one({'username': username})
        print(f"User found ----> {userFound}\n\n")
        password = password.encode('utf-8')
        if bcrypt.checkpw(password,userFound['password']):
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking password ----> {e}\n\n")
        return False
'''    
def logout(): #Remove user from session
    try:
        token = request.headers.get('token')
        return jsonify({'message': 'logout successful'}), 200
    except Exception as e:
        print(f"Error logging out ----> {e}\n\n")
        return jsonify({'message': 'error logging out'}), 500
'''