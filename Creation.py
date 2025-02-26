from flask import Flask
from models import db, MagicalGirl
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magical_girls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

    # Lista de chicas mágicas a crear
    girls = [
        {
    "name": "Mohamed Salah",
    "age": 32,
    "city": "Nagrig",
    "status": "Activa",
    "contract_date": "2017-07-01",
    "race": "Faraon",
    "photo_url": "https://vignette.wikia.nocookie.net/liverpoolfc/images/0/05/MSalah2018.jpeg/revision/latest?cb=20180809023000"
    },

    {
    "name": "Trent Alexander-Arnold",
    "age": 26,
    "city": "Liverpool",
    "status": "Desaparecida",
    "contract_date": "2016-07-01",
    "race": "Dragon",
    "photo_url": "https://firstsportz.com/wp-content/uploads/2020/06/1196090853-2048x1415.jpg"
    },

    {
    "name": "Luis Díaz",
    "age": 28,
    "city": "Barrancas",
    "status": "Desaparecida",
    "contract_date": "2022-01-30",
    "race": "Dragon",
    "photo_url": "https://www.thickaccent.com/wp-content/uploads/2022/01/Screenshot-2022-01-30-at-12.11.35-PM-957x1024.jpg.webp"
    },

    {
    "name": "Jean-Philippe Mateta",
    "age": 27,
    "city": "Sevran",
    "status": "rescatada por la Ley de los Ciclos",
    "contract_date": "2021-03-21",
    "race": "Aguila",
    "photo_url": "https://static01.nyt.com/athletic/uploads/wp/2024/01/03112113/GettyImages-1874247973-scaled.jpg"
    }   
    ]

    # Crear y añadir cada chica mágica a la base de datos
    for girl_data in girls:
        existing_girl = MagicalGirl.query.filter_by(name=girl_data["name"]).first()
        if not existing_girl:
            new_girl = MagicalGirl(
                name=girl_data["name"],
                age=girl_data["age"],
                city=girl_data["city"],
                status=girl_data["status"],
                contract_date=datetime.strptime(girl_data["contract_date"], "%Y-%m-%d"),
                race=girl_data["race"],
                photo_url=girl_data["photo_url"]
            )
            db.session.add(new_girl)
            db.session.commit()
            print(f"Chica mágica {new_girl.name} creada")
        else:
            print(f"Chica mágica {girl_data['name']} ya existe en la base de datos")


'''
from flask import Flask
from models import db, MagicalGirl

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///magical_girls.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    # Obtener la chica mágica por ID
    girl_id = 3  # Cambia esto al ID de la chica mágica que quieres actualizar
    new_race = "Urraca"  # La nueva raza que quieres asignar

    girl = MagicalGirl.query.get(girl_id)
    if girl:
        girl.race = new_race
        db.session.commit()
        print(f"Raza de {girl.name} actualizada a {new_race}")
    else:
        print(f"No se encontró una chica mágica con ID {girl_id}")
'''