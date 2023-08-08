from app import db  

class Task(db.Model):

    __tablename__= "task"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descrybe = db.Column(db.String(255), unique=True, nullable=False)
    deadline = db.Column(db.Integer, nullable=False)
    id_user  = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[id_user], back_populates='task', uselist=False)

    def __init__(self, descrybe, deadline, id_user):
        self.descrybe = descrybe
        self.deadline = deadline
        self.id_user = id_user
        
    def __repr__(self):
        return "<Task '{}'>".format(self.descrybe)
