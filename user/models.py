from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE'),
)

TITLES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Mx', 'Mx'),
    ('Sir', 'Sir'),
    ('Dr', 'Dr'),
    ('Cllr', 'Cllr'),
    ('Lady', 'Lady'),
    ('Lord', 'Lord'),

)


class User(AbstractUser):
    title = models.CharField(max_length=5,choices=TITLES)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=40)
    other_names = models.CharField(max_length=140,null=True, blank=True)
    gender = models.CharField(max_length=10,choices=GENDER)
    is_logistics_manager = models.BooleanField(default=False)
    is_system_operator = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Operator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=20)
    branch_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class LogisticsManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=20)
    branch_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} -- {self.user.last_name}"
