from datetime import datetime  
from app.extensions import db
# category 
class customer(db.Model):

    # The tabel name
    __tablename__ = 'customer'
   
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    title = db.Column(db.String(20), nullable = False)
    name     = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
    contact = db.Column(db.Integer, nullable = False)
    # time stamps
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, default = datetime.now())

            # Defining all the attributes
        def __init__(self,id, title, name, contact, location, created_at, updated_at):
         self.id = id
         self.title = title
         self.name = name
         self.contact = contact
         self.location = location
         self.created_at = created_at
         self.updated_at = updated_at