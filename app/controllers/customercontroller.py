from flask import Blueprint, request, jsonify
from app.statuscode import HTTP_400_BAD_REQUEST,HTTP_409_NOT_CONFLICT,HTTP_500_INTERNAL_SERVER_ERROR,HTTP_201_CREATED,HTTP_404_NOT_FOUND,HTTP_403_FORBIDDEN,HTTP_200_OK
import validators
from app.models.customermodel import customer
from app.extensions import db,bcrypt
from flask_jwt_extended import jwt_required, get_jwt_identity

 customer blueprint
customer = Blueprint('customer', _name_,url_prefix='/api/v1/customer')

# customer registration

@customer.route("/register,methods=['POST']")
def create_a_customer():
    data = request.json
    name = data.get('name')
    id = data.get('id')
    title   = data.get('title')
    contact = data.get('contact')
    location = data.get('location')
    created_at=data.get('created_at')
    updated_at = data.get('updated_at')
     #Creating the customer
         customer = customer(id=id,at,created_at=created_at,title=title, updated_at=updated_at, contact=contact, location=location)
         db.session.add(customer)
         db.session.commit()
