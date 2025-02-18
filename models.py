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
    photo_url = db.Column(db.String(200), nullable=True)
    state_history = db.relationship('StateHistory', backref='magical_girl', lazy=True)

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

class StateHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    girl_id = db.Column(db.Integer, db.ForeignKey('magical_girl.id'), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    change_date = db.Column(db.Date, nullable=False)
