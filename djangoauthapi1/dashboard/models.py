from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

class TestSuite(models.Model):
    PROTOCOL_CHOICES = [
        ('SMB', 'SMB'),
        ('P1', 'P1'),
        ('P2', 'P2'),
        ('P3', 'P3'),
        ('P4', 'P4'),
    ]

    LOG_LEVEL_CHOICES = [
        ('Debug', 'Debug'),
        ('Warning', 'Warning'),
        ('Critical', 'Critical'),
        ('Info', 'Info'),
    ]
    
    YES_NO_CHOICES = [
        (True, 'YES'),
        (False, 'NO'),
    ]


    protocol = models.CharField(max_length=50, choices=PROTOCOL_CHOICES)
    host_ip_address = models.GenericIPAddressField()
    share = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z0-9]*$',
                                                                      message='Share must contain only alphanumeric characters')])
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[\w.@+-]+$',
                                                                          message='Invalid password format')])
    log_level = models.CharField(max_length=50, choices=LOG_LEVEL_CHOICES)
    sign = models.BooleanField(default=True, choices=YES_NO_CHOICES)
    encrypt = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    trace = models.BooleanField(default=False, choices=YES_NO_CHOICES)
    min_dialect = models.IntegerField(validators=[MinValueValidator(0)])
    max_dialect = models.IntegerField(validators=[MaxValueValidator(1000)])

    def __str__(self):
        return f"{self.protocol} - {self.host_ip_address} - {self.share} - {self.user_name}"





class OperatingSystem(models.Model):
    OS_CHOICES = [
        ('centos', 'CentOS'),
        ('windows', 'Windows'),
        ('ubuntu', 'Ubuntu'),
    ]
    
    name = models.CharField(max_length=20, choices=OS_CHOICES)

    def __str__(self):
        return self.name


class TestSuiteName(models.Model):
    name = models.CharField(max_length=200)
    operating_system = models.ForeignKey(OperatingSystem, on_delete=models.CASCADE)
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, help_text="Enter folder location")
    # Remove the user_name and password fields here

    def __str__(self):
        return self.name
