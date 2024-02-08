from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


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

    protocol = models.CharField(max_length=50, choices=PROTOCOL_CHOICES, verbose_name=_("Protocol"))
    host_ip_address = models.GenericIPAddressField(verbose_name=_("Host IP Address"))
    share = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z0-9]*$', message='Share must contain only alphanumeric characters')], verbose_name=_("Share Name"))
    user_name = models.CharField(max_length=50, verbose_name=_("User Name"))
    password = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[\w.@+-]+$', message='Invalid password format')], verbose_name=_("Password"))
    log_level = models.CharField(max_length=50, choices=LOG_LEVEL_CHOICES, verbose_name=_("Log Level"))
    sign = models.BooleanField(default=True, choices=YES_NO_CHOICES, verbose_name=_("Sign"))
    encrypt = models.BooleanField(default=False, choices=YES_NO_CHOICES, verbose_name=_("Encrypt"))
    trace = models.BooleanField(default=False, choices=YES_NO_CHOICES, verbose_name=_("Trace"))
    dialect_regex = r'^[A-Za-z]+_[A-Za-z0-9_]+$'
    dialect_validator = RegexValidator(regex=dialect_regex,message=_("Dialect should be in the format 'DIALECT_SMB3_1_1'"),)
    min_dialect = models.CharField(max_length=255,validators=[dialect_validator],default='DIALECT_SMB3_1_1',  verbose_name=_("Min Dialect"), )
    max_dialect = models.CharField( max_length=255, validators=[dialect_validator],default='DIALECT_SMB2_002',  verbose_name=_("Max Dialect"),)

    def __str__(self):
        return f"{self.protocol} - {self.host_ip_address} - {self.share} - {self.user_name}"




class TestSuiteName(models.Model):
    OS_CHOICES = [
        ('centos', 'CentOS'),
        ('windows', 'Windows'),
        ('ubuntu', 'Ubuntu'),
    ]
    operating_system = models.CharField(max_length=50, choices=OS_CHOICES, verbose_name=_("Operating System"))
    test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE, verbose_name=_("Test Suite"))
    location = models.FileField(upload_to='test_locations/', help_text=_("Enter folder location"), verbose_name=_("Location"))
    user_name = models.CharField(max_length=50, verbose_name=_("User Name"))
    password = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[\w.@+-]+$', message='Invalid password format')], verbose_name=_("Password"))

    def __str__(self):
        return f"{self.operating_system} - {self.location}"




# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator

# class TestSuite(models.Model):
#     PROTOCOL_CHOICES = [
#         ('SMB', 'SMB'),
#         ('P1', 'P1'),
#         ('P2', 'P2'),
#         ('P3', 'P3'),
#         ('P4', 'P4'),
#     ]

#     LOG_LEVEL_CHOICES = [
#         ('Debug', 'Debug'),
#         ('Warning', 'Warning'),
#         ('Critical', 'Critical'),
#         ('Info', 'Info'),
#     ]
    
#     YES_NO_CHOICES = [
#         (True, 'YES'),
#         (False, 'NO'),
#     ]


#     protocol = models.CharField(max_length=50, choices=PROTOCOL_CHOICES)
#     host_ip_address = models.GenericIPAddressField()
#     share = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[a-zA-Z0-9]*$',message='Share must contain only alphanumeric characters')])
#     user_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[\w.@+-]+$',message='Invalid password format')])
#     log_level = models.CharField(max_length=50, choices=LOG_LEVEL_CHOICES)
#     sign = models.BooleanField(default=True, choices=YES_NO_CHOICES)
#     encrypt = models.BooleanField(default=False, choices=YES_NO_CHOICES)
#     trace = models.BooleanField(default=False, choices=YES_NO_CHOICES)
#     min_dialect = models.IntegerField(validators=[MinValueValidator(0)])
#     max_dialect = models.IntegerField(validators=[MaxValueValidator(1000)])

#     def __str__(self):
#         return f"{self.protocol} - {self.host_ip_address} - {self.share} - {self.user_name}"


# class TestSuiteName(models.Model):
#     OS_CHOICES = [
#         ('centos', 'CentOS'),
#         ('windows', 'Windows'),
#         ('ubuntu', 'Ubuntu'),
#     ]
#     operating_system = models.CharField(max_length=50, choices=OS_CHOICES)
#     test_suite = models.ForeignKey(TestSuite, on_delete=models.CASCADE)
#     location = models.FileField(upload_to='test_locations/', help_text="Enter folder location")
#     user_name = models.CharField(max_length=50)
#     password = models.CharField(max_length=50, validators=[RegexValidator(regex=r'^[\w.@+-]+$',message='Invalid password format')])

#     def __str__(self):
#         return f"{self.operating_system} - {self.location}"

