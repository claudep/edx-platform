# Generated by Django 2.2.12 on 2020-04-22 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSchedule',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField(default=True, help_text='Indicates if this schedule is actively used')),
                ('start_date', models.DateTimeField(db_index=True, default=None, help_text='Date this schedule went into effect', null=True)),
                ('upgrade_deadline', models.DateTimeField(blank=True, db_index=True, help_text='Deadline by which the learner must upgrade to a verified seat', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Schedule',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField(default=True, help_text='Indicates if this schedule is actively used')),
                ('start_date', models.DateTimeField(db_index=True, default=None, help_text='Date this schedule went into effect', null=True)),
                ('upgrade_deadline', models.DateTimeField(blank=True, db_index=True, help_text='Deadline by which the learner must upgrade to a verified seat', null=True)),
            ],
            options={
                'verbose_name_plural': 'Schedules',
                'verbose_name': 'Schedule',
            },
        ),
        migrations.CreateModel(
            name='ScheduleExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_type', models.PositiveSmallIntegerField(choices=[(0, 'Recurring Nudge and Upgrade Reminder'), (1, 'Course Updates')], default=0)),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='schedules.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('create_schedules', models.BooleanField(default=False)),
                ('enqueue_recurring_nudge', models.BooleanField(default=False)),
                ('deliver_recurring_nudge', models.BooleanField(default=False)),
                ('enqueue_upgrade_reminder', models.BooleanField(default=False)),
                ('deliver_upgrade_reminder', models.BooleanField(default=False)),
                ('enqueue_course_update', models.BooleanField(default=False)),
                ('deliver_course_update', models.BooleanField(default=False)),
                ('hold_back_ratio', models.FloatField(default=0)),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'ordering': ('-change_date',),
                'abstract': False,
            },
        ),
    ]
