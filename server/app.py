#!/usr/bin/env python3


from flask import request, jsonify
from models import db, City
from config import app, api



@app.route('/cities', methods=['POST'])
def create_city():
    pass

@app.route('/cities', methods=['GET'])
def get_all_cities():
    pass

if __name__ == '__main__':
    app.run(port=5555, debug=True)

