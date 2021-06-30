from portfolio.models import Projects
from django.contrib import admin
from .models import Projects
from .models import Aboutpage

# Register your models here.
admin.site.register(Projects)
admin.site.register(Aboutpage)
