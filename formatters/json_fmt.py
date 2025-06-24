import json

from formatters.base import Formatter


class JSONFormatter(Formatter):
    def format(self, data):
        return json.dumps(data, indent=4)