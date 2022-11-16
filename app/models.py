from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    player_url = db.Column(db.Text(), nullable=False)
    short_name = db.Column(db.Text(), nullable=False)
    long_name = db.Column(db.Text(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    dob = db.Column(db.Text(), nullable=False)
    height_cm = db.Column(db.Integer(), nullable=False)
    weight_kg = db.Column(db.Integer(), nullable=False)
    nationality = db.Column(db.Text(), nullable=False)
    club = db.Column(db.Text(), nullable=False)
    joined = db.Column(db.Text(), nullable=False)

    def to_dict(self):
        return{
            'player_url': self.player_url,
            'short_name': self.short_name,
            'long_name': self.long_name,
            'age': self.age,
            'dob': self.dob,
            'height_cm': self.height_cm,
            'weight_kg': self.weight_kg,
            'nationality': self.nationality,
            'club': self.club,
            'joined': self.joined
        }
