from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import TestSuite, TestSuiteName
from .serializers import TestSuiteSerializer, TestSuiteNameSerializer
from rest_framework.permissions import IsAuthenticated
from .serializers import TestSuiteDetailSerializer

class TestSuitePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 10000



class TestSuiteCreateView(generics.CreateAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        test_suite_id = serializer.instance.id

        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuite created successfully', 'data': {'id': test_suite_id}}, headers=headers)




class TestSuiteListView(generics.ListAPIView):
    queryset = TestSuite.objects.all().order_by('id')
    serializer_class = TestSuiteSerializer
    pagination_class = TestSuitePagination
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuites retrieved successfully', 'data': serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuites retrieved successfully', 'data': serializer.data})




class TestSuiteDeleteView(generics.DestroyAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite deleted successfully'})
    
    
    

class TestSuiteNamePagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 1000



class TestSuiteNameCreateView(generics.CreateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        test_suite_name_id = serializer.instance.id

        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuiteName created successfully', 'data': {'id': test_suite_name_id}}, headers=headers)




class TestSuiteNameListView(generics.ListAPIView):
    queryset = TestSuiteName.objects.all().order_by('id')
    serializer_class = TestSuiteNameSerializer
    pagination_class = TestSuiteNamePagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteNames retrieved successfully', 'data': serializer.data})





class TestSuiteNameDeleteView(generics.DestroyAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName deleted successfully'})




class TestSuiteDetailView(generics.RetrieveAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteDetailSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuite detail retrieved successfully', 'data': serializer.data})




class TestSuiteNameUpdateView(generics.UpdateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({'status': 'success', 'code': status.HTTP_200_OK, 'msg': 'TestSuiteName updated successfully', 'data': serializer.data})








