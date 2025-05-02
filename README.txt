1.pip install Flask
2.Create app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)

3.python app.py

4. Cấu trúc project chuẩn
/project/
│
├── app.py
├── /templates/         ← HTML (Jinja2)
│    └── index.html
├── /static/            ← CSS, JS, hình ảnh
│    └── style.css



5. Install FlaskSqlAlchemy
    - pip install flask-sqlalchemy pymysql

6. Install flask-admin
    - pip install flask-admin


NOTE WHEN OPEN SOURCE CODE
source .venv/bin/activate