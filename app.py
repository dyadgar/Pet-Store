from flask import Flask, render_template
import flask_wtf
import wtforms
import json

import random
from pets_class import Pet
# from cart_class import Cart

app=Flask(__name__)
app.config['SECRET_KEY']= random._urandom(16)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pets')
def pets():
    lists = Pet()
    all_pets= lists.getPets()
    return render_template('pets.html',petlist=all_pets)

@app.route('/pet/<int:id>')
def petId(id):
    lists= Pet()
    one_pet=lists.getPetId(id)
    return render_template('pet.html', one_pet=one_pet)

# @app.route('/cart/<int:id>',method=['POST'])
# def addToCart(id):
#     lists= Class()
#     each_pet=lists.getPetId(id)
#     return render_template('cart.html', each_pet=each_pet)

# @app.route('/add', methods=['POST'])
# def addToCart():
#     form= Cart()
#
#     if form.is_submitted():
#         id=form.id.data
#         name=form.name.data
#         type=form.type.data
#         image=form.image.data
#         description=form.description.data
#         price=form.price.data
#
#
#         with open('cart.json', 'r') as f:
#             cart= json.load(f)
#             add = { 'Id': id, 'Name': name, 'Type': type, 'Image': image, 'Description': description, 'Price': price}
#             cart.append(add)
#
#         with open('cart.json','w') as f:
#             json.dump(cart, f)
#
#         return render_template('addToCart.html', form=form)

if __name__ =='__main__':
    app.run(debug=True)