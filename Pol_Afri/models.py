import enum
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()

class RoleEnum(enum.Enum):
    admin = "admin"
    client = "client"
    service_provider = "service_provider"


class Person(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    #showing relationship torole-specific profiles
    client_profile = db.relationship("Client", backpopulates="user", uselist=False, cascade="all, delete-orphan")
    service_provider_profile = db.relationship("ServiceProvider", backpopulates="user", uselist=False, cascade="all, delete-orphan")

    def generate_password_hash(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        if check_password_hash(self.password_hash,password):
            return True
        return False

    
    
    def __repr__(self):
        return f"<Person {self.id} {self.username} ({self.role.value})>"
    
class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    wallet = db.Column(db.Float, nullable=True, default=0.0)

    user = db.relationship("Person", backpopulates="client_profile")

    def __repr__(self):
        return f"<Client {self.id} User ID: {self.user_id} Wallet: {self.wallet}>"

class ServiceProvider (db.Model):
    __tablename__ = "service_providers"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    business_name = db.Column(db.String(120), nullable=False)
    speciality = db.Column(db.String(120), nullable=True)
    rate_multiplier = db.Column(db.Float, nullable=True, default=1.0)
    location = db.Column(db.String(255), nullable=True)

    user = db.relationship("Person", backpopulates="service_provider_profile")

    def __repr__(self):
        return f"<ServiceProvider {self.id} User ID: {self.user_id} Speciality: {self.speciality} Rate Multiplier: {self.rate_multiplier}>"

class Service_category(db.Model):
    __tablename__ = "service_category"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    name = db.Column(db.String(120), unique=True, nullable=False) # e.g Hair, Manicure, Food
  

    def __repr__(self):
        return f"<ServiceCategory {self.id} Name: {self.name}>"
    
class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    category_id = db.Column(db.Integer, db.ForeignKey("service_categories.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False) #e.g Knotless Braids, French Manicure

    
    category = db.relationship("Service_category", backref=db.backref("services", lazy=True))
    

    def __repr__(self):
        return f"<Service {self.id} Name: {self.name} Duration: {self.duration_min}min Base Price: {self.base_price} {self.currency}>"
    
class Provider_Service(db.Model):
    __tablename__ = "provider_services"

    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey("service_providers.id"), nullable=False)
    base_price = db.Column(db.Float, nullable=True)
    duration_min = db.Column(db.Integer, nullable=True)

    service = db.relationship("Service", backref=db.backref("provider_services", lazy=True))
    provider = db.relationship("ServiceProvider", backref=db.backref("provider_services", lazy=True))

    def __repr__(self):
        return f"<ProviderService {self.id} Service ID: {self.service_id} Provider ID: {self.provider_id} Custom Price: {self.custom_price}>"



