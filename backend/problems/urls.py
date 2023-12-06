from django.urls import path
from .views import ProblemList, ProblemDetail, SubmissionList, SubmissionDetail

urlpatterns = [
    path('problems/', ProblemList.as_view(), name='problem-list'),
    path('problems/<int:pk>/', ProblemDetail.as_view(), name='problem-detail'),
    path('submissions/', SubmissionList.as_view(), name='submission-list'),
    path('submissions/<int:pk>/', SubmissionDetail.as_view(), name='submission-detail'),
]