FROM python:3

WORKDIR /usr/src/app

# docker-compose対応にパスを書き換え
COPY flask_blog_app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
