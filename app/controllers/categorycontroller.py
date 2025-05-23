from flask import Blueprint, request, jsonify
from app.statuscode import HTTP_400_BAD_REQUEST,HTTP_409_NOT_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_403_FORBIDDEN,HTTP_200_OK
import validators
from app.models.categorymodel import categories
from app.extensions import db,bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity

 categories blueprint
categories = Blueprint('category', _name_,url_prefix='/api/v1/category')

# user registration

@category.route("/register,methods=['POST']")
def create_a_category():
    data = request.json
    id = data.get('id')
    title   = data.get('title')


    