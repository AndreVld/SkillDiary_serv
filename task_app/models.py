from datetime import date

from django.db import models
from courseapp.models import Course, AdditionalInfo
from users_app.models import Person


class Task(models.Model):
    STATUS_CHOICES = [
        ('WORK', 'В работе'),
        ('PLAN', 'Планируется'),
        ('OVERDUE', 'Просрочена'),
        ('COMPLETED', 'Завершена'),
    ]
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='WORK'
    )
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting tasks.'
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='tasks')
    user = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='tasks')

    def __str__(self):
        return self.name

    def check_status(self):
        today = date.today()

        if self.status == 'WORK' and today > self.end_date:
            self.status = 'OVERDUE'
            self.save()

        elif self.status == 'PLAN' and today >= self.start_date:
            self.status = 'WORK'
            self.save()


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.PROTECT, related_name="comments")
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting comments.'
    )

    def __str__(self):
        return self.text


class File(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="files")
    task = models.ForeignKey(Task, on_delete=models.PROTECT, blank=True, null=True, related_name='files')
    additional_info = models.ForeignKey(AdditionalInfo, on_delete=models.PROTECT, blank=True, null=True,
                                        related_name='files')

    def __str__(self):
        return self.name
