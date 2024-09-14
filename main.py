import os
from flask import Flask
from src.routes.cv_get import routes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(routes, url_prefix="/cv")


@app.route("/")
def index():
    return "nawas"


# ****************** main **********************
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 3000))
    )
