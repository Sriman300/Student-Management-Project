from datetime import datetime
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse

from controllers.students import (
    get_all_students
    # , get_student
    # , create_student
    # , update_student
    # , delete_student
)

from core.static import serve_static
from core.responses import send_404
from core.middleware import add_cors_headers


class StudentRouter(BaseHTTPRequestHandler):
    def do_Get(self):
        # path = urlpare(self.path).path

        # if path in ("/", "/index.html"):

        #     return serve(self)
        #     if path.startswith("/static/")
        #     return serve_static(self)

        #     if path == "/api/students":
        #         return get_all_students(self)

                if path.startswith("/api/students/"):
                    student_id = int(path.split("/")[-1])
                    return get_student_(self, student_id)

                    return send_404(self)