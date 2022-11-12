from multiprocessing import AuthenticationError
from django.db import models

class gpxType(models.Model):
    version = models.CharField(max_length=10, null=True, blank=True)
    creator = models.CharField(max_length=200, null=True, blank=True)

class metadataType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(null=True, blank=True)
    keywords = models.CharField(max_length=200, null=True, blank=True)
    gpx = models.ForeignKey(gpxType, on_delete=models.CASCADE, null=True, blank=True)

class boundsType(models.Model):
    minlat = models.FloatField(null=True, blank=True)
    minlon = models.FloatField(null=True, blank=True)
    maxlat = models.FloatField(null=True, blank=True)
    maxlon = models.FloatField(null=True, blank=True)
    metadata = models.ForeignKey(metadataType, on_delete=models.CASCADE, null=True, blank=True)

class personType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    metadata = models.ForeignKey(metadataType, on_delete=models.CASCADE, null=True, blank=True)

class linkType(models.Model):
    href = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    person = models.ForeignKey(personType, on_delete=models.CASCADE, null=True, blank=True)
    metadata = models.ForeignKey(metadataType, on_delete=models.CASCADE, null=True, blank=True)

class copyrightType(models.Model):
    author = models.CharField(max_length=50, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    licence = models.URLField(null=True, blank=True)
    metadata = models.ForeignKey(metadataType, on_delete=models.CASCADE, null=True, blank=True)
   
class mailType(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    domain = models.CharField(max_length=50, null=True, blank=True)

class trkType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    cmt = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    src = models.CharField(max_length=200, null=True, blank=True)
    link = models.ForeignKey(linkType, on_delete=models.CASCADE, null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True) 
    type = models.CharField(max_length=200, null=True, blank=True)
    gpx = models.ForeignKey(gpxType, on_delete=models.CASCADE, null=True, blank=True)

class trksegType(models.Model):
    trk =  models.ForeignKey(trkType, on_delete=models.CASCADE, null=True, blank=True)

class rteType(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    cmt = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    src = models.CharField(max_length=200, null=True, blank=True)
    link = models.ForeignKey(linkType, on_delete=models.CASCADE, null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True) 
    type = models.CharField(max_length=200, null=True, blank=True)
    gpx = models.ForeignKey(gpxType, on_delete=models.CASCADE, null=True, blank=True)

class wptType(models.Model):
    lat=models.FloatField()
    lon=models.FloatField()
    ele=models.FloatField(null=True, blank=True)
    time=models.DateTimeField(null=True, blank=True)
    magvar=models.FloatField(null=True, blank=True)
    geoidheight=models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    cmt = models.CharField(max_length=200, null=True, blank=True)
    desc = models.CharField(max_length=200, null=True, blank=True)
    src = models.CharField(max_length=200, null=True, blank=True)
    link = models.ForeignKey(linkType, on_delete=models.CASCADE, null=True, blank=True)
    sym = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, null=True, blank=True)
    fix = models.CharField(max_length=200, null=True, blank=True)
    sat = models.PositiveIntegerField(null=True, blank=True) 
    hdop = models.FloatField(null=True, blank=True)
    vdop = models.FloatField(null=True, blank=True)
    pdop = models.FloatField(null=True, blank=True)
    ageofdgpsdata = models.FloatField(null=True, blank=True)
    dgpsid = models.IntegerField(null=True, blank=True)
    gpx =  models.ForeignKey(gpxType, on_delete=models.CASCADE, null=True, blank=True)
    rte =  models.ForeignKey(rteType, on_delete=models.CASCADE, null=True, blank=True)
    trkseg =  models.ForeignKey(trksegType, on_delete=models.CASCADE, null=True, blank=True)









