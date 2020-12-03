FROM python:3.8
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

# 작성자 정보(옵션)
MAINTAINER Hyunwoo Hong <hw.hwhong@haezoom.com>
