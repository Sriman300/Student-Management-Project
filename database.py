import json 
import database
from utils.responses import send_json,send_404

def parse_body(handler):
    length = int(handlers.headers.get("Content_Length", 0))
    raw = handler.rfile.read(length)
    return json.loads(raw.decode("utf-8"))

def get_all