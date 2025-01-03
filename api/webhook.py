from http.server import BaseHTTPRequestHandler
from services.document_service import create_word_document, convert_to_pdf
from services.airtable_service import update_airtable_with_files
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 요청 데이터 읽기
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)

        record_id = data.get("record_id")
        if not record_id:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing 'record_id'")
            return

        try:
            # 1. Word 문서 생성
            word_file_path = create_word_document(data)

            # 2. PDF로 변환
            pdf_file_path = convert_to_pdf(word_file_path)

            # 3. Airtable에 파일 제출
            update_airtable_with_files(record_id, word_file_path, pdf_file_path)

            # 성공 응답
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Files uploaded successfully")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode("utf-8"))
