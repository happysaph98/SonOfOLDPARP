main: gunicorn -b 0.0.0.0:8000 -k gevent -w 3 main:app
<<<<<<< HEAD
chat: gunicorn -b 0.0.0.0:8000 -k gevent -w 3 chat:app
main-debug: gunicorn --debug --log-level=debug -b 0.0.0.0:8000 -k gevent -w 1 main:app
chat-debug: gunicorn --debug --log-level=debug -b 0.0.0.0:8000 -k gevent -w 1 chat:app
archiver: python archiver.py
matchmaker: python matchmaker.py
reaper: python reaper.py
initdb: python initdb.py
=======
main-debug: gunicorn --debug --log-level=debug -b 0.0.0.0:8000 -k gevent -w 1 main:app
archiver: python archiver.py
initdb: python initdb.py
exporter: python exporter.py
>>>>>>> 68ff6b3af88cb4d1d46a949b61b7e3086f286404
