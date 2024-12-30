from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # HTML 안내 문구
        html_content = """
        <html>
            <head>
                <title>Welcome to Wellcome Server</title>
            </head>
            <body>
                <h1>Welcome to Wellcome Server</h1>
                <p>This server handles API endpoints like:</p>
                <ul>
                    <li><a href="/webhook">/webhook</a>: For handling webhooks.</li>
                    <li><a href="/service">/service</a>: For API services.</li>
                </ul>
            </body>
        </html>
        """

        # 응답 전송
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html_content.encode("utf-8"))
