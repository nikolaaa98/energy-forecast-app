from app import db

class DataEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    load = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    # Add more fields as needed

    def __repr__(self):
        return f'<DataEntry {self.timestamp}>'
