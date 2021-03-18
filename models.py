def create_rent(db):
    class Rent(db.Model):
        __tablename__ = 'rent'

        id = db.Column(db.Integer, primary_key=True)
        city = db.Column(db.String(240))
        state = db.Column(db.String(240))
        year = db.Column(db.Integer)
        month = db.Column(db.Integer)
        price = db.Column(db.Integer)

        def __repr__(self):
            return '<Rent %r>' % (self.name)
    return Rent

def create_house(db):
    class House(db.Model):
        __tablename__ = 'house'

        id = db.Column(db.Integer, primary_key=True)
        city = db.Column(db.String(240))
        state = db.Column(db.String(240))
        year = db.Column(db.Integer)
        month = db.Column(db.Integer)
        price = db.Column(db.Integer)

        def __repr__(self):
            return '<House %r>' % (self.name)
    return House