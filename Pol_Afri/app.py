import re
from flask import Flask, redirect, render_template, request, url_for,session
from flask_migrate import Migrate
from models import Client
from authenticate import authenticate_user
from models import Person, RoleEnum, ServiceProvider, db
from werkzeug.security import generate_password_hash

from config import Config


app = Flask(__name__)


#Load configuration connection
app.config.from_object(Config)

#start migrations
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/', methods=['GET', 'POST']) #Defining the route for the login page
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = authenticate_user(username,password)
        
        if user:
            role =user.role.value
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = role

            if role == 'admin' :
                return redirect(url_for('admin_dashboard'))
            elif role == 'client':
                return redirect(url_for('client_dashboard'))
            elif role == 'service_provider':
                return redirect(url_for('service_provider_dashboard'))
            else:
                return "Unknown role, Please contact support."
        else:
            #if username exists but password forgotten
            existing_user = Person.query.filter_by(username=username).first()
            if existing_user:
                error_msg = "Incorrect password. Please try again."
                return render_template('login.html', error=error_msg)
            else:
                return redirect(url_for('register',error = "Invalid username or password. Please register new user"))
        
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])  # Defining the route for the Register page
def register():
    error_mssg = request.args.get('error')
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    password_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#^()[\]{}._+-=])[A-Za-z\d@$!%*?&#^()[\]{}._+-=]{8,}$' # Minimum eight characters, at least one letter and one number  
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        role = request.form['role']
        if role not in [' client', 'service_provider']:
            role = 'client'  # Default role
        elif role == 'admin':
            return "Unauthorized admin registration attempt."
        
        #validating all fields are filled
        if not all([username, password, first_name, last_name, email, role]):
            error_mssg = "All fields are required."
            return render_template('register.html', error=error_mssg)
        
        # Validating email format
        if not re.match(email_regex, email):
            error_mssg = "Invalid email format."
            return render_template('register.html', error=error_mssg)
        
        # Validating password strength
        if not re.match(password_regex, request.form['password']):
            error_mssg = "Password must be at least 8 characters long, include uppercase and lowercase letters, a number, and a special character."
            return render_template('register.html', error=error_mssg)
        
        if Person.query.filter_by(username=username).first() == True:
            error_mssg = "Username already exists. Please choose a different username."
            return redirect(url_for('login'), error=error_mssg)
        
        else:
            new_user = Person(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                role=RoleEnum(role)
            )
            new_user.generate_passsword(request.form['password'])

            db.session.add(new_user)
            db.session.commit()

        # Create profile based on role
            if role == 'client':
                db.session.add(Client(user_id=new_user.id))
            elif role == 'service_provider':
                db.session.add(ServiceProvider(user_id=new_user.id, business_name=f"{first_name}'s Business"))
            db.session.commit()

            return redirect(url_for('login'))
    
   
    return render_template('register.html', error=error_mssg)


@app.route('/admin')
def admin_dashboard():
    return render_template('admin.html')

@app.route('/client')
def client_dashboard():
    return render_template('client.html')

@app.route('/service_provider')
def service_provider_dashboard():
    return render_template('service_provider.html')

#To run the app
if __name__ == "__main__":
    app.run(debug=True)

