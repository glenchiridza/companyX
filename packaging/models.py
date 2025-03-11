from django.core.validators import MaxValueValidator
from django.db import models

PACKAGE_TYPE = (
    ('LOOSE', 'LOOSE'),
    ('CARTON', 'CARTON'),
)


class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    max_allowed_capacity_in_kgs = models.PositiveIntegerField(default=0)
    current_available_capacity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Warehouse name:: {self.name}'


class QualityMark(models.Model):
    type_of_product = models.CharField(max_length=100, unique=True)
    mass_of_product = models.PositiveIntegerField(default=0)


class Package(models.Model):
    package_type = models.CharField(max_length=100, choices=PACKAGE_TYPE)
    serial_number = models.CharField(max_length=100, unique=True)
    quality_mark = models.ForeignKey(QualityMark, on_delete=models.CASCADE)
    line = models.ForeignKey('Line', on_delete=models.CASCADE, null=True, blank=True)
    pallet = models.ForeignKey('Pallet', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'package serial number:: {self.serial_number}'


class Line(models.Model):
    max_capacity_allowed_in_kgs = models.PositiveIntegerField(default=0)
    number_of_cartons = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    is_special_case = models.BooleanField(default=False)
    max_packages = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(3)])

    def __str__(self):
        return f' line belong to warehouse:: {self.warehouse.name}'


class Pallet(models.Model):
    serial_number = models.CharField(max_length=100)
    capacity_limit_number = models.PositiveIntegerField(default=0)
    current_available_capacity = models.PositiveIntegerField(default=0)
    rack = models.ForeignKey('Rack', on_delete=models.CASCADE)

    def __str__(self):
        return f'Pallet serial:: {self.serial_number}'


class Rack(models.Model):
    name = models.CharField(max_length=20)
    weight_capacity = models.PositiveIntegerField(default=0)
    current_available_capacity = models.PositiveIntegerField(default=0)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
