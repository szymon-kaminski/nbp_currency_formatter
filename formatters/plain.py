from formatters.base import Formatter


class PlainTextFormatter(Formatter):
    def format(self, data):
        if not data:
            return "No data available."
        return "\n".join(f"{key}: {value}" for key, value in data.items())