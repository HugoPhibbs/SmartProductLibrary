from flask import Blueprint, request

import src.core.query_engines.connection_query_engine as query_engine

connection_bp = Blueprint('connection', __name__)


@connection_bp.route('/<connection_id>', methods=['GET'])
def get_connection(connection_id: str):
    print(connection_id)
    connection = query_engine.get_connection_by_id(connection_id)
    return connection, 200 if connection else None, 404


@connection_bp.route("/filter", methods=["GET"])
def get_connections_by_filter():
    query_params = request.args.to_dict()

    results = query_engine.get_connections_by_filter(query_params)
    return results, 200


@connection_bp.route("/", methods=['GET'])
def get_all_connections():
    connections = query_engine.get_all_connections()
    return connections, 200


@connection_bp.route("/section-type", methods=['GET'])
def get_section_types():
    member_types = query_engine.get_section_types()
    return member_types, 200
