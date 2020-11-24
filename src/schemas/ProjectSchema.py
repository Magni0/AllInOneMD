from main import ma
from models.Project import Project

class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project