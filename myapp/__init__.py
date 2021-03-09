from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import Config


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    migrate.init_app(app,db)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login' ### name of the view

    with app.app_context():

        from myapp.home.views import bp_home, bp_login, bp_logout, bp_regist
        app.register_blueprint(bp_home)
        app.register_blueprint(bp_login)
        app.register_blueprint(bp_logout)
        app.register_blueprint(bp_regist)

        from myapp.dashapp_nondb_1.views import bp1
        app.register_blueprint(bp1)

        from myapp.dashapp_nondb_2.views import bp2
        app.register_blueprint(bp2)

        from myapp.dashapp_3.views import bp3
        app.register_blueprint(bp3)




        from myapp.dashapp_nondb_1.dash_app_1 import init_dashboard
        app = init_dashboard(app)
        app = app.server

        from myapp.dashapp_nondb_2.dash_app_2 import init_dashboard
        app = init_dashboard(app)
        app = app.server

        from myapp.dashapp_3.dash_app_3 import init_dashboard
        app = init_dashboard(app)
        app = app.server



        return app