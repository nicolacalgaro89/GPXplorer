# Generated by Django 4.1.3 on 2022-11-04 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GPXManager', '0004_alter_boundstype_maxlat_alter_boundstype_maxlon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gpxtype',
            name='metadata',
        ),
        migrations.RemoveField(
            model_name='gpxtype',
            name='rte',
        ),
        migrations.RemoveField(
            model_name='gpxtype',
            name='trk',
        ),
        migrations.RemoveField(
            model_name='gpxtype',
            name='wpt',
        ),
        migrations.RemoveField(
            model_name='metadatatype',
            name='author',
        ),
        migrations.RemoveField(
            model_name='metadatatype',
            name='bounds',
        ),
        migrations.RemoveField(
            model_name='metadatatype',
            name='copyright',
        ),
        migrations.RemoveField(
            model_name='metadatatype',
            name='link',
        ),
        migrations.RemoveField(
            model_name='persontype',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persontype',
            name='link',
        ),
        migrations.RemoveField(
            model_name='rtetype',
            name='rtept',
        ),
        migrations.RemoveField(
            model_name='trksegtype',
            name='trkpt',
        ),
        migrations.RemoveField(
            model_name='trktype',
            name='trkseg',
        ),
        migrations.AddField(
            model_name='boundstype',
            name='metadata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.metadatatype'),
        ),
        migrations.AddField(
            model_name='copyrighttype',
            name='metadata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.metadatatype'),
        ),
        migrations.AddField(
            model_name='linktype',
            name='metadata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.metadatatype'),
        ),
        migrations.AddField(
            model_name='linktype',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.persontype'),
        ),
        migrations.AddField(
            model_name='metadatatype',
            name='gpx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.gpxtype'),
        ),
        migrations.AddField(
            model_name='persontype',
            name='metadata',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.metadatatype'),
        ),
        migrations.AddField(
            model_name='rtetype',
            name='gpx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.gpxtype'),
        ),
        migrations.AddField(
            model_name='trksegtype',
            name='trk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.trktype'),
        ),
        migrations.AddField(
            model_name='trktype',
            name='gpx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.gpxtype'),
        ),
        migrations.AddField(
            model_name='wpttype',
            name='gpx',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.gpxtype'),
        ),
        migrations.AddField(
            model_name='wpttype',
            name='rte',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.rtetype'),
        ),
        migrations.AddField(
            model_name='wpttype',
            name='trkseg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='GPXManager.trksegtype'),
        ),
    ]
