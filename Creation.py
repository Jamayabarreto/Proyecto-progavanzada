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
    "name": "Bruno Fernandes",
    "age": 30,
    "city": "Maia",
    "status": "Rescatada por la lay de los ciclos",
    "contract_date": "2020-01-30",
    "race": "Demonio",
    "photo_url": "https://images.daznservices.com/di/library/GOAL/2c/20/bruno-fernandes-manchester-united-2020-21_1hyly9p0a6i8n1xwj51slqmgam.jpg?t=1020514389&w={width}&quality=80"
},
{
    "name": "James Maddison",
    "age": 28,
    "city": "Coventry",
    "status": "Activa",
    "contract_date": "2018-06-20",
    "race": "Gallinazo",
    "photo_url": "https://i2-prod.dailystar.co.uk/incoming/article31031371.ece/ALTERNATES/s1200/1_AFC-Bournemouth-v-Tottenham-Hotspur-Premier-League.jpg"
},
{
    "name": "Kaoru Mitoma",
    "age": 27,
    "city": "Kawasaki",
    "status": "Activa",
    "contract_date": "2021-08-10",
    "race": "Gaviota",
    "photo_url": "https://uk1.sportal365images.com/process/smp-image-api/livescore.com/11112022/a68c0047-6ecc-4991-8eae-26b51c5d7bfa.jpg"
},
{
    "name": "Son Heung-min",
    "age": 32,
    "city": "Chuncheon",
    "status": "desaparecida",
    "contract_date": "2015-08-28",
    "race": "Gallinazo",
    "photo_url": "https://d2x51gyc4ptf2q.cloudfront.net/content/uploads/2023/01/17151019/Son-spurs.jpg"
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