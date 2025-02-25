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
            "name": "Erling Haaland",
            "age": 24,
            "city": "Oslo",
            "status": "activa",
            "contract_date": "2024-06-11",
            "race": "Humana",
            "photo_url": "https://icdn.benchwarmers.ie/wp-content/uploads/2022/10/Erling-Haaland.jpeg"
        },
        {
            "name": "Daniel Muñoz",
            "age": 27,
            "city": "Medellin",
            "status": "activa",
            "contract_date": "2021-05-21",
            "race": "Aguila",
            "photo_url": "https://cdn1.wearepalace.uk/uploads/28/2024/05/GettyImages-2151201013-scaled.jpg"
        },
        {
            "name": "ChipiChipi",
            "age": 24,
            "city": "Estocolmo",
            "status": "activa",
            "contract_date": "2024-12-15",
            "race": "Humana",
            "photo_url": "https://static0.givemesportimages.com/wordpress/wp-content/uploads/2024/02/newcastle-united-striker-alexander-isak-1.jpg"
        },
        {
            "name": "Chris Wood",
            "age": 32,
            "city": "Aukland",
            "status": "activa",
            "contract_date": "2017-03-01",
            "race": "Carpintero",
            "photo_url": "https://th.bing.com/th/id/OIF.xbDtYevDEzMLFGtM7qUtXg?w=302&h=180&c=7&r=0&o=5&dpr=1.1&pid=1.7"
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