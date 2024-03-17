from django.contrib import messages
from django.shortcuts import render, redirect

from service_app.models import AppointmentSchedule, Customer, Appointment


def schedule_cus(request):
    s = AppointmentSchedule.objects.all()

    context = {
        'schedule': s,

    }
    return render(request, 'customer/cus_schedule.html', context)


def take_appointment(request, id):
    schedule = AppointmentSchedule.objects.get(id=id)
    u = Customer.objects.get(user=request.user)
    appointment = Appointment.objects.filter(user=u , schedule=schedule)
    if appointment.exists():
        messages.info(request, 'You Have Already Requested Appointment for this Schedule')
        return redirect("schedule_cus")
    else:
        if request.method == 'POST':
            obj = Appointment()
            obj.user = u
            obj.schedule = schedule
            obj.save()
            messages.info(request, 'Appointment Booked Successfully')
            return redirect('appointments')
    return render(request, 'customer/take_appointment.html', {'schedule': schedule})



def appointments(request):
    u = Customer.objects.get(user=request.user)
    a = Appointment.objects.filter(user=u)
    return render(request, 'customer/cus_appointment.html', {'appointment': a})


