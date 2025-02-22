from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from .form import JoinForm
from .models import Participant


def home(request):
    return render(request, "myapp/home.html")
def competitions(request):
    return render(request, "myapp/competitions.html")
def contactus(request):
    return render(request, "myapp/contactus.html")

def aboutus(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            # Create a new Participant instance and save it to the database
            participant = Participant(
                full_name=form.cleaned_data['full_name'],
                age=form.cleaned_data['age'],
                city=form.cleaned_data['city'],
                school_name=form.cleaned_data['school_name'],
                category=form.cleaned_data['category']
            )
            participant.save()  # Save the participant to the database
            
            # Redirect to a success page or display a success message
            return redirect('aboutus')  # Adjust this to your actual success view/template
    else:
        form = JoinForm()

    return render(request, 'myapp/aboutus.html', {'form': form})
    
def contactus(request):
    return render(request, "myapp/contactus.html")
    