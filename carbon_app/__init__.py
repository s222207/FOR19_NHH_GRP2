from flask import Flask
import os
application = Flask(__name__)

# = os.environ['SECRET_KEY]
application.config['SECRET_KEY'] = '9295f1efe735f29d3b8a645260d191075ec8c0d09625826e'

from carbon_app.home.routes import home
from carbon_app.methodology.routes import methodology
from carbon_app.carbon_calculator.routes import carbon_calculator
from carbon_app.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_calculator)
application.register_blueprint(users)