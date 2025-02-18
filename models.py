from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class MagicalGirl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    contract_date = db.Column(db.Date, nullable=False)
    race = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)  # Nuevo campo para la URL de la foto

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'city': self.city,
            'status': self.status,
            'contract_date': self.contract_date.strftime('%Y-%m-%d'),
            'race': self.race,
            'photo_url': self.photo_url
        }

    contract_date = db.Column(db.Date, nullable=False)
    photo_url = db.Column(db.String(200), nullable=True)  # Nuevo campo para la URL de la foto

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'city': self.city,
            'status': self.status,
            'race': self.race,
            'contract_date': self.contract_date.strftime('%Y-%m-%d'),
            'photo_url': self.photo_url
        }
