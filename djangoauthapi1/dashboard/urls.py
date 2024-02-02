
from django.urls import path
from .views import TestSuiteCreateView, TestSuiteNameCreateView

urlpatterns = [
    path('test-suite/', TestSuiteCreateView.as_view(), name='test_suite_create'),
    path('test-suite-name/', TestSuiteNameCreateView.as_view(), name='test_suite_name_create'),
]
