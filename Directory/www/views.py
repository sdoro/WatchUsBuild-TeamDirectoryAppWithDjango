from django.shortcuts import render
from www.models import Person

# Create your views here.
def index(request):
    people = Person.objects.all()
    return render(request, 'index.html', {'people': people})
