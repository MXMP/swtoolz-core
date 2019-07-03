FROM mxmp/python-netsnmp
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

WORKDIR /
#COPY requirements.txt ./
#RUN pip3 install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
#RUN rm requirements.txt

COPY . /app
WORKDIR /app
