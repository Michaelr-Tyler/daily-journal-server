from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from entries import get_all_entries, get_single_entry, delete_entry
from instructors import get_all_instructors, get_single_instructor
from moods import get_all_moods, get_single_mood

class HandleRequests(BaseHTTPRequestHandler):

    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        # Check if there is a query string parameter
        if "?" in resource:


            param = resource.split("?")[1]  
            resource = resource.split("?")[0]  
            pair = param.split("=")  
            key = pair[0]  
            value = pair[1]  

            return ( resource, key, value )

        # No query string parameter
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass  # No route parameter exists: 
            except ValueError:
                pass  # Request had trailing slash: 

            return (resource, id)

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type')
        self.end_headers()

    # Get request
    def do_GET(self):
        self._set_headers(200)

        response = {}

        # Parse URL and store entire tuple in a variable
        parsed = self.parse_url(self.path)

        # Response from parse_url() is a tuple with 2
        # items in it, which means the request was for
        # `/entries` or `/entries/2`
        if len(parsed) == 2:
            ( resource, id ) = parsed

            if resource == "entries":
                if id is not None:
                    response = f"{get_single_entry(id)}"
                else:
                    response = f"{get_all_entries()}"
            elif resource == "instructors":
                if id is not None:
                    response = f"{get_single_instructor(id)}"
                else:
                    response = f"{get_all_instructors()}"
            elif resource == "moods":
                if id is not None:
                    response = f"{get_single_mood(id)}"
                else:
                    response = f"{get_all_moods()}"

        elif len(parsed) == 3:
            ( resource, key, value ) = parsed
            if key == "#" and resource == "#":
                pass

        self.wfile.write(response.encode())
    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        # Convert JSON string to a Python dictionary
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        if resource == "entries":
            pass



    # Here's a method on the class that overrides the parent's method.
    # It handles any PUT request.
    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        # Parse the URL
        (resource, id) = self.parse_url(self.path)

        if resource == "entries":
            pass
        self.wfile.write("".encode())


    def do_DELETE(self):
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "entries":
            delete_entry(id)
        self.wfile.write("".encode())



# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()

if __name__ == "__main__":
    main()