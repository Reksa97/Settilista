FROM ubuntu:16.04 

WORKDIR /project
COPY . .
EXPOSE 5000
RUN apt update && apt install -y python3-pip
RUN pip3 install -r requirements.txt
CMD python3 run.py
