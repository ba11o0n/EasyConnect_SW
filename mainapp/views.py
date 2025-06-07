from django.shortcuts import render
from mainapp.decorators import role_required
from core.mqtt_client import latest_message

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

def ticket_dashboard(request):
    msg = latest_message.get("easyconnect/ticket", "No ticket data")
    return render(request, "mainapp/dashboard.html", {"ticket_info": msg})