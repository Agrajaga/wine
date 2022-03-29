import collections
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pandas import read_excel


def get_winery_age(start_year):
    measurements = ('лет', 'год', 'года', 'года', 'года',
                    'лет', 'лет', 'лет', 'лет', 'лет')

    age = str(datetime.date.today().year - start_year)
    return f'{age} {measurements[int(age[-1])]}'


def get_drinks_by_category(filename):
    drinks_by_category = collections.defaultdict(list)
    file_content = read_excel(
        filename, keep_default_na=False).to_dict(orient='records')
    for element in file_content:
        drinks_by_category[element['Категория']].append(element)
    return drinks_by_category


if __name__ == "__main__":
    start_year = 1920
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        winery_age=get_winery_age(start_year),
        drinks_by_category=get_drinks_by_category('wine.xlsx')
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
