from datetime import datetime  
from app.extensions import db
# category 
class category(db.Model):

    # The tabel name
    __tablename__ = 'category'
   
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    title = db.Column(db.String(20), nullable = False)

    # time stamps
    created_at = db.Column(db.DateTime, default = datetime.now())
    updated_at = db.Column(db.DateTime, default = datetime.now())


        # Defining all the attributes
        def __init__(self,id,title, created_at, updated_at):
         self.id = id
         self.title = title
         self.created_at = created_at
         self.updated_at = updated_at