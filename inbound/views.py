from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from environs import Env

from metra.views import handle_metra_call
from sharks.views import handle_sharks_call
from medspa.views import handle_medspa_call

env = Env()
env.read_env()

VAPI_URL_SECRET = env.str("VAPI_URL_SECRET")

@csrf_exempt
def testAndDirectInboundCall(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)    
    try:
        # Assuming the POST data is sent as JSON
        request_data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
    message = request_data.get("message", {})
    if message.get("type") != "assistant-request":
        return JsonResponse({'error': 'Endpoint only for assistant requests'}, status=404)

   # Verify serverUrlSecret
    phone_number = message.get("phoneNumber", {})
    server_url_secret = phone_number.get("serverUrlSecret")

    if server_url_secret != VAPI_URL_SECRET:
        return JsonResponse({'error': 'Request Forbidden'}, status=403)
    
    call_data = message.get("call", {})
    phone_number_id = call_data.get("phoneNumberId")
    
    vapi_phone_list = [
        "95606d61-7ead-4836-847f-ae20dd869b33",
        "285e5e94-ad1b-4910-b66c-5048eab0ad58",
        "ffe3fe49-db4c-40a1-ad89-4b0b5188ff0d"
    ]

    if phone_number_id not in vapi_phone_list:        
        return JsonResponse({'error': 'Request Forbidden'}, status=403)
    
    # Extract additional useful information
    customer_number = call_data.get("customer", {}).get("number")
    call_status = call_data.get("status")
    call_id = call_data.get("id")
     
    # Route to appropriate app based on phone ID
    if phone_number_id == "95606d61-7ead-4836-847f-ae20dd869b33":
        return handle_metra_call(request_data)
    elif phone_number_id == "285e5e94-ad1b-4910-b66c-5048eab0ad58":
        return handle_sharks_call(request_data)
    elif phone_number_id == "ffe3fe49-db4c-40a1-ad89-4b0b5188ff0d":
        return handle_medspa_call(request_data)
    else:
        return JsonResponse({'error': 'Unknown phone ID'}, status=400)
    
  

    
