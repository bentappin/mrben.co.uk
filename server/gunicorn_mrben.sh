#!/bin/bash
set -e
LOGFILE=/var/local/sites/mrben/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=4
USER=web-mrben
GROUP=web-mrben
ADDRESS=127.0.0.1:8000
test -d $LOGDIR || mkdir -p $LOGDIR
cd /var/local/sites/mrben && \
  source /home/web-mrben/.virtualenvs/mrben/bin/activate &&
  /home/web-mrben/.virtualenvs/mrben/bin/gunicorn \
  -b $ADDRESS -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE \
  mrben.wsgi:application \
  2>>$LOGFILE