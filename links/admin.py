from django.contrib import admin
from links.models import Link
from django.contrib.auth.models import Group

admin.site.register(Link)

admin.site.unregister(Group)
# Register your models here.

admin.site.site_header = "Student Id: I4G029095NHE"