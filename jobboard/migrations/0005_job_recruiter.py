# Generated by Django 3.2.9 on 2021-11-28 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0001_initial'),
        ('jobboard', '0004_alter_job_work_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='recruiter',
            field=models.ForeignKey(default='<django.db.models.fields.related.ForeignKey>',
                                    on_delete=django.db.models.deletion.PROTECT, to='recruiter.recruiter'),
        ),
    ]