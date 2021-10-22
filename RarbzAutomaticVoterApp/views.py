from django.http import HttpResponse
from apscheduler.schedulers.background import BackgroundScheduler

from .voter import Voter

def index(request):
  voter = Voter()
  voter.open_browser()
  scheduler = BackgroundScheduler()
  scheduler.add_job(voter.vote, 'interval', seconds=11)
  scheduler.start()
  return HttpResponse("Hello, world. You're at the polls index.")