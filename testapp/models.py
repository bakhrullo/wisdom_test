from django.db import models
from django.contrib.auth.models import AbstractUser


class Grade(models.Model):
    grade = models.CharField(max_length=20, unique=True, verbose_name='Класс')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')

    def __str__(self):
        return self.grade

    class Meta:
        verbose_name = "Классы"
        verbose_name_plural = "Классы"


class NewUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Ученик'),
        (2, 'Учитель'),
        (3, 'Родитель'),
        (4, 'Директор'),
        (5, 'Секретарь'),
        (6, 'Продавец'),
    )

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    father_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    is_active = models.BooleanField(default=True, verbose_name='Является активным')
    role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, verbose_name='Роль')
    balance = models.PositiveBigIntegerField(default=0, blank=True, verbose_name="Баланс")

    def __str__(self):
        return self.username

    class Meta:
        abstract = True


class Pupil(NewUser):
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Ученики"
        verbose_name_plural = "Ученики"


class Parent(NewUser):
    pupil = models.ManyToManyField(Pupil)

    class Meta:
        verbose_name = "Родители"
        verbose_name_plural = "Родители"


class Teacher(NewUser):
    grade = models.ManyToManyField(Grade)

    class Meta:
        verbose_name = "Учителя"
        verbose_name_plural = "Учителя"


class Staff(NewUser):
    pass

    class Meta:
        verbose_name = "Персонал"
        verbose_name_plural = "Персонал"


class Clerk(NewUser):
    pass

    class Meta:
        verbose_name = "Секретарь"
        verbose_name_plural = "Секретарь"


class Seller(NewUser):
    pass

    class Meta:
        verbose_name = "Продавцы"
        verbose_name_plural = "Продавцы"
