FROM alpine:latest

RUN apk add --no-cache python3-dev
RUN apk add --update py-pip

WORKDIR /service

COPY . /service

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD python3 demo/__init__.py