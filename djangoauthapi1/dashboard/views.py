from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import TestSuite, TestSuiteName
from .serializers import TestSuiteSerializer, TestSuiteNameSerializer

class TestSuitePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 10000

class TestSuiteCreateView(generics.CreateAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuite created successfully'}, headers=headers)

class TestSuiteListView(generics.ListAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    pagination_class = TestSuitePagination

class TestSuiteDeleteView(generics.DestroyAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer

class TestSuiteNamePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 1000

class TestSuiteNameCreateView(generics.CreateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuiteName created successfully'}, headers=headers)

class TestSuiteNameListView(generics.ListAPIView):
    queryset = TestSuiteName.objects.all().order_by('id')
    serializer_class = TestSuiteNameSerializer
    pagination_class = TestSuiteNamePagination


class TestSuiteNameDeleteView(generics.DestroyAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
















# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status
# from .models import TestSuite, TestSuiteName 
# from .serializers import TestSuiteSerializer 
# from .serializers import TestSuiteNameSerializer 
# from .serializers import TestSuiteSerializer, TestSuiteNameSerializer

# class TestSuiteCreateView(generics.CreateAPIView):
#     queryset = TestSuite.objects.all()
#     serializer_class = TestSuiteSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuite created successfully'}, headers=headers)


# class TestSuiteNameCreateView(generics.CreateAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuiteName created successfully'}, headers=headers)


# class TestSuiteListView(generics.ListAPIView):
#     queryset = TestSuite.objects.all()
#     serializer_class = TestSuiteSerializer


# class TestSuiteNameListView(generics.ListAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer


# class TestSuiteDeleteView(generics.DestroyAPIView):
#     queryset = TestSuite.objects.all()
#     serializer_class = TestSuiteSerializer


# class TestSuiteNameDeleteView(generics.DestroyAPIView):
#     queryset = TestSuiteName.objects.all()
#     serializer_class = TestSuiteNameSerializer


