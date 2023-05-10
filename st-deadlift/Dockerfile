From python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py entries.csv ./

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]