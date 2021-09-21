
FROM python:3-alpine

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

# COPY ./ /usr/app/

EXPOSE 8000

# Change this part to point to the right python script
CMD [ "python", "/usr/app/api.py" ]