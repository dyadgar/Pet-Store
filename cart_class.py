from flask import Flask, render_template
import flask_wtf
import wtforms
from wtforms.validators import data_required, Length
import json
import random



class Cart:
    total = 0


    def addtocart(self,id):
        with open('all_pets.json','r') as f:
            data = json.load(f)
            data = data['pets']
            pet = list(filter(lambda x: x['id'] == id, data))[0]

        with open('cart.json','r') as f:
            data = json.load(f)
            data.append(pet)

        with open('cart.json', 'w') as f:
            json.dump(data,f)
        Cart.total += pet['price']


    def getcart(self):
        with open('cart.json', 'r') as f:
            cart_list = json.load(f)
            return cart_list




