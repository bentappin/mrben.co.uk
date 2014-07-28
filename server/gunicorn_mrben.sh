#!/bin/bash
set -e
LOGFILE=/var/local/sites/mrben/logs/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=4
# user/group to run as
USER=web-mrben
GROUP=web-mrben
test -d $LOGDIR || mkdir -p $LOGDIR
cd /var/local/sites/mrben/mrben &&
	/home/web-mrben/.virtualenvs/mrben/bin/python /home/web-mrben/.virtualenvs/mrben/bin/gunicorn_django \
		-w $NUM_WORKERS --user=$USER --group=$GROUP --log-level=debug \
		--log-file=$LOGFILE 2>>$LOGFILE
