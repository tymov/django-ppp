from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
from .models import Link

def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', 'https://www.espn.com/nba/scoreboard')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
    
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            
            # Add error handling for None values
            if link_address is not None and link_text is not None:
                Link.objects.create(address=link_address, name=link_text)
                
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
 
    return render(request, 'webscraper/scrape.html', {'data': data})
 
def clear(request):
    Link.objects.all().delete()
    return render(request, 'webscraper/scrape.html')
