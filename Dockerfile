FROM python:3.8

ENV PORT 5000
ENV HOST 0.0.0.0
ENV DEBUG True
ENV USER fibo
ENV HOME /home/${USER}
WORKDIR ${HOME}

COPY ./requirements.txt ${HOME}/requirements.txt

RUN pip install -r requirements.txt

COPY apps ${HOME}/apps
COPY main.py ${HOME}

ENTRYPOINT [ "gunicorn" ]
CMD [ "main:app" ]
