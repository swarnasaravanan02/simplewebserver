from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title> my device</title>
    </head>
    <body>
        <h1>DEVICE SPECIFICATIONS - 25009452</h1>
        <table border="3" cellspacing="5">
            <tr>
                <th>S.NO.</th>
                <th>Device name</th>
                <th>graphics card</th>
                
            </tr>
            <tr>
                <td>1</td>
                <td>Processor</td>
                <td>13th Gen Intel(R) Core</td>
            
            </tr>
            <tr>
                <td>2</td>
                <td>Device ID</td>
                <td>4A587D00</td>
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