from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from bson import json_util
from .pymongo import collection
from django.http import HttpResponseBadRequest
from pymongo.errors import BulkWriteError


@csrf_exempt
def list_human_info(request):
    """
        GET     --> List all human_infos 
    """

    if request.method == 'GET':
        human_info_OBJECTS = collection.find()

        json_data = json_util.dumps(list(human_info_OBJECTS))

        return HttpResponse(json_data, content_type='application/json')
    else:
        return HttpResponse("GET Method only allowed in list")


@csrf_exempt
def create_one_human_info(request):
    """
        POST     --> Create one human_info 
    """

    if request.method == 'POST':
        data = json.loads(request.body)
        result = collection.insert_one(data)
        return JsonResponse({'message': 'human_info added', 'human_info_id': str(result.inserted_id)})
    else:
        return HttpResponse("POST Method only allowed in create_one")


@csrf_exempt
def create_many_human_info(request):
    """
        POST     --> Create multi human_info 
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
def specific_human_info(request, human_id=None):
    """
        GET     --> return speicific human_info with (HMP ID)
        PATCH   ->  update speicific human_info with (HMP ID)
        DELETE  ->  Delete speicific human_info with (HMP ID)
    """
    if request.method == 'GET':

        if human_id is not None:

            human_info = collection.find_one({"HMP_ID": str(human_id)})

            if human_info:

                return JsonResponse(json.loads(json_util.dumps(human_info)), safe=False)
            else:
                return HttpResponseBadRequest('human_info with this id not found')

    elif request.method == 'PATCH':
        try:
            data = json.loads(request.body)
            del data['_id']
            human_info = collection.update_one(
                {'HMP_ID': str(human_id)}, {'$set': data})
            if human_info.modified_count > 0:
                return JsonResponse({'message': 'human_info updated'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON request body'}, status=400)
        else:
            return JsonResponse({'error': 'human_info not found'})

    elif request.method == 'DELETE':

        human_info = collection.delete_one({'HMP_ID': str(human_id)})
        if human_info.deleted_count > 0:
            return JsonResponse({'message': 'human_info deleted'})
        else:
            return JsonResponse({'error': 'human_info not found'}, status=400)

    else:
        return HttpResponse("this Method not allowed in specific human_info")


@csrf_exempt
def aggregate_human_info(request):
    """
        GET --> Aggregate all human_infos with optional filtering by domain, sorting, and grouping
        Query parameters:
            domain: filter by domain (optional)
            sort_by: sort by field (optional)
            group_by: group by field (optional)
    """
    if request.method == 'GET':
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
            pipeline.append(
                {'$group': {'_id': '$' + group_by, 'count': {'$sum': 1}}})

        pipeline.append({'$project': {'_id': 0, 'data': '$$ROOT'}})

        results = collection.aggregate(pipeline)

        serialized = json_util.dumps(list(results))

        return HttpResponse(serialized, content_type='application/json')
    else:
        return HttpResponseBadRequest('GET Method only allowed in list')


@csrf_exempt
def delete_many(request):

    if request.method == 'GET':
        field = request.GET.get('field')
        value = request.GET.get('value')

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
        return HttpResponseBadRequest('Only POST requests are allowed')


@csrf_exempt
def show_indexs(request):
    if request.method == 'GET':
        indexes = collection.index_information()
        return JsonResponse(indexes)
    else:
        return HttpResponseBadRequest('Only GET requests are allowed')
