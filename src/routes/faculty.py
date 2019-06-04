from flask import Blueprint
from src.util import RestApi

from src.controllers import FacultyResource, FacultyListResource


FACULTY_BLUEPRINT = Blueprint('faculty', __name__)

RestApi(FACULTY_BLUEPRINT).add_resource(
    FacultyListResource,
    '/faculties'
)

RestApi(FACULTY_BLUEPRINT).add_resource(
    FacultyResource,
    '/faculties/<string:id>'
)
