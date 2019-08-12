import requests

from flask import Flask, Response, jsonify, render_template
from flask import request as flask_request

from flask_cors import CORS
import os

from ddtrace import tracer
from ddtrace.ext.priority import USER_REJECT, USER_KEEP

import subprocess
import random

from os import environ

app = Flask('api')

if os.environ['FLASK_DEBUG']:
    CORS(app)

# Uncomment below if working in Kubernetes
  
# IMAGE_CLIP_URL = f"http://{environ['IMAGE_CLIP_SERVICE_HOST']}:{environ['IMAGE_CLIP_SERVICE_PORT_HTTP']}"
# NOTES_URL = f"http://{environ['NOTES_SERVICE_SERVICE_HOST']}:{environ['NOTES_SERVICE_SERVICE_PORT']}"
# AUTHENTICATION_URL = f"http://{environ['AUTHENTICATION_SERVICE_HOST']}:{environ['AUTHENTICATION_SERVICE_PORT_HTTP']}"
# GOLANG_URL = f"http://{environ['GO_CONCURRENT_SERVICE_SERVICE_HOST']}:{environ['GO_CONCURRENT_SERVICE_SERVICE_PORT']}"

# app.logger.info("Image Clip URL: " + IMAGE_CLIP_URL)
# app.logger.info("Notes URL: " + NOTES_URL)
# app.logger.info("Authentication URL: " + AUTHENTICATION_URL)

@app.route('/')
def homepage():
    return app.send_static_file('index.html')

