from django.db import models
from courseapp.models import Course, AdditionalInfo


class Task(models.Model):
    STATUS_CHOICES = [
        ('WORK', 'в работе'),
        ('PLAN', 'планируется'),
        ('OVERDUE', 'просрочена'),
        ('COMPLETED', 'завершена'),
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
    user = models.ForeignKey('users_app.Person', on_delete=models.PROTECT, related_name='tasks')

    def __str__(self):
        return self.name


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
