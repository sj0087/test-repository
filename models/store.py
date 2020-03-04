from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    
    items = db.relationship('ItemModel', lazy='dynamic')
    
    # when we use lazy= dynamic self.item no 
    # longer is a list of items, now it is query builder that has the ability to look into the 
    # items table, then we can use .all to retrieve all the items in that table

    def __init__(self,name):
        self.name = name
       
    def json(self):
        return {'name' : self.name, 'items' : [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name=name).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  #it will update and insert both
       
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()  
                      
#internal representation  so it also has to contain the properties of an item  as object property