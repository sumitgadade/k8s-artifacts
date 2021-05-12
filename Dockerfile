FROM python:3.7

WORKDIR /opt/app

COPY ./myapp .
RUN pip install pytz tzlocal
RUN pip install --no-cache-dir -r req-prd.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
