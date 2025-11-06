from models import Person
from werkzeug.security import generate_password_hash,check_password_hash


def authenticate_user(username, password):
    user = Person.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    else:
        return None

  #For Admin passsword generation testing  
# def hashed_password(password):
#     Hashed_password = generate_password_hash(password)
#     print(f"Hashed Password: {Hashed_password}")

# if __name__ == "__main__":
#     password = input("Enter password to hash: ")
#     hashed_password(password)

# def check_passqord(password_hash,password):
#      if check_password_hash(password_hash,password):
#             print(f"Password match")
#      else:
#             print(f"Password do not match")

# if __name__ == "__main__":
#     password_hash = input("Enter hashed password: ").strip()
#     password = input("Enter password to check: ").strip()
#     check_passqord(password_hash,password)
    