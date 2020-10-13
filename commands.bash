#!/bin/bash
source env/bin/activate
gunicorn -w 1 -k eventlet -b 0.0.0.0:8000 -t 60 --limit-request-line 8190 deploy:app
