from . import db
from datetime import datetime

class Post(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(99), nullable=False)
    content   = db.Column(db.String)
    email      = db.Column(db.String, nullable=False)
    picture     = db.Column(db.String)
    created_at   = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, server_default=db.func.now())
    
    def __repr__(self):
        return f"<Post {self.content}>"
    
