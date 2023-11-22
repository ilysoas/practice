from django.db import models

class RunString(models.Model):
    title = models.CharField(max_length=100, verbose_name='Enter your title')
    description = models.TextField(verbose_name='Enter your description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Бегущую строку'
        verbose_name_plural = 'Бегущие строки'

class Manga(models.Model):
    CHOICE_STATUS = (
        ('ВЫПУСКАЕТСЯ', 'ВЫПУСКАЕТСЯ'),
        ('ЗАВЕРШЁН', 'ЗАВЕРШЁН')
    )
    image = models.ImageField(upload_to='manga/')
    title = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=30, choices=CHOICE_STATUS)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

class Afisha(models.Model):
    title_manga = models.CharField(max_length=100)
    chapter = models.CharField(max_length=20, null=True)
    update_data = models.DateField()

    def __str__(self):
        return self.title_manga

class Slider(models.Model):
    photo = models.URLField()

    def __str__(self):
        return self.photo