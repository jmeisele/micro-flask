FROM python:alpine3.7 
RUN mkdir /python-factory-service
COPY . /python-factory-service
WORKDIR /python-factory-service
RUN pip install -r requirements.txt 
# EXPOSE 3001
ENTRYPOINT [ "python" ] 
CMD [ "main.py" ]  