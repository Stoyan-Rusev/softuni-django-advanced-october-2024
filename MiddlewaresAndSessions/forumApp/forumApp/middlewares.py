import time
from django.utils.deprecation import MiddlewareMixin


class MeasureTimeExecution(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()

    def process_view(self, request, view, *args, **kwargs):
        print("Its processing")

    def process_template_response(self, request, response):
        print("It's in the process template response")
        return response

    def process_exception(self, request, exception):
        print(f"The exception that happend was {exception}")

    def process_response(self, request, response):
        self.end_time = time.time()
        total_time = self.end_time - self.start_time
        print(f"New class measure time: {total_time}")
        return response
