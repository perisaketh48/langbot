FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

# Force pip to download the ultra-lightweight CPU-only PyTorch wheel
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 10000

CMD ["./start.sh"]