import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel

def get_winery_age():
    measurements = ('лет', 'год', 'года', 'года', 'года', 'лет', 'лет', 'лет', 'лет', 'лет')
    start_year = 1920
    age = str(datetime.date.today().year - start_year)
    return f'{age} {measurements[int(age[-1])]}'


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

excel_wines_filename = 'wine.xlsx'

rendered_page = template.render(
    winery_age=get_winery_age(),
    wines=read_excel(excel_wines_filename).to_dict(orient='records')
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()