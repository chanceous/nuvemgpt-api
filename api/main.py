import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
from dotenv import load_dotenv
from classes.NuvemIndex import NuvemIndex

load_dotenv()

api = Flask(__name__)
CORS(api, resources={r"/*": {"origins": "*"}})

openai.api_key = os.getenv("OPENAI_API_KEY")

@api.route('/query', methods=['POST'])
def query():
    return jsonify({
        "response": NuvemIndex.query(
            request.values.get('prompt')
        ),
        "code": 200,
    })
