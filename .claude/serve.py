import functools
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

DIRECTORY = "/Users/ahmedali/Downloads/design_handoff_sprints_launch"
PORT = int(os.environ.get("PORT", "4599"))
Handler = functools.partial(SimpleHTTPRequestHandler, directory=DIRECTORY)
ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
