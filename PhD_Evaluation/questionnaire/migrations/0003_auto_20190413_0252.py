# Generated by Django 2.1.7 on 2019-04-13 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_auto_20190413_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='Current_Academic_Advisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='academic_advisor', to='registration.professorName'),
        ),
    ]