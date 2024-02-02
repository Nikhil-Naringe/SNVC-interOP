
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import TestSuite , TestSuiteName 
from .serializers import TestSuiteSerializer 
from .serializers import TestSuiteNameSerializer 

class TestSuiteCreateView(generics.CreateAPIView):
    queryset = TestSuite.objects.all()
    serializer_class = TestSuiteSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuite created successfully'}, headers=headers)





class TestSuiteNameCreateView(generics.CreateAPIView):
    queryset = TestSuiteName.objects.all()
    serializer_class = TestSuiteNameSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'status': 'success', 'code': status.HTTP_201_CREATED, 'msg': 'TestSuiteName created successfully'}, headers=headers)
