from django.urls import path,include
from .views import list_project_info,create_one_project_info,create_many_project_info,specific_project_info,aggregate_project_info,show_indexs,create_index

urlpatterns = [
    
    #handle specific project_info (GET,PATCH,DELETE)
    path('<int:Human_id>/' ,specific_project_info),
    
    #handle create new one project_info (POST)
    path('create_one/' ,create_one_project_info),
    
    #handle create new many project_info (POST)
    path('create_many/' ,create_many_project_info),
    
    # list all project_info data in Collection
    path('list/', list_project_info),
    
    path('aggregate_project_info/',aggregate_project_info),
    
    # create index
    path('create_index',create_index),
    
    # show all indexes
    path('show_indexes/',show_indexs),
    
    
]
