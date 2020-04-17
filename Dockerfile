FROM nvcr.io/nvidia/pytorch:19.07-py3

RUN mkdir -p /src

WORKDIR /src




ADD requirements.txt /src


RUN pip install -r requirements.txt


ENV NAME Generation1

CMD [ "python", "/src/train.py" ]
