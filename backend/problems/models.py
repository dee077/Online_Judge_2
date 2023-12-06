from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Problem(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=255)
    statement = models.TextField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')
    submission_count = models.PositiveIntegerField(default=0)
    input_file = models.FileField(upload_to='problem_inputs/', null=True, blank=True)
    output_file = models.FileField(upload_to='correct_outputs/', null=True, blank=True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    LANGUAGE_CHOICES = [
        ('cpp', 'C++'),
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    code_text = models.TextField(null=True, blank=True)
    code_file = models.FileField(null=True)
    submission_time = models.DateTimeField(auto_now_add=True)
    time_taken = models.FloatField(null=True, blank=True)
    memory_used = models.FloatField(null=True, blank=True)
    verdict = models.CharField(max_length=20)

    def validate_code_fields(self):
        if not self.code and not self.code_file:
            raise ValidationError("Either 'code_text' or 'code_file' must be provided.")

    def clean(self):
        self.validate_code_fields()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.user.username}'s submission for {self.problem.title}"
