import os
import datetime
import shutil
import zipfile
from jinja2 import Environment, FileSystemLoader
from webhelpers import paginate
from messages import parse_line
from model import Log

env = Environment(loader=FileSystemLoader('templates'))
log_template = env.get_template('archivelog.html')

class PageURL(object):
    """A simple page URL generator for any framework."""

    def __init__(self, path):
        """
        ``path`` is the current URL path, with or without a "scheme://host"
         prefix.

        ``params`` is the current URL's query parameters as a dict or dict-like
        object.
        """
        self.path = path

    def __call__(self, page, partial=False):
        return str(page) + ".html"

def zipdir(path, ziph, logname):
    for root, dirs, files in os.walk(path):
        for f in files:
            ziph.write(os.path.join(root, f), logname + '/' + f)

def export_chat(redis, sql, url):
    log = sql.query(Log).filter(Log.url == url).scalar()

    if not log:
        return

    # Create temp directory.
    if not os.path.exists('tmp/' + log.url):
        os.makedirs('tmp/' + log.url)

    # Create export pages.
    for page in log.pages:
        with open('tmp/' + log.url + '/' + str(page.number) + '.html', 'w') as f:
            paginator = paginate.Page([], page=page.number, items_per_page=1, item_count=log.page_count, url=PageURL(log.url))

            lines = page.content.split('\n')[0:-1]
            lines = map(lambda _: parse_line(_, 0), lines)

            for line in lines:
                line['datetime'] = datetime.datetime.fromtimestamp(line['timestamp'])

            f.write(log_template.render(
                lines=lines,
                paginator=paginator
            ).encode("utf8"))

    # Copy static assets
    if not os.path.exists('tmp/' + log.url + '/static'):
        os.makedirs('tmp/' + log.url + '/static')

    shutil.copyfile('static/js/bbcode.js', 'tmp/' + log.url + '/static/bbcode.js')
    shutil.copyfile('static/js/jquery.min.js', 'tmp/' + log.url + '/static/jquery.min.js')
    shutil.copyfile('static/css/msparp.css', 'tmp/' + log.url + '/static/msparp.css')
    shutil.copyfile('static/css/chat.css', 'tmp/' + log.url + '/static/chat.css')

    # Create export zip.
    with zipfile.ZipFile('logs/' + log.url + ".zip", 'w', zipfile.ZIP_DEFLATED) as logzip:
        zipdir('tmp/'+log.url, logzip, log.url)