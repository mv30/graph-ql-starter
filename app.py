from flask import Flask
from flask import jsonify
from flask import request

from ariadne import graphql_sync
from ariadne import snake_case_fallback_resolvers
from ariadne import ObjectType
from ariadne import load_schema_from_path
from ariadne import make_executable_schema

from queries import resolve_any_one, resolve_find_one_by_id

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return 'Hello world'

@app.route("/graphql-any", methods=['POST'])
def find_any():
    data = request.get_json()
    success, result = graphql_sync( schema, data, context_value=request, debug=app.debug)
    return jsonify(result)

@app.route("/graphql-by-id", methods=['POST'])
def find_one_by_id():
    data = request.get_json()
    success, result = graphql_sync( schema, data, context_value=request, debug=app.debug)
    return jsonify(result)

query = ObjectType("Query")
query.set_field("findAny", resolve_any_one)
query.set_field("findOneById", resolve_find_one_by_id)
type_def = load_schema_from_path("schema.graphql")
schema = make_executable_schema( type_def, query, snake_case_fallback_resolvers)
