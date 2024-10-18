from flask import Flask
from flask_jwt_extended import JWTManager
from routes.auth import auth
from routes.users import users
from config import SECRET_KEY

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = SECRET_KEY

jwt = JWTManager(app)

app.register_blueprint(auth, url_prefix='/api/auth')
app.register_blueprint(users, url_prefix='/api/users')

if __name__ == '__main__':
    app.run(debug=True)