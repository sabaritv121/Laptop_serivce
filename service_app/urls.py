from django.urls import path

from service_app import views, admin_views, customer_views

urlpatterns = [
 # path("",views.test,name="test"),
 # path("",views.landing_page,name="landing"),

 path('',views.RegistrationView.as_view()),
 path('login_view', views.login_page, name="login_view"),
 path("admin_dashboard",views.admin_dashboard,name='admin_dashboard'),
 path("customer_dashboard", views.customer_dashboard, name='customer_dashboard'),
 path("seller_dashboard", views.seller_dashboard, name='seller_dashboard'),
 path("manager_dashboard", views.manager_dashboard, name='manager_dashboard'),

#admin
 path("new",views.new,name="new"),
 path('schedule',admin_views.schedule_add,name='schedule'),
 path('schedule_view', admin_views.schedule, name='schedule_view'),
 path('schedule_delete/<int:id>/', admin_views.schedule_delete, name='schedule_delete'),

 path('appointment_admin',admin_views.appointment_admin,name='appointment_admin'),
 path('approve_appointment/<int:id>/', admin_views.approve_appointment, name='approve_appointment'),
 path('reject_appointment/<int:id>/', admin_views.reject_appointment, name='reject_appointment'),


 #customer
 path("schedule_cus",customer_views.schedule_cus,name="schedule_cus"),
 path('take_appointment/<int:id>/', customer_views.take_appointment, name='take_appointment'),
 path('appointments', customer_views.appointments, name='appointments'),

]