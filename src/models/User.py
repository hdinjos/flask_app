from src import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, username=None, email=None):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username!r}>'
