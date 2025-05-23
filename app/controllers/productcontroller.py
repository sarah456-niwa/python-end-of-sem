from flask import Blueprint, request, jsonify
from app.statuscode import HTTP_400_BAD_REQUEST,HTTP_409_NOT_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_403_FORBIDDEN,HTTP_200_OK
import validators
from app.models.productmodel import products
from app.extensions import db,bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity

 products blueprint
products = Blueprint('product', _name_,url_prefix='/api/v1/product')

#API endpoint POST
@product.route("/register,methods=['POST']")
def create_a_customer():
    data = request.json
    id = data.get('id')
    title   = data.get('title')
    price = data.get('price')
    description = data.get('description', '')if type == "description" else ''

#API end point PUT
#editing a product
@product.route("/register,methods=['PUT']")
def edit_a_product():
    data = request.json
    id = data.get('id')
    title   = data.get('title')
    price = data.get('price')
    description = data.get('description', '')if type == "description" else ''

#API endpoint GET
#getting products
@product.route("/register,methods=['GET']")
def get_all_products():
    data = request.json
    id = data.get('id')
    title   = data.get('title')
    price = data.get('price')
    description = data.get('description', '')if type == "description" else ''
    
#API endpoint DELETE
#Deleting a product
    @product.route("/register,methods=['DELETE']")
def delete_a_product():
    data = request.json
    id = data.get('id')
    title   = data.get('title')
    price = data.get('price')
    description = data.get('description', '')if type == "description" else ''#

