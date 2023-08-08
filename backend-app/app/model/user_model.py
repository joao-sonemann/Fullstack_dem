from app import db  

class User(db.Model):

    __tablename__= "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    function = db.Column(db.String(255), nullable=False)
    
    task = db.relationship('task', back_populates='user', uselist=True)

    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def __repr__(self):
        return "<User '{}'>".format(self.name)
    
    

 
