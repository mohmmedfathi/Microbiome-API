from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson import json_util
from .pymongo import collection
from pymongo.errors import BulkWriteError
from django.http import HttpResponseBadRequest

@csrf_exempt
def list_disease_info(request):
    """
        GET     --> List all disease_infos 
    """
    
    if request.method == 'GET':
        disease_info_OBJECTS = collection.find()

        json_data = json_util.dumps(disease_info_OBJECTS)

        
        return HttpResponse(json_data, content_type='application/json')
    else :
        return HttpResponse("GET Method only allowed in list")
    
@csrf_exempt
def create_one_disease_info(request):
    """
        POST     --> Create one disease_info 
    """

    if request.method == 'POST':
        data = json.loads(request.body)
        result = collection.find_one({"_id": data["_id"]})
        
        
        if result:    
            return HttpResponseBadRequest('Error : element is already exist')
        else : 
            result = collection.insert_one(data)
            
        return JsonResponse({'message': 'disease_info added', 'disease_info_id': str(result.inserted_id)})
    else:
        return HttpResponse("POST Method only allowed in create_one")

@csrf_exempt
def create_many_disease_info(request):
    """
        POST     --> Create multi disease_info 
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
def specific_disease_info(request, disease_id=None):
    """
        GET     --> return speicific disease_info with (disease_id ID)
        PATCH   ->  update speicific disease_info with (disease_id ID)
        DELETE  ->  Delete speicific disease_info with (disease_id ID)
    """
    if request.method == 'GET':
        
        if disease_id is not None:
            disease_info = collection.find_one({'_id': disease_id})
            
            if disease_info:
                
                return JsonResponse(json.loads(json_util.dumps(disease_info)))
            else:
                return JsonResponse({'error': 'disease_info not found'})
        else:
            disease_info_obj = []
            for disease_info in collection.find():
                disease_info_obj.append(disease_info)
            return JsonResponse(disease_info_obj, safe=False)
    
    elif request.method == 'PATCH':
        
        data = json.loads(request.body)
        print(data)
        del data['_id'] 
        disease_info = collection.update_one({'disease_id': disease_id}, {'$set': data})
        if disease_info.modified_count > 0:
            return JsonResponse({'message': 'disease_info updated'})
        else:
            return JsonResponse({'error': 'disease_info not found'})
        
    elif request.method == 'DELETE':
        
        disease_info = collection.delete_one({'disease_id': disease_id})
        if disease_info.deleted_count > 0:
            return JsonResponse({'message': 'disease_info deleted'})
        else:
            return JsonResponse({'error': 'disease_info not found'})
    
    else : 
        return HttpResponse("this Method not allowed in specific disease_info")
    



def delete_many(request):
    
    if request.method == 'GET':
        field = request.GET.get('field')
        value = request.GET.get('value')
        print(field,"======",value)
        if not field:
            return HttpResponseBadRequest('Query parameter "field" is required')
        
        if not value:
            return HttpResponseBadRequest('Query parameter "value" is required')
        
        result = collection.delete_many({field: value})
        
        if result.deleted_count == 0:
            return HttpResponseBadRequest(f'No documents found with field "{field}"')
        else:
            return HttpResponse(f'Removed field "{field}" from {result.modified_count} documents')
        
    else:
        return HttpResponseBadRequest('Only GET requests are allowed')        

@csrf_exempt
def create_index(request):
    if request.method == 'GET':
        field = request.GET.get('field')
        order = request.GET.get('order')
        order = order.replace("/", "")
        print(order)
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
