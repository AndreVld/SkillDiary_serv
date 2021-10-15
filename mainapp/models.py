from django.db import models
from authapp.models import Person


class Profession(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=128, blank=True, null=True)
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
        ('WORK', 'в работе'),
        ('PLAN', 'планируется'),
        ('OVERDUE', 'просрочена'),
        ('COMPLETED', 'завершена'),
    ]
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128, blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,blank=True, null=True

    )
    level = models.CharField(
        max_length=4,
        choices=LEVEL_CHOICES,blank=True, null=True

    )
    rate = models.IntegerField(default=0, blank=True, null=True)
    profession = models.ForeignKey(Profession, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting tasks.'
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('WORK', 'в работе'),
        ('PLAN', 'планируется'),
        ('OVERDUE', 'просрочена'),
        ('COMPLETED', 'завершена'),
    ]
    name = models.CharField(max_length=128)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,

    )
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting tasks.'
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting comments.'
    )

    def __str__(self):
        return self.text


class AdditionalInfo(models.Model):
    TYPE_CHOICES = [
        ('URL', 'Url'),
        ('TEXT', 'Text'),
        ('FILE', 'File'),
    ]
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    type_info = models.CharField(
        max_length=4,
        choices=TYPE_CHOICES,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text='Unselect this instead of deleting element.')


class File(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="files")
    task = models.ForeignKey(Task, on_delete=models.PROTECT, blank=True, null=True)
    additional_info = models.ForeignKey(AdditionalInfo, on_delete=models.PROTECT, blank=True, null=True)

    @property
    def __str__(self):
        return self.name


class HeroText(models.Model):
    TEXT_CHOICES = [
        ('GOOD', 'good'),
        ('BAD', 'bad'),
    ]
    text = models.CharField(max_length=128)
    type_text = models.CharField(
        max_length=4,
        choices=TEXT_CHOICES,
        default='good',
    )

    def __str__(self):
        return self.text


class Hero(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='Hero_images', blank=True)
    is_active = models.BooleanField(
        default=True,
        help_text='Unselect this instead of deleting hero.'
    )

    def __str__(self):
        return self.name