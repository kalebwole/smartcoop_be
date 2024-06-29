from . import db

class CooperativeMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phoneno = db.Column(db.String(20))
    address = db.Column(db.String(255))
    staff_id = db.Column(db.String(50))
    dob = db.Column(db.Date)
    password = db.Column(db.String(100), nullable=False)
    wallet = db.Column(db.Float, default=0)
    photo = db.Column(db.String(255))
    gender = db.Column(db.String(10))
    status = db.Column(db.String(20), default='active')

class MemberCooperative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('cooperative_member.id'), nullable=False)
    cooperative_id = db.Column(db.Integer, nullable=False)
