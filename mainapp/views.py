from django.shortcuts import render
from mainapp.decorators import role_required

def home(request):
    return render(request, 'main/index.html')

@role_required('admin')
def admin(request):
    return render(request, 'main/admin.html')

@role_required('vendor')
def vendor(request):
    return render(request, 'main/vendor.html')

@role_required('attendee')
def attendee(request):
    return render(request, 'main/attendee.html')
