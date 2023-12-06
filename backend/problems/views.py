from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from .models import Problem, Submission
from .serializers import ProblemSerializer, SubmissionSerializer, UserLoginSerializer, UserSignupSerializer

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh), 'access': str(refresh.access_token)}
        serializer.validated_data['tokens'] = data
        return Response(serializer.data)

class LoginView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        username_or_email = request.data.get('username_or_email')
        password = request.data.get('password')

        user = authenticate(request, username=username_or_email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            data = {'refresh': str(refresh), 'access': str(refresh.access_token)}
            return Response(data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProblemList(generics.ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class ProblemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SubmissionList(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class SubmissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]