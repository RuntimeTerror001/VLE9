FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

COPY app/ /usr/share/nginx/html/
COPY security/ ./security/

RUN pip install flask

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]