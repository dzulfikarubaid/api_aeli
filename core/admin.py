from django.contrib.admin import site
from .models import Dpd, Dpp

site.register([Dpd, Dpp])