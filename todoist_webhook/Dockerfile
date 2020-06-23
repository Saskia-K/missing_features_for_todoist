FROM python:3.6

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8800

RUN apt-get update
RUN apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

CMD [ "python", "src/main.py" ]
