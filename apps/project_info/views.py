from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson import json_util
from .pymongo import collection
from django.http import HttpResponseBadRequest
from pymongo.errors import BulkWriteError
from .redis import redis_client
@csrf_exempt
def list_project_info(request):
    """
        GET     --> List all project_infos 
    """
    
    if request.method == 'GET':
        if redis_client.exists('project_info_cache'):
            json_data = redis_client.get('project_info_cache')
            print("returned from cache")
        else : 
            project_info_OBJECTS = collection.find()

            
            json_data = json_util.dumps(project_info_OBJECTS)

            redis_client.set('project_info_cache', json_data)
            print("setted!")
        return HttpResponse(json_data, content_type='application/json')
    else :
        return HttpResponse("GET Method only allowed in list")
    
@csrf_exempt
def create_one_project_info(request):
    """
        POST     --> Create one project_info 
    """
    
    if request.method == 'POST':
        data = json.loads(request.body)
        result = collection.find_one({"Human_id": data["Human_id"]})
        if result:
            return HttpResponseBadRequest('Error : element is already exist')
        else:
            result = collection.insert_one(data)
            
        return JsonResponse({'message': 'project_info added', 'project_info_id': str(result.inserted_id)})
    else:
        return HttpResponse("POST Method only allowed in create_one")

@csrf_exempt
def create_many_project_info(request):
    """
        POST     --> Create multi project_info 
    """
    if request.method == 'POST':
        documents = json.loads(request.body)
        
        try:
            result = collection.insert_many(documents)
            return JsonResponse({'message': f'{len(result.inserted_ids)} documents inserted'})
        
        except BulkWriteError as e:
            return HttpResponseBadRequest('Error : one or more of elements is already exist')
        
    else:
        return HttpResponse("POST Method only in create_many")

@csrf_exempt
def specific_project_info(request, Human_id=None):
    """
        GET     --> return speicific project_info with (HMP ID)
        PATCH   ->  update speicific project_info with (HMP ID)
        DELETE  ->  Delete speicific project_info with (HMP ID)
    """
    if request.method == 'GET':
        
        if Human_id is not None:
            project_info = collection.find_one({'Human_id': Human_id})
            
            if project_info:
                
                return JsonResponse(json.loads(json_util.dumps(project_info)))
            else:
                return HttpResponseBadRequest('project_info with this id not found')
    
    elif request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            del data['_id'] 
            project_info = collection.update_one({'Human_id': Human_id}, {'$set': data})
            if project_info.modified_count > 0:
                return JsonResponse({'message': 'project_info updated'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON request body'}, status=400)
        else:
            return JsonResponse({'error': 'project_info not found'},status = 400)
        
            
        
    elif request.method == 'DELETE':
        
        project_info = collection.delete_one({'Human_id': Human_id})
        if project_info.deleted_count > 0:
            return JsonResponse({'message': 'project_info deleted'})
        else:
            return JsonResponse({'error': 'project_info not found'},status = 400)
    
    else : 
        return HttpResponse("this Method not allowed in specific project_info")
    

@csrf_exempt
def aggregate_project_info(request):
    """
        GET --> Aggregate all project_infos with optional filtering by domain, sorting, and grouping
        Query parameters:
            domain: filter by domain (optional)
            sort_by: sort by field (optional)
            group_by: group by field (optional)
            
    """
    # Parse query parameters
    domain = request.GET.get('domain')
    sort_by = request.GET.get('sort_by')
    group_by = request.GET.get('group_by')

    # Build aggregation pipeline
    pipeline = []
    
    if domain:
        pipeline.append({'$match': {'Domain': domain}})
    
    if sort_by:
        pipeline.append({'$sort': {sort_by: 1}})
        
    if group_by:
        pipeline = {'$group': {'_id': '$Domain','count': {'$sum': 1}}}
        # group the documents by the 'Domain' field 
        # count the number of documents in each group using the $sum operator.
        pipeline.append({'$group': {'_id': '$' + group_by, 'count': {'$sum': 1}}})
    
    pipeline.append({'$project': {'_id': 0, 'data': '$$ROOT'}})

    # Execute aggregation query
    results = collection.aggregate(pipeline)

    # Serialize results as JSON
    serialized = json_util.dumps(list(results))

    return HttpResponse(serialized, content_type='application/json')

@csrf_exempt
def create_index(request):
    if request.method == 'POST':
        field = request.GET.get('field')
        order = request.GET.get('order')
        
        if not field:
            return HttpResponseBadRequest('Query parameter "field" is required')
        
        if not order:
            return HttpResponseBadRequest('Query parameter "order" is required')
        
        # create the index on the specified field
        result = collection.create_index([(str(field), int(order))])

        indexes = collection.index_information()
        
        return HttpResponse(f'Index created on field "{field}" with name "{result}" \n current indexes = "{indexes}"')

    else:
        return HttpResponseBadRequest('Only GET requests are allowed')

@csrf_exempt
def show_indexs(request):
    if request.method == 'GET':
        indexes = collection.index_information()
        return JsonResponse(indexes)
    else:
        return HttpResponseBadRequest('Only GET requests are allowed')



@csrf_exempt
def delete_many(request):
    
    if request.method == 'GET':
        field = request.GET.get('field')
        value = request.GET.get('value')
        
        # GOLD_ID:"oppo"
        
        if not field:
            return HttpResponseBadRequest('Query parameter "field" is required')
        
        if not value:
            return HttpResponseBadRequest('Query parameter "value" is required')
        
        result = collection.delete_many({field: value})
        
        if result.deleted_count == 0:
            return HttpResponseBadRequest(f'No documents found with field "{field}"')
        else:
            return HttpResponse(f'Removed field "{field}" from {result.deleted_count} documents')
        
    else:
        return HttpResponseBadRequest('Only GET requests are allowed') 