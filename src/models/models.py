from src import db
import datetime
from flask import jsonify

# Pipeline 2 table

class Pipeline(db.Model):
    __tablename__ = "pipeline2"
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, default=datetime.datetime.utcnow)
    hash_value = db.Column(db.String(32), unique=True, nullable=False)
    state = db.Column(db.String(10))
    attributes = db.Column(db.JSON, nullable=False)
    last_update = db.Column(db.TIMESTAMP)

    def __init__(self, project: str, hash_value: str, attributes: str):
        self.project = project
        self.hash_value = hash_value
        self.state = "RUNNING"
        self.attributes = attributes

    @staticmethod
    def create(project, hash_value, attributes):  # create new user
        new_pipeline = Pipeline(project, hash_value, attributes)
        db.session.add(new_pipeline)
        db.session.commit()

    @staticmethod
    def change_state(hash_value, state):
        pipeline = Pipeline.query.filter(Pipeline.hash_value == hash_value)
        pipeline.update({'state': state, "last_update": datetime.datetime.utcnow()})
        db.session.commit()
        return pipeline

    @staticmethod
    def get_pipelines():
        return [{'pipeline_id': i.id, 'project': i.project, 'timestamp': i.timestamp, 'last_update': i.last_update, 'hash_value': i.hash_value, 'state': i.state, 'attributes': i.attributes}
            for i in Pipeline.query.order_by(Pipeline.id.desc()).limit(500)]
