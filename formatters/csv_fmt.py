import csv
import io

from formatters.base import Formatter

class CSVFormatter(Formatter):
    def format(self, data):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Currency", "Rate"])
        for key, value in data.items():
            writer.writerow([key, value])
        return output.getvalue()