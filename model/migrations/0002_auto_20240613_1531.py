# Generated by Django 3.2.23 on 2024-06-13 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classificationresult',
            name='musim',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='penyakit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='prediction',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='rasa',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='teknik',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='varietas',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='classificationresult',
            name='warna',
            field=models.FloatField(),
        ),
    ]
