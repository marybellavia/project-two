def create_rent(db):
    class Rent(db.Model):
        __tablename__ = 'Rent'

        RegionId = db.Column(db.Integer, primary_key=True)
        SizeRank = db.Column(db.Integer)
        State = db.Column(db.String(240))
        City = db.Column(db.String(240))
        Year = db.Column(db.Integer)
        Month = db.Column(db.Integer)
        Price = db.Column(db.Integer)

    return Rent

def create_house(db):
    class House(db.Model):
        __tablename__ = 'House'

        RegionId = db.Column(db.Integer, primary_key=True)
        SizeRank = db.Column(db.Integer)
        State = db.Column(db.String(240))
        City = db.Column(db.String(240))
        Year = db.Column(db.Integer)
        Month = db.Column(db.Integer)
        Price = db.Column(db.Integer)

    return House