FROM python:2.7.13
MAINTAINER Your Name "zacharyzhong1116@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN pip install  PyYAML
ENTRYPOINT ["python","app.py"]
