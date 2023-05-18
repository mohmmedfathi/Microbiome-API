from django.urls import path,include
from .views import specific_human_info,create_one_human_info,list_human_info,create_many_human_info,aggregate_human_info,delete_many,create_index,show_indexs

urlpatterns = [
    
    
    #handle specific microbiome (GET,PATCH,DELETE)
    path('<int:human_id>/' ,specific_human_info),
    
    #handle create new one microbiome (POST)
    path('create_one/' ,create_one_human_info),
    
    #handle create new many microbiome (POST)
    path('create_many/' ,create_many_human_info),
    
    # list all microbiome data in Collection
    path('list/', list_human_info),
    
    path('aggregation/',aggregate_human_info),
    
    path('delete_many/',delete_many),
    
    path('create_index/',create_index),
    
    path('show_indexes/',show_indexs),
    
]
