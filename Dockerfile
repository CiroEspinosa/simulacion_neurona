FROM python:3.8
RUN pip install pandas scikit-learn streamlit
COPY src/app.py /app/
WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py"]

