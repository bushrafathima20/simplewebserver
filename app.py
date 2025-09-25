from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
       <title>
        bush's Page
       </title>
    </head>
    <body>
        <h1><b>
            Device Specification(BUSH)
            </b>
        </h1>
        <table BORDER="5">
        <tr>
        <th>S.NO</th>
        <th>DEVICE NAME</th>
        <th>RAM</th>
        <th>DEVICE ID</th>
        <th>PRODUCT ID</th>
        <th>SYSTEM TYPE</th>
        </tr>
        <tr>
            <td>1</td>
        <td>BUSH</td>
        <td>AMD Asus AI 5 350 w/Radeon 860M</td>
        <td>64.0GB</td>
        <td>00123-98765-76543-AAOEM</td>
        <td>32-bit operating system,x64-based processor</td>
        </tr>
        </table>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()