from django.urls import path, include
from apps.clinic.views import doctor, patient, branch, service, tag

app_name='clinic'
doctor_urls=[
    path('', doctor.DoctorListView.as_view(), name='doctor-list'),
    path('<int:pk>/', doctor.DoctorRetrieveView.as_view(), name='doctor-detail'),
    path('create/', doctor.DoctorCreateView.as_view(), name='doctor-create'),
    path('<int:pk>/update/', doctor.DoctorUpdateView.as_view(), name='doctor-update'),
    path('<int:pk>/delete/', doctor.DoctorDestroyView.as_view(), name='doctor-delete'),
]

patient_urls=[
    path('', patient.PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', patient.PatientRetrieveView.as_view(), name='patient-detail'),
    path('create/', patient.PatientCreateView.as_view(), name='patient-create'),
    path('<int:pk>/update/', patient.PatientUpdateView.as_view(), name='patient-update'),
    path('<int:pk>/delete/', patient.PatientDestroyView.as_view(), name='patient-delete'),
]

branch_urls=[
    path('', branch.BranchListView.as_view(), name='branch-list'),
    path('<int:pk>/', branch.BranchRetrieveView.as_view(), name='branch-detail'),
    path('create/', branch.BranchCreateView.as_view(), name='branch-create'),
    path('<int:pk>/update/', branch.BranchUpdateView.as_view(), name='branch-update'),
    path('<int:pk>/delete/', branch.BranchDestroyView.as_view(), name='branch-delete'),

]

service_urls=[
    path('', service.ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', service.ServiceRetrieveView.as_view(), name='service-detail'),
    path('create/', service.ServiceCreateView.as_view(), name='service-create'),
    path('<int:pk>/update/', service.ServiceUpdateView.as_view(), name='service-update'),
    path('<int:pk>/delete/', service.ServiceDestroyView.as_view(), name='service-delete'),
]

tag_urls=[
    path('', tag.TagListView.as_view(), name='tag-list'),
    path('create/', tag.TagCreateView.as_view(), name='tag-create'),
    path('<int:pk>/update/', tag.TagUpdateView.as_view(), name='tag-update'),
    path('<int:pk>/delete/', tag.TagDestroyView.as_view(), name='tag-delete'),
]

director_urls=[
    path('', branch.DirectorListCreateView.as_view(), name='director-list-create'),
    path('<int:pk>/', branch.DirectorRetrieveUpdateDestroyView.as_view(), name='director-detail-update-delete'),
]

urlpatterns=[
    path('doctor/', include(doctor_urls)),
    path('patient/', include(patient_urls)),
    path('branch/', include(branch_urls)),
    path('service/', include(service_urls)),
    path('tag/', include(tag_urls)),
    path('director/', include(director_urls)),

]



