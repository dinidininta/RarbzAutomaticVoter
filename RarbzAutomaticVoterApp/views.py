from django.shortcuts import render
from apscheduler.schedulers.background import BackgroundScheduler

from .voter import Voter

def index(request):
  voter = Voter()
  voter.open_browser()
  scheduler = BackgroundScheduler()
  scheduler.add_job(voter.vote, 'interval', seconds=15)
  scheduler.start()
  increment = voter.get_increment()
  return render(request, "RarbzAutomaticVoterApp/index.html", { 'increment': increment })