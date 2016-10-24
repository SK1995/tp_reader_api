from __init__ import db


class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String, unique=True, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    password= db.Column(db.String)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.email)

    def __repr__(self):
        return '<user: %s>' % (self.email)