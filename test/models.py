db = SQLAlchemy()

class car_origin(db.model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50), nullable=False)
    brands = db.relationship("car_brand", back_populates="car", cascade="all, delete-orphan")
    expectancy = db.relationship("car_expectancy", back_populates="brand", cascade="all, delete-orphan")
 

class car_brand(db.model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    brand_name = db.Column(db.String(100), nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    car = db.relationship("car_origin", back_populates="brands")

class car_expectancy(db.model):
    __tablename__ = "car_expectancy"
    id = db.Column(db.Integer, primary_key=True)
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    average_lifespan_years = db.Column(db.Integer, nullable=False)
    brand = db.relationship("car_origin", back_populates="expectancy")

class car_owner(db.model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(150), nullable=True)
    owners_id = db.Column(db.Integer, db.ForeignKey("cars.id"), nullable=False)
    owned_car = db.relationship("car_origin",backref="owners")
    



