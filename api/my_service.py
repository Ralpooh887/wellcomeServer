from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = self.path
        print(f"Query received: {query}")

        response = {
            "message": "Hello! This is my custom API response.",
            "query": query
        }

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))
