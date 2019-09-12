#!/usr/bin/env python3
import asyncio
import logging
import sys
from os import sep

from aiohttp import web

from daemon import Daemon
from handlers import handle_get
from swconfig import logfile
from swconfig import port

logging.basicConfig(filename=logfile, level=logging.DEBUG, format='%(levelname)s %(asctime)s  %(message)s')

# Добавляем директорию 'devices' в список path. Это нужно, чтобы демон мог находить модули в этой директории
sys.path.append('%s%sdevices' % (sys.path[0], sep))


async def main():
    app = web.Application()
    app.add_routes([web.get('/{user}/{target_ip}/{comm_index}/{commands:.*}', handle_get)])

    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, port=port)
    await site.start()
    app.logger.info(f"Serving app on {site._host}:{site._port} ...")  # Да, я знаю, что лучше так не делать
    return runner, site


class MyDaemon(Daemon):
    def run(self):
        main()


if __name__ == "__main__":
    daemon = MyDaemon('/var/run/swtoolz-core.pid', '/dev/null', logfile, logfile)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'faststart' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        elif 'nodaemon' == sys.argv[1]:
            loop = asyncio.get_event_loop()
            runner, site = loop.run_until_complete(main())
            try:
                loop.run_forever()
            except KeyboardInterrupt:
                loop.run_until_complete(runner.cleanup())
            loop.close()
        else:
            print("swtoolz-core: " + sys.argv[1] + " - unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: %s start|stop|restart|nodaemon" % sys.argv[0])
        sys.exit(2)
