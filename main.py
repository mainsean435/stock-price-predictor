from email import message
from flask import Flask
from flask_restx import Api
from exts import db
from models import Stock, User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from stocks import stock_ns
from transactions import transaction_ns
from auth import auth_ns
from flask_cors import CORS

def create_app(config):
    """
    Initialize the application and set ups all the necessary i.e database controllers and authentication manager
    Returns the application object initializes with the provided configurations.
    """
    #Create the app object
    app=Flask(__name__,static_url_path='/',static_folder='./client/build')
    app.config.from_object(config)

    @app.route('/')
    def index():
        message = "Hello world!"
        return f"<h1>{message}</h1>"
        # return app.send_static_file('index.html')

    #Allow cross origin policy
    CORS(app)

    db.init_app(app)

    #Initialize the database controller and JWT authentication manager
    migrate=Migrate(app,db)
    JWTManager(app)


    api=Api(app,doc='/docs')

    api.add_namespace(stock_ns)
    api.add_namespace(transaction_ns)
    api.add_namespace(auth_ns)


    @app.errorhandler(404)
    def not_found(err):
        return app.send_static_file('404.html')

    #model (serializer)
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Stock":Stock,
            "User":User
        }

    return app
