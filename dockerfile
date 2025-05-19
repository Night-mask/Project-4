FROM Python:3.0
WORKDIR /app
COPY r.txt /app
RUN pip install -r r.txt
EXPOSE 5000
CMD ["python3","k.py"]
