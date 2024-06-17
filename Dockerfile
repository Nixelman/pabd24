# syntax=docker/dockerfile:1

FROM python:3.9
WORKDIR /app
COPY ./src/predict_app.py ./src/predict_app.py
COPY ./.env ./.env
COPY ./models/GBR.joblib ./models/GBR.joblib

RUN pip3 install flask flask-cors flask_httpauth scikit-learn python-dotenv joblib numpy

# CMD ["python3", "src/predict_app.py"]
# EXPOSE 5000

RUN pip3 install gunicorn
CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "src.predict_app:app"]
EXPOSE 8000