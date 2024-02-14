from rest_framework import serializers
from .models import TestSuite, TestSuiteName

class TestSuiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSuite
        fields = ['id', 'protocol', 'host_ip_address', 'share', 'user_name', 'password', 'log_level', 'sign', 'encrypt', 'trace', 'min_dialect', 'max_dialect']
        read_only_fields = ['id']

class TestSuiteNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestSuiteName
        fields = ['id', 'user_name', 'password', 'operating_system', 'test_suite', 'location']
        read_only_fields = ['id']
