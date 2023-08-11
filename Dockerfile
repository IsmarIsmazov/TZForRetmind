FROM python:latest
LABEL authors="ismarhahazov"
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
WORKDIR /TZForRetmind
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r /TZForRetmind/requirements.txt
ADD . .