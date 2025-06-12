# Morfo Case
This is the Senior Data Engineer case solution!

# How to run with Docker:
docker build -t morfo-etl .
docker run --rm -v "${PWD}/data:/app/data" morfo-etl
