import os
from flask import Flask


def create_app(test_config=None):
    # here we are creating and configuring the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='a4a72987d5cd8f3df196496c9b4616f35301fa678dfb73cc475fe914ed8b0701',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')
    
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app


# waitress-serve --call 'flaskr:create_app' use this to run the app
