from flask import Flask, render_template


from .exntensions import db 



from .routes.main import main

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)




    app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///project.db'



    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    

    return app 