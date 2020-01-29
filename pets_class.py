from flask import Flask, render_template, render_template_string, url_for,redirect
import json
import flask_wtf
import wtforms
from wtforms.validators import data_required, Length, ValidationError
import random

app=Flask(__name__)
app.config['SECRET_KEY']= random._urandom(16)


class Pet():

    def getPets(self):
        with open('all_pets.json','r') as f:
            pet_list=json.load(f)
        return pet_list['pets']



    def getPetId(self,id):
        with open('all_pets.json','r') as f:
            pet_list=json.load(f)
        for eachPet in pet_list['pets']:
            if eachPet['id']==id:
                return eachPet






