from flask import ( Blueprint, render_template )
import json 

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")

@bp.route('/')
def index(): 
    return render_template('index.html', pets=pets)

@bp.route('/new')
def new(): 
    return render_template('new.html')

@bp.route('/show/<int:id>')
def show(id):
    pet = next((pet for pet in pets if pet["pet_id"] == id), None)
    if pet:
        return render_template('show.html', pet=pet)
    else:
        return "Pet not found", 404
