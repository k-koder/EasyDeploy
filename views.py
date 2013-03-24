# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from cxlsite.login.models import Author

def login(request):
        return render_to_response('login.html')
        
def index(request):
        username=request.POST.get('usern')
        password=request.POST.get('passw')
        db=Author.objects.filter(usern=username).values()
        if db is not None:
                if password==db[0].get('passw'):
                        return render_to_response('login_s.html')
                else:
                        return render_to_response('login_w.html')
        else:
                return render_to_response('login_w.html')
        
       # user=authenticate(usern=username,passw=password)
        #if user is not None:
        #        return render_to_response('login_s.html')    
        #else:   
          #      return render_to_response('login_w.html')

               