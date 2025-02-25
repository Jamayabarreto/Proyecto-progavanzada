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
            "name": "Cole Palmer",
            "age": 22,
            "city": "Manchester",
            "status": "activa",
            "contract_date": "2025-01-15",
            "race": "Leon",
            "photo_url": "https://uk1.sportal365images.com/process/smp-image-api/livescore.com/23012024/b4a32bbf-2e73-4f49-8a49-1dd5d57b7b75.jpg"
        },
        {
            "name": "Bryan Mbeumo",
            "age": 27,
            "city": "Avallon",
            "status": "rescatada por la Ley de los Ciclos",
            "contract_date": "2021-08-21",
            "race": "Abeja",
            "photo_url": "https://static01.nyt.com/athletic/uploads/wp/2023/12/07093935/bryan-mbeumo-scaled-e1701962367529.jpeg"
        },
        {
            "name": "Matheus Cunha",
            "age": 25,
            "city": "João Pessoa",
            "status": "activa",
            "contract_date": "2024-06-02",
            "race": "Lobo",
            "photo_url": "https://icdn.caughtoffside.com/wp-content/uploads/2025/02/tottenham-wolves-matheus-cunha-1536x1078.jpg"
        },
        {
            "name": "Ollie Watkins",
            "age": 26,
            "city": "Exeter",
            "status": "Desaparecida",
            "contract_date": "2020-04-11",
            "race": "Leon",
            "photo_url": "https://mercatofootanglais.com/wp-content/uploads/2023/04/ollie-watkins-scaled.jpg"
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