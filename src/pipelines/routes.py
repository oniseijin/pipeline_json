from flask import Blueprint, render_template, request, jsonify
from src.models.models import Pipeline
import datetime
import base64
import hashlib

bp = Blueprint('pipelines', __name__)


@bp.route('/')
def get_pipelines():  # put application's code here
    p = Pipeline.get_pipelines()
    return render_template('pipeline.html', pipelines=p)

@bp.route('/insert_pipeline', methods=['POST'])
def insert_pipeline():
    if request.method == "POST":
        json_data = request.json
        attributes = json_data['attributes']  # this has to be json again, so may need to convert
        project = attributes['project']   #
        # TODO, anything else to lift to the highest level?
        # hash needs to be computed by something else
        hash_string = project + attributes['timestamp'] # from timestamp
        hash_value = hashlib.md5(hash_string.encode('utf-8')).hexdigest()
        Pipeline.create(project, hash_value, attributes)
        return jsonify(json_data)


@bp.route('/update_state', methods=['POST'])
def update_state():
    # just needs the hash and the state change
    if request.method == "POST":
        json_data = request.json
        Pipeline.change_state(json_data['hash_value'], json_data['state'])
        return jsonify(json_data)