from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .faculty import Faculty, FacultySchema
