from django.urls import path
from .views import(
TestSuiteCreateView, 
TestSuiteNameCreateView,
TestSuiteListView, 
TestSuiteNameListView,
TestSuiteDeleteView,
TestSuiteNameDeleteView,
TestSuiteDetailView,
)

urlpatterns = [
    path('test-suite/', TestSuiteCreateView.as_view(), name='test_suite_create'),
    path('test-suite-list/', TestSuiteListView.as_view(), name='test_suite_list'), 
    path('test-suite/<int:pk>/', TestSuiteDetailView.as_view(), name='test_suite_detail'),
    path('test-suite-name/', TestSuiteNameCreateView.as_view(), name='test_suite_name_create'),
    path('test-suite-name-list/', TestSuiteNameListView.as_view(), name='test_suite_name_list'),
    path('test-suite_delete/<int:pk>/', TestSuiteDeleteView.as_view(), name='test_suite_delete'),  
    path('test-suite-name/<int:pk>/', TestSuiteNameDeleteView.as_view(), name='test_suite_name_delete'),  

]