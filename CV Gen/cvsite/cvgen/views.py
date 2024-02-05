from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.
def accept(request):
    
    if request.method == "POST":
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        address = request.POST.get('address', "")
        about = request.POST.get('about', "")
        college = request.POST.get('college', "")
        degree = request.POST.get('degree', "")
        previous_work = request.POST.get('previous_work', "")
        skills = request.POST.get('skills', "")
        profile = Profile(name=name, email=email, phone=phone, address=address, about=about, college=college, degree=degree, previous_work=previous_work, skills=skills)
        profile.save()
    
    return render(request, 'cvgen/accept.html')

def resume(request, id):
    profile = Profile.objects.get(pk=id)
    
    template = loader.get_template('cvgen/resume.html')
    html = template.render({'profile': profile})
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",   
    }
    pdf = pdfkit.from_string(html, False, options)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename= "resume.pdf"
        
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request, 'cvgen/list.html', {'profiles': profiles})