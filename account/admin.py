from django.contrib import admin
from account.models import Contact, CustomUser


admin.site.register(CustomUser)
admin.site.register(Contact)