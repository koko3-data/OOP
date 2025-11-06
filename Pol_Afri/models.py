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

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(1000), nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    #showing relationship torole-specific profiles
    client_profile = db.relationship("Client", back_populates="user", uselist=False, cascade="all, delete-orphan")
    service_provider_profile = db.relationship("ServiceProvider", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def generate_passsword(self, password: str):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        if check_password_hash(self.password_hash,password):
            return True
        return False

    
    
    def __repr__(self):
        return f"<Person {self.id} {self.username} ({self.role.value})>"
    
class Client(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    wallet = db.Column(db.Float, nullable=True, default=0.0)

    user = db.relationship("Person", back_populates="client_profile")

    def __repr__(self):
        return f"<Client {self.id} User ID: {self.user_id} Wallet: {self.wallet}>"
    

class ServiceProvider (db.Model):
    __tablename__ = "service_providers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    business_name = db.Column(db.String(120), nullable=False)
    speciality = db.Column(db.String(120), nullable=True)
    rate_multiplier = db.Column(db.Float, nullable=True, default=1.0)
    location = db.Column(db.String(255), nullable=True)

    user = db.relationship("Person", back_populates="service_provider_profile")
    
    provider_services = db.relationship("ProviderService", back_populates="provider", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ServiceProvider {self.id} User ID: {self.user_id} Speciality: {self.speciality} Rate Multiplier: {self.rate_multiplier}>"


    
class Service_category(db.Model):
    __tablename__ = "service_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False) # e.g Hair, Manicure, Food

    services = db.relationship("Service", back_populates="category", cascade="all, delete-orphan")
  

    def __repr__(self):
        return f"<ServiceCategory {self.id} Name: {self.name}>"

class ProviderService(db.Model):
    __tablename__ = "provider_services"

    id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey("services.id"), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey("service_providers.id"), nullable=False)
    base_price = db.Column(db.Float, nullable=True)
    duration_min = db.Column(db.Integer, nullable=True)

    provider = db.relationship('ServiceProvider', back_populates='provider_services')
    service = db.relationship('Service', back_populates='provider_services')

    def __repr__(self):
        return f"<ProviderService {self.id} Service ID: {self.service_id} Provider ID: {self.provider_id}>"


    
class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("service_categories.id"), nullable=False)
    name = db.Column(db.String(120), nullable=False) #e.g Knotless Braids, French Manicure
    description = db.Column(db.Text, nullable=True)

    
    category = db.relationship("Service_category", back_populates="services")
    provider_services = db.relationship("ProviderService", back_populates="service", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Service {self.id} Name: {self.name}>"
    



    

