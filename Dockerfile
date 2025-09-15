From python:3.12.3
RUN pip install virtualenv
ENV VIRTUAL_ENV=/venv
RUN virtualenv venv -p python3
ENV PATH="VIRTUAL_ENV/bin:$PATH"

WORKdiR /app
ADD . /app

ENV PORT 8080

CMD ["gunicorn" , "app:app" , "--config=config.py"]
