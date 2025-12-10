# 1. Use an official lightweight Python image
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy requirements first (for caching speed)
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Download the missing TextBlob data
RUN python -m textblob.download_corpora

# 6. Copy the rest of the app
COPY . .

# 7. Expose the port Streamlit runs on
EXPOSE 8501

# 8. Run the app
# --server.address=0.0.0.0 : REQUIRED to accept connections from outside
# --browser.serverAddress=localhost : OPTIONAL, makes the printed URL clickable
CMD [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=localhost"]