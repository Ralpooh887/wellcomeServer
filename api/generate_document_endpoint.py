from http.server import BaseHTTPRequestHandler
from services.document_service import generate_document
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 요청 데이터 읽기
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        # record_id 확인
        if "record_id" not in data:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing 'record_id' in request body")
            return

        # 문서 생성 호출
        try:
            document_path = generate_document(data)
            response = {"status": "success", "document_path": document_path}
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
