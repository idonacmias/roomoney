from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('add_debt/', views.add_debt),
    path('url_num/<int:num>/', views.read_url_num),
    path('roommate_data/<str:name>', views.roommate_data),
    path('update_phone_number/<str:name>/<str:phone>/', views.update_phone_number),
    path('create_new_partner/<str:name>/<str:date_of_berith>/<str:phone>/<str:email>', views.create_new_partner),
    path('delete_partner/<str:name>/', views.delete_partner),
    path('display_partner/<str:name>/', views.display_partner),
    path('display_all_partners/', views.display_all_partners),
    path('add_partner/', views.add_partner),
    path('display_transaction/<str:name>/', views.display_transaction), 
    path('display_partner_debt_sum/', views.display_partner_debt_sum),
    path('transaction_list/', views.transaction_list),
    path('transaction_dtails/', views.transaction_dtails),
    path('partner_details/<int:pk>/', views.partner_details),
    path('return_json/', views.PartnerViewSet.as_view({'get' : 'list'})),    
]

