from flask import Flask, request, jsonify, render_template
from models import db, MagicalGirl, StateHistory
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magical_girls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    girls = MagicalGirl.query.all()
    return render_template('index.html', girls=girls)

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

    new_status = StateHistory(
        girl_id=new_girl.id,
        status=new_girl.status,
        change_date=datetime.now()
    )
    db.session.add(new_status)
    db.session.commit()
    
    return jsonify({'message': 'Chica mágica creada'}), 201

@app.route('/magical_girls', methods=['GET'])
def get_magical_girls():
    girls = MagicalGirl.query.all()
    return jsonify([girl.to_dict() for girl in girls])

@app.route('/magical_girls/<int:id>', methods=['GET'])
def get_magical_girl(id):
    girl = MagicalGirl.query.get_or_404(id)
    print(girl.id)  # Debugging statement
    return render_template('profile.html', girl=girl)


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
    girl.status = data.get('status', girl.status)
    girl.photo_url = data.get('photo_url', girl.photo_url)
    db.session.commit()

    new_status = StateHistory(
        girl_id=girl.id,
        status=girl.status,
        change_date=datetime.now()
    )
    db.session.add(new_status)
    db.session.commit()

    return jsonify({'message': 'Chica mágica actualizada'}), 200

# Ruta para filtrar por estado
@app.route('/magical_girls/state', methods=['GET'])
def filter_by_status():
    status = request.args.get('estado')
    print(f"Estado recibido: {status}")  # Depuración
    if status and status != "*":
        girls = MagicalGirl.query.filter(db.func.lower(MagicalGirl.status) == status.lower()).all()
        print(f"Chicas encontradas: {[girl.name for girl in girls]}")  # Depuración
        if not girls:
            print("No se encontraron chicas con ese estado.")
    else:
        girls = MagicalGirl.query.all()
    return render_template('index.html', girls=girls)



# Ruta para obtener los distintos estados
@app.route('/magical_girls/statuses', methods=['GET'])
def get_statuses():
    statuses = db.session.query(MagicalGirl.status).distinct().all()
    statuses = [status[0] for status in statuses]  # Extraer los valores de status del resultado
    return jsonify(statuses)


if __name__ == '__main__':
    app.run(debug=True)
