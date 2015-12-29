from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.utils import timezone
import datetime


class Student(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=15, blank=True, null=True)
    homeroom = models.CharField(max_length=20, blank=True, null=True)
    adults = ArrayField(models.CharField(max_length=250), blank=True, null=True)

    enrolled = models.BooleanField(default=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True, null=True)

    def is_enrolled(self):
        return self.enrolled

    def enrolled_this_year(self):
        return self.add_date.year == datetime.datetime.now().year

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=250)
    percentage = models.DecimalField(max_digits=4, decimal_places=3, null=True)
    amounts = ArrayField(models.DecimalField(max_digits=20, decimal_places=2),
                                             blank=True, null=True)
    enrolled = models.BooleanField(default=True, blank=True)
    add_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True, null=True)

    def is_enrolled(self):
        return self.enrolled

    def enrolled_this_year(self):
        return self.add_date.year == datetime.datetime.now().year

    def __str__(self):
        return self.name


class Purchase(models.Model):
    student = models.ForeignKey(Student, on_delete=models.SET_NULL,
                                blank=True, null=True)
    business = models.ForeignKey(Business, on_delete=models.SET_NULL,
                                blank=True, null=True)
    purchase_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now=True, null=True)

    amount = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    student_earned = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    school_earned = models.DecimalField(max_digits=20, decimal_places=2, null=True)


    def purchased_this_year(self):
        return self.purchase_date.year == datetime.datetime.now().year

    def __str__(self):
        return '{} with {}'.format(self.student, self.business)
