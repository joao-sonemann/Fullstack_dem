from app import db  

class user(db.Model):

    __tablename__= "user"

    id = db.Column(id.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.string(255), unique=True, nullable=False)
    function = db.Column(db.string(255), nullable=False)
    
    tasks = db.relationship('task', back_populates='user', uselist=True)

    def __init__(self, name, function):
        self.name = name
        self.function = function
        
    def __repr__(self):
        return "<User '{}'>".format(self.name)
    
    

 
