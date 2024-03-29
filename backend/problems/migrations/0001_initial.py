# Generated by Django 4.2.7 on 2023-11-14 11:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('statement', models.TextField()),
                ('difficulty', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], default='medium', max_length=10)),
                ('submission_count', models.PositiveIntegerField(default=0)),
                ('input_file', models.FileField(blank=True, null=True, upload_to='problem_inputs/')),
                ('output_file', models.FileField(blank=True, null=True, upload_to='correct_outputs/')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('cpp', 'C++'), ('python', 'Python'), ('javascript', 'JavaScript')], max_length=20)),
                ('code', models.TextField()),
                ('code_file', models.FileField(null=True, upload_to='')),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('verdict', models.CharField(max_length=20)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
