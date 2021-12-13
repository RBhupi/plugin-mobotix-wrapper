FROM waggle/plugin-base:1.1.1-base

COPY requirements.txt /app/
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    make \
    g++ \
    vim \
    ffmpeg
COPY app /app/
COPY eventstreamclient /eventstreamclient/
RUN /usr/bin/make -C /eventstreamclient/samples/thermal-raw

#WORKDIR /
#ENTRYPOINT ["python3", "/app/app.py"]

ENTRYPOINT ["/bin/bash"]
