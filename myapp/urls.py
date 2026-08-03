from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.Userlogin, name='login'),
    path('register/', views.Usersignup, name='register'),
    path('profile/', views.Userprofile, name='profile'),
    path('logout/', views.Userlogout, name='logout'),
    path('members/', views.member_list, name='members'),
    path('members/add/', views.add_member, name='addmember'),
    # View button click hone par member ID wise edit page khulega
    path('members/edit/<int:pk>/', views.edit_member, name='memberdetails'),
    # Export Excel URL
    path('members/export/excel/', views.export_members_excel, name='export_members_excel'),

    #admin url
    path('allmemberslist/',views.all_members,name='allmembers'),
    path('allzimmedarlist/', views.all_zimmedar, name='allzimmedar'),
    # Excel download view for user/zimmedar
    path('export-users-excel/', views.export_users_excel, name='export_users_excel'),  
    
      
]