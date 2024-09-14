import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def index():
    return {
        "name": "123"
    }


# ****************** main **********************
if __name__ == "__main__":
    app.run(
        # debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 3000))
    )
