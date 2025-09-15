From python:3.12.3
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKIDR /app
ADD . /app

RUN PORT 8080

CMD ["gunicorn" , "app:app" , "--config=config.py"]
