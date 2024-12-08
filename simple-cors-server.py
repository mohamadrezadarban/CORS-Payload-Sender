from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):

    # Handle POST requests
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')

            print("Received POST data:", post_data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

        except Exception as e:
            print(f"Error handling POST request: {e}")
            self.send_response(500)
            self.end_headers()

    # Handle GET requests
    def do_GET(self):
        print("Received GET request")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"GET method is supported")

    # Handle OPTIONS request (CORS preflight request)
    def do_OPTIONS(self):
        print("Received OPTIONS request")
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    # Generic error handler
    def log_message(self, format, *args):
        print(f"{self.address_string()} - {format % args}")

# Start the server
if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 8081
    try:
        server = HTTPServer((HOST, PORT), MyHandler)
        print(f"Server running on http://{HOST}:{PORT}")
        server.serve_forever()

    except KeyboardInterrupt:
        print("\nServer shutting down.")
        server.socket.close()
