#!/bin/bash

zip -r update.zip mysite/ manage.py requirements.txt
scp update.zip masteralish@masteralish.myjino.ru:django/net/
rm update.zip
ssh masteralish@masteralish.myjino.ru << END
    cd django/net
    unzip -uo update.zip
    rm update.zip
    if [ -f mysite/local_settings.py ]; then
        rm mysite/local_settings.py
    fi
    mv mysite/jino_settings.py mysite/local_settings.py
    source env/bin/activate
    pip install -r requirements.txt
    python manage.py migrate --noinput
    python manage.py collectstatic --noinput
END
