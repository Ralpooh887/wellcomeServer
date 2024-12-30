from http.server import BaseHTTPRequestHandler
from services.airtable_service import update_airtable_column
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 요청 데이터 읽기
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        # record_id 및 document_path 확인
        if "record_id" not in data or "document_path" not in data:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing 'record_id' or 'document_path' in request body")
            return

        # Airtable 업데이트 호출
        try:
            update_airtable_column(data["record_id"], data["document_path"])
            response = {"status": "success"}
        except Exception as e:
            response = {"status": "error", "message": str(e)}
            self.send_response(500)
            self.end_headers()
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        # 성공 응답
        self.send_response(200)
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))
