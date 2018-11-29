from django.db import models
from django.contrib.auth.models import User

class Machine(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    current_machine = models.CharField(max_length=100)
    current_operation = models.CharField(max_length=100)
    # previous_operations =
    MACHINE_STATUS = (
        ('INACTIVE', 'Inactive'),
        ('ACTIVE', 'Active'),
        # ('L', 'Large'),
    )
    status = models.CharField(max_length=10, choices=MACHINE_STATUS)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Machines"

    def __str__(self):
        return self.name

class Operation(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    # component = models.OneToOneField(Component, on_delete=models.CASCADE, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    MACHINE_STATUS = (
        ('INACTIVE', 'Inactive'),
        ('ACTIVE', 'Active'),
        # ('L', 'Large'),
    )
    status = models.CharField(max_length=10, choices=MACHINE_STATUS)

    class Meta:
        verbose_name_plural = "Operations"


class Component(models.Model):
    machine = models.ForeignKey(Machine, related_name="machine_operation", on_delete=models.CASCADE )
    operation = models.ForeignKey(Operation, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Components"


    def __str__(self):
        return self.name


class Stats(models.Model):
    machine = models.ForeignKey(Machine,null=True, blank=True, on_delete=models.CASCADE)
    component= models.ForeignKey(Component,null=True, blank=True, on_delete=models.CASCADE)
    operation = models.ForeignKey(Operation,null=True, blank=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    TEMPRATURE = 'temperature'
    PRESSURE = 'pressure'
    TYPE_CHOICES = (
        (TEMPRATURE,'temperature'),
        (PRESSURE,'pressure'),
    )
    type = models.CharField(choices=TYPE_CHOICES,max_length=20)
    value = models.IntegerField()

    class Meta:
        # managed = False
        verbose_name_plural = "Stats"
        # db_table = 'fixture_stats'


