from http.server import BaseHTTPRequestHandler
import json
from services.document_service import generate_document
from services.airtable_service import update_airtable_column

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 요청 데이터 읽기
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        webhook_data = json.loads(body)

        # record_id 추출
        record_id = webhook_data.get("record_id")
        if not record_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing record_id in webhook data")
            return

        try:
            # 1. 문서 생성
            document_path = generate_document(webhook_data)

            # 2. Airtable 업데이트
            update_airtable_column(record_id, document_path)

            # 응답
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Webhook processed successfully")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode("utf-8"))
