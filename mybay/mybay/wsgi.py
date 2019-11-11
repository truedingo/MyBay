"""
WSGI config for mybay project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from apscheduler.schedulers.background import BackgroundScheduler as Scheduler
from django.core.mail import send_mail
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import logging
import sys
from mybay_app.models import Item

sys.path.append('mybay_app')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mybay.settings")
application = get_wsgi_application()

#Start Log
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

# Start the scheduler
sched = Scheduler()
sched.start()

# Define the function that is to be executed
def mailing_service():
    users = User.objects.all()
    items = Item.objects.all().order_by('-item_date')
    today = datetime.today()
    emails = list()
    itemtosend = 'Our most recent items:\n'
    for user in users:
        emails.append(user.username)
    count = 1
    for item in items:
        if count == 4:
            break
        itemtosend = itemtosend + str(count) + ':' + str(item) + '\n'
        count = count + 1
    if emails:
        send_mail('Our most recent items',
                  itemtosend,
                  'arturgcoutinho@gmail.com',
                  emails)
    run_day = today + timedelta(days=1)
    sched.add_job(mailing_service, next_run_time=run_day)

today = datetime.today() + timedelta(0, 30)
sched.add_job(mailing_service, next_run_time=today)
