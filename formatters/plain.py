from formatters.base import Formatter


class PlainTextFormatter(Formatter):
    def format(self, data):
        return "\n".join(f"{key}: {value}" for key, value in data.items())