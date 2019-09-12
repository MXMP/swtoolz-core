FROM mxmp/python-netsnmp:python3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN pip3 install python3-netsnmp easysnmp aiohttp

WORKDIR /

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3", "swtoolz-core.py", "nodaemon"]