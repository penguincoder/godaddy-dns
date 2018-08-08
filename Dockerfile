FROM frolvlad/alpine-python3
MAINTAINER Andrew Coleman <penguincoder@gmail.com>

RUN pip install --upgrade pif godaddypy
ADD update_penguincoder.org.py /
CMD [ "python3", "update_penguincoder.org.py" ]
