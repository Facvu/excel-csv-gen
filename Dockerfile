FROM amancevice/pandas

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install flask
RUN pip install flask_restful
RUN pip install uwsgi

COPY . /app

CMD ["uwsgi", "--http", "0.0.0.0:8000", "--wsgi-file", "app.py", "--callable", "app"]
#CMD ["./start.sh"]

#CMD ["nginx","-g","daemon off;"]
#CMD ["uwsgi", "--ini", "uwsgi.ini"]
