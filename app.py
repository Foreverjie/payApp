from flask import Flask
import config
from routes.index import main as index_routes

app = Flask(__name__)
app.secret_key = config.secret_key


app.register_blueprint(index_routes)

if __name__ == '__main__':
    app.run()
