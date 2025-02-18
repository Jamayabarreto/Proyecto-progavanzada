from flask import Flask, request, jsonify, render_template
from flask_migrate import Migrate, upgrade
from models import db, MagicalGirl
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magical_girls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)  # Configurar Flask-Migrate

with app.app_context():
    db.create_all()

    # Aplicar las migraciones
    try:
        upgrade()
        print("Migración aplicada correctamente")
    except Exception as e:
        print(f"Error al aplicar la migración: {e}")

@app.route('/')
def index():
    girls = MagicalGirl.query.all()
    return render_template('index.html', girls=girls)

@app.route('/test', methods=['GET'])
def test_route():
    return jsonify({'message': '¡La configuración inicial está completa!'}), 200

@app.route('/magical_girls', methods=['POST'])
def create_magical_girl():
    data = request.get_json()
    new_girl = MagicalGirl(
        name=data['name'],
        age=data['age'],
        city=data['city'],
        status=data['status'],
        contract_date=datetime.strptime(data['contract_date'], '%Y-%m-%d'),
        race=data['race'],
        photo_url=data.get('photo_url')
    )
    db.session.add(new_girl)
    db.session.commit()
    return jsonify({'message': 'Chica mágica creada'}), 201

@app.route('/magical_girls', methods=['GET'])
def get_magical_girls():
    girls = MagicalGirl.query.all()
    return jsonify([girl.to_dict() for girl in girls])

@app.route('/magical_girls/<int:id>', methods=['DELETE'])
def delete_magical_girl(id):
    girl = MagicalGirl.query.get_or_404(id)
    db.session.delete(girl)
    db.session.commit()
    return jsonify({'message': 'Chica mágica eliminada'}), 200

@app.route('/magical_girls/<int:id>', methods=['PUT'])
def update_magical_girl(id):
    data = request.get_json()
    girl = MagicalGirl.query.get_or_404(id)
    girl.race = data.get('race', girl.race)
    girl.photo_url = data.get('photo_url', girl.photo_url)
    db.session.commit()
    return jsonify({'message': 'Chica mágica actualizada'}), 200

if __name__ == '__main__':
    app.run(debug=True)
