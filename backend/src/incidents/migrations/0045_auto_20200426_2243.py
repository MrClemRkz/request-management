# Generated by Django 2.2.12 on 2020-04-26 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('incidents', '0044_auto_20200425_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestInformationWorkflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('is_advice_provided', models.BooleanField(default=False)),
                ('actioned_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_requestinformationworkflow_related', related_query_name='incidents_requestinformationworkflows', to=settings.AUTH_USER_MODEL)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='incidents_requestinformationworkflow_related', related_query_name='incidents_requestinformationworkflows', to='incidents.Incident')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='incidentstatus',
            name='current_status',
            field=models.CharField(choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('ADVICE_PROVIDED', 'Advice Provided'), ('INFORMATION_REQESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50),
        ),
        migrations.AlterField(
            model_name='incidentstatus',
            name='previous_status',
            field=models.CharField(blank=True, choices=[('NEW', 'New'), ('CLOSED', 'Closed'), ('ACTION_TAKEN', 'Action Taken'), ('ACTION_PENDING', 'Action Pending'), ('ADVICE_PROVIDED', 'Advice Provided'), ('INFORMATION_REQESTED', 'Information Requested'), ('VERIFIED', 'Verified'), ('INVALIDATED', 'Invalidated'), ('REOPENED', 'Reopened')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='provideadviceworkflow',
            name='initiated_workflow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='incidents.RequestInformationWorkflow'),
        ),
        migrations.DeleteModel(
            name='RequestAdviceWorkflow',
        ),
    ]
