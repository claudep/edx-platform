# Generated by Django 2.2.12 on 2020-04-22 13:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course_overviews', '0020_courseoverviewtab_url_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEntitlement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('course_uuid', models.UUIDField(help_text='UUID for the Course, not the Course Run')),
                ('expired_at', models.DateTimeField(blank=True, help_text='The date that an entitlement expired, if NULL the entitlement has not expired.', null=True)),
                ('mode', models.CharField(help_text='The mode of the Course that will be applied on enroll.', max_length=100)),
                ('order_number', models.CharField(default=None, max_length=128, null=True)),
                ('refund_locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEntitlementPolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expiration_period', models.DurationField(default=datetime.timedelta(730), help_text='Duration in days from when an entitlement is created until when it is expired.')),
                ('refund_period', models.DurationField(default=datetime.timedelta(60), help_text='Duration in days from when an entitlement is created until when it is no longer refundable')),
                ('regain_period', models.DurationField(default=datetime.timedelta(14), help_text='Duration in days from when an entitlement is redeemed for a course run until it is no longer able to be regained by a user.')),
                ('mode', models.CharField(choices=[(None, '---------'), ('verified', 'verified'), ('professional', 'professional')], max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseEntitlementSupportDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('reason', models.CharField(choices=[('LEAVE', 'Learner requested leave session for expired entitlement'), ('CHANGE', 'Learner requested session change for expired entitlement'), ('LEARNER_NEW', 'Learner requested new entitlement'), ('COURSE_TEAM_NEW', 'Course team requested entitlement for learnerg'), ('OTHER', 'Other')], max_length=15)),
                ('action', models.CharField(choices=[('REISSUE', 'Re-issue entitlement'), ('CREATE', 'Create new entitlement')], max_length=15)),
                ('comments', models.TextField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalCourseEntitlementSupportDetail',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('reason', models.CharField(choices=[('LEAVE', 'Learner requested leave session for expired entitlement'), ('CHANGE', 'Learner requested session change for expired entitlement'), ('LEARNER_NEW', 'Learner requested new entitlement'), ('COURSE_TEAM_NEW', 'Course team requested entitlement for learnerg'), ('OTHER', 'Other')], max_length=15)),
                ('action', models.CharField(choices=[('REISSUE', 'Re-issue entitlement'), ('CREATE', 'Create new entitlement')], max_length=15)),
                ('comments', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('entitlement', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='entitlements.CourseEntitlement')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('support_user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('unenrolled_run', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='course_overviews.CourseOverview')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical course entitlement support detail',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCourseEntitlement',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('course_uuid', models.UUIDField(help_text='UUID for the Course, not the Course Run')),
                ('expired_at', models.DateTimeField(blank=True, help_text='The date that an entitlement expired, if NULL the entitlement has not expired.', null=True)),
                ('mode', models.CharField(help_text='The mode of the Course that will be applied on enroll.', max_length=100)),
                ('order_number', models.CharField(default=None, max_length=128, null=True)),
                ('refund_locked', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('_policy', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='entitlements.CourseEntitlementPolicy')),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical course entitlement',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
