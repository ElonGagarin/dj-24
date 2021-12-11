import datetime

class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value):
        value = datetime.strptime(value, self.regex)

        return value

    def to_url(self, value):
        return value.__str__()