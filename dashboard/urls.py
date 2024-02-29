from django.urls import path
from .views import (
    SuiteNameView,
    TestSuiteCreateView,
    TestSuiteNameCreateView,
    TestSuiteListView,
    TestSuiteNameListView,
    TestSuiteDeleteView,
    TestSuiteNameDeleteView,
    TestSuiteDetailView,
    TestSuiteNameListViewBySuite,
    TestSuiteNameRetrieveView,
    TestSuiteNameUpdateView, 
   
)

urlpatterns = [
    path('test-suite/', TestSuiteCreateView.as_view(), name='test_suite_create'),
    path('test-suite-list/', TestSuiteListView.as_view(), name='test_suite_list'), 
    path('test-suite/<int:pk>/', TestSuiteDetailView.as_view(), name='test_suite_detail'),
    path('test-suite-name/', TestSuiteNameCreateView.as_view(), name='test_suite_name_create'),
    path('test-suite-name-list/', TestSuiteNameListView.as_view(), name='test_suite_name_list'),
    path('single-test-suite-name/<int:pk>/', TestSuiteNameRetrieveView.as_view(), name='testsuites-detail'),
    path('test-suite-name-list/<int:pk>/', TestSuiteNameListViewBySuite.as_view(), name='test_suite_name_list'),
    path('test-suite-delete/<int:pk>/', TestSuiteDeleteView.as_view(), name='test_suite_delete'),  
    path('test-suite-name-delete/<int:pk>/', TestSuiteNameDeleteView.as_view(), name='test_suite_name_delete'),
    path('test-suite-name-update/<int:pk>/', TestSuiteNameUpdateView.as_view(), name='test_suite_name_update'),
    path('suite-names/', SuiteNameView.as_view(), name='suite_names'),
]