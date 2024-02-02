from rest_framework import serializers
from .models import TestSuite, TestSuiteName

class TestSuiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSuite
        fields = ['protocol', 'host_ip_address', 'share', 'user_name', 'password',  'log_level', 'sign', 'encrypt', 'trace', 'min_dialect', 'max_dialect' ]
        
        

class TestSuiteNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSuiteName
        fields = ['name', 'operating_system', 'test_suite', 'location']