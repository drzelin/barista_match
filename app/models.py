from app import db

class Barista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Barista {}>'.format(self.name)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cafe_name = db.Column(db.String(64), index=True, unique=True)
    owner_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    phone = db.Column(db.Numeric(precision=8, asdecimal=False, decimal_return_scale=None))

    def __repr__(self):
        return '<Cafe {}>'.format(self.cafe_name)
