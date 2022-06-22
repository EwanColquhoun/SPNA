from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    """Used to prepare the html from the summernote
    fields for use in emails. Based on
    https://stackoverflow.com/questions/11061058/using-htmlparser-in-python-3-2"""
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
