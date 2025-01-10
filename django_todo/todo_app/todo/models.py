from django.db import models
import datetime
# Create your models here.
# class User(db.Model):
#     __tablename__ = 'users'
#     user_id = db.Column(db.Integer, primary_key=True)
#     first = db.Column(db.String(50), unique=True, nullable=False)
#     last = db.Column(db.String(50), unique=True, nullable=False)
#     username = db.Column(db.String(50), nullable=False)
#     password = db.Column(db.String(225), nullable=False)
#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
#     tasks = db.relationship('Task', backref='user', lazy=True)

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(default=datetime.datetime.now)