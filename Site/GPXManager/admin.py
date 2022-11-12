from django.contrib import admin

# Register your models here.
from .models import wptType
from .models import trksegType
from .models import trkType
from .models import gpxType

admin.site.register(wptType)
admin.site.register(trksegType)
admin.site.register(trkType)
admin.site.register(gpxType)
