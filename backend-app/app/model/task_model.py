from app import db  

class task(db.Model):

    __tablename__= "task"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    descrybe = db.Column(db.string(255), unique=True, nullable=False)
    deadline = db.Column(db.Integer, nullable=False)
    
    user_id  = db.Column(db.integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', foreign_keys=[user_id], back_populates='task', uselist=False)

    def __init__(self, descrybe, deadline, user_id):
        self.descrybe = descrybe
        self.deadline = deadline
        self.user_id = user_id
        
    def __repr__(self):
        return "<Task '{}'>".format(self.descrybe)
