from formatters.plain import PlainTextFormatter
from formatters.json_fmt import JSONFormatter
from formatters.csv_fmt import CSVFormatter


def get_formatter(format_type: str):
    formatters = {
        "plain": PlainTextFormatter
        "json": JSONFormatter
        "csv": CSVFormatter 
    }


formatter_class = formatters.get(format_type.lower())
if not formatter_class:
    raise ValueError(f"Unknown format type: {format_type}")
return formatter_class

