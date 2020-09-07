import sys
import logging
from os import sep

from aiohttp import web

from handlers import handle_get
from swconfig import logfile, debug_mode

# Добавляем директорию 'devices' в список path. Это нужно, чтобы демон мог находить модули в этой директории
sys.path.append('%s%sdevices' % (sys.path[0], sep))

if debug_mode:
    logging_level = logging.DEBUG
else:
    logging_level = logging.INFO
logging.basicConfig(filename=logfile, level=logging_level, format='%(levelname)s %(asctime)s  %(message)s')


async def swtoolz_core_app():
    app = web.Application()
    app.add_routes([web.get('/{user}/{target_ip}/{comm_index}/{commands:.*}', handle_get)])
    return app
