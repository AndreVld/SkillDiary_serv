from django.db import models
from users_app.models import Person


class Profession(models.Model):
    name = models.CharField(max_length=128, unique=True)
    # description = models.CharField(max_length=128, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting tasks.'
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ('1', 'Низкий'),
        ('2', 'Средний'),
        ('3', 'Высокий'),
    ]
    STATUS_CHOICES = [
        ('WORK', 'В работе'),
        ('PLAN', 'Планируется'),
        ('OVERDUE', 'Пройден не доконца'),
        ('COMPLETED', 'Завершен'),
    ]
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True)
    target = models.CharField(max_length=255, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='PLAN'
    )
    level = models.CharField(
        max_length=4,
        choices=LEVEL_CHOICES,
        default='1'
    )
    rate = models.IntegerField(default=0)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT, related_name='courses')
    add_report = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='courses')
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting tasks.'
    )

    def __str__(self):
        return self.name


class AdditionalInfo(models.Model):
    TYPE_CHOICES = [
        ('URL', 'Ссылка'),
        ('TEXT', 'Заметка'),
        ('FILE', 'Файл'),
    ]
    name = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    note = models.CharField(max_length=256, blank=True)
    type_info = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
        default='URL'
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, related_name='addinfo')
    is_active = models.BooleanField(default=True, help_text='Unselect this instead of deleting element.')
