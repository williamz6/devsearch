# Generated by Django 4.0.1 on 2022-05-01 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_vote_ratio_alter_project_vote_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200),
        ),
    ]