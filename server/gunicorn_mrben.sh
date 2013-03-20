#!/bin/bash
set -e
LOGFILE=/var/local/sites/mrben.co.uk/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=9
# user/group to run as
USER=webapps
GROUP=webapps
test -d $LOGDIR || mkdir -p $LOGDIR
exec /var/local/sites/.virtualenvs/mrben/bin/python /var/local/sites/.virtualenvs/mrben/bin/gunicorn_django -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug \
  --log-file=$LOGFILE 2>>$LOGFILE