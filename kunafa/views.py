from django.shortcuts import render
from .models import Kunafa, Baklawa,  Crunchy_kunafa, Topping
from django.views.generic import ListView

#def home(request):
   # Kunafa_list = Kunafa.objects.all()
   # Baklawa_list = Baklawa.objects.all()
   # Crunchy_kunafa_list = Crunchy_kunafa.objects.all()
   # Topping_list = Topping.objects.all()
   # return render(request,'index.html',{'Kunafa_list':Kunafa_list,'Baklawa_list':Baklawa_list,'Crunchy_kunafa_list':Crunchy_kunafa_list,'Topping_list':Topping_list})

def home(request):
	return render(request, 'index.html')

class MenuView(ListView):
    model = Kunafa
    template_name = 'menu.html'
    context_object_name = 'Kunafa'


    def get_context_data(self, **kwargs):
    	# Call the base implementation first to get a context
         context = super(MenuView, self).get_context_data(**kwargs)
         # Add in a QuerySet of all the Baklawa
         context['Baklawa'] = Baklawa.objects.all()
         context['Crunchy_kunafa'] = Crunchy_kunafa.objects.all()
         context['Topping'] = Topping.objects.all()
         return context



def contact(request):
	return render(request, 'contact.html')


def about(request):
	return render(request, 'about.html')


def what(request):
	return render(request, 'what.html')


def menu(request):
	return render(request, 'menu.html')