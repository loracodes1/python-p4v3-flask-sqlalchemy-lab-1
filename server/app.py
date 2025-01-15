# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here
@app.route('/earthquakes/<int:id>')
def earthquakes(id):
    earthquake = Earthquake.query.filter(Earthquake.id==id).first()

    if earthquake is not None:
        body = {
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }

        return make_response(body)
    
    body = {'message': f"Earthquake {id} not found."}
    return make_response(body, 404)

@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquakes(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude>=magnitude).first()

    if quakes is not None:
        body = {
  "count": 2,
  "quakes": [
    {
      "id": 1,
      "location": "Chile",
      "magnitude": 9.5,
      "year": 1960
    },
    {
      "id": 2,
      "location": "Alaska",
      "magnitude": 9.2,
      "year": 1964
    }
  ]
}
        return make_response(body)
    
    body = {'message': f"Earthquake {id} not found."}
    return make_response(body, 404)

    




if __name__ == '__main__':
    app.run(port=5555, debug=True)
