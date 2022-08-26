from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256))
    completed = db.Column(db.Boolean, default=False)

    def save_task_to_db(self):
        db.session.add(self)
        db.session.commit()

    def complete_task(self):
        self.completed = True if self.completed == False else False
        db.session.commit()
