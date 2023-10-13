from django.views.generic import TemplateView

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'
    
class MenuView(TemplateView):
    template_name = 'menu.html'
    
class AboutUs(TemplateView):
    template_name = 'about.html'
    
    
class ContactView(TemplateView):
    template_name = 'contact.html'