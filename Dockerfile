FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
ENV PORT 8080
ENV APP_MODULE app.api:app
ENV LOG_LEVEL debug
ENV WEB_CONCURRENCY 2

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

RUN pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_core_sci_scibert-0.5.1.tar.gz

COPY ./app /app/app