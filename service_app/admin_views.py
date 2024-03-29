from django.contrib import messages
from django.shortcuts import redirect,render

from service_app.forms import ScheduleAdd
from service_app.models import AppointmentSchedule, Appointment, Sales_add


def schedule_add(request):
    form = ScheduleAdd()
    if request.method == 'POST':
        form = ScheduleAdd(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, ' Schedule Added Successfully')
            return redirect('schedule_view')
    else:
        form = ScheduleAdd()
    return render(request, 'admin/schedule_add.html', {'form': form})



def schedule(request):
    n = AppointmentSchedule.objects.all()

    context = {
        'schedule': n,

    }
    return render(request, 'admin/schedule_view.html', context)


def schedule_delete(request, id):
    n = AppointmentSchedule.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, 'Schedule Deleted Successfully')
        return redirect('schedule_view')




def appointment_admin(request):
    p = Appointment.objects.all()

    context = {
        'appointment': p,

    }
    return render(request, 'admin/appointment.html', context)


def approve_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 1
    n.save()
    messages.info(request, 'Appointment  Confirmed')
    return redirect('appointment_admin')


def reject_appointment(request, id):
    n = Appointment.objects.get(id=id)
    n.status = 2
    n.save()
    messages.info(request, 'Appointment Rejected')
    return redirect('appointment_admin')


def adm_view_items(request):

    data=Sales_add.objects.all()

    return render(request,'customer/cus_items.html',{'data':data})