# Generated by Django 4.0.1 on 2022-04-16 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_social_webiste_profile_social_website'),
        ('projects', '0004_project_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
