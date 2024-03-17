from django.contrib import admin

from service_app import models

admin.site.register(models.Login_view)

admin.site.register(models.Customer)