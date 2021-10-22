from django.http import HttpResponse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def index(request):
  driver = webdriver.Chrome(ChromeDriverManager().install())
  driver.get("https://www.mtvema.com/vote/bestk-pop/")
  time.sleep(300)
  return HttpResponse("Hello, world. You're at the polls index.")