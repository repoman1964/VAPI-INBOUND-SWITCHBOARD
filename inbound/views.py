from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from environs import Env

env = Env()
env.read_env()

VAPI_URL_SECRET = env.str("VAPI_URL_SECRET")
VAPI_PHONE_LIST = env.list("VAPI_PHONE_LIST")

@csrf_exempt
def testAndDirectInboundCall(request):
    """
    View function to handle and direct inbound calls.

    This function validates the incoming request, extracts call information,
    and routes the call to the appropriate handling function based on the phone number ID.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        JsonResponse: A JSON response indicating the result of the operation or any errors.

    Raises:
        JsonResponse: With appropriate error messages and status codes for invalid requests.
    """

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
    
    vapi_phone_list = VAPI_PHONE_LIST


    if phone_number_id not in vapi_phone_list:        
        return JsonResponse({'error': 'Request Forbidden'}, status=403)
    
    # Extract additional useful information
    customer_number = call_data.get("customer", {}).get("number")
    call_status = call_data.get("status")
    call_id = call_data.get("id")
     
    # Route to appropriate app based on phone ID
    if phone_number_id == vapi_phone_list[0]:
        vapi_phone_id = vapi_phone_list[0]     
        return phone_id_one_call(request_data, vapi_phone_list[0])
    elif phone_number_id == vapi_phone_list[1]:
        return phone_id_two_call(request_data, vapi_phone_list[1])
    elif phone_number_id == vapi_phone_list[2]:
        return phone_id_three_call(request_data, vapi_phone_list[2])
    else:
        return JsonResponse({'error': 'Unknown phone ID'}, status=400)
    

def phone_id_one_call(request_data, vapi_phone_id):
    """
    Handle calls for the first phone ID.

    Args:
        request_data (dict): The parsed request data.
        vapi_phone_id (str): The phone ID being handled.

    Returns:
        JsonResponse: A JSON response indicating the phone ID switch.
    """
    print('DO SOMETHING HERE IF PHONE ID ONE')

    return JsonResponse(f"Switched to phone id {vapi_phone_id}", status=200, safe=False)

def phone_id_two_call(request_data, vapi_phone_id):
    """
    Handle calls for the second phone ID.

    Args:
        request_data (dict): The parsed request data.
        vapi_phone_id (str): The phone ID being handled.

    Returns:
        JsonResponse: A JSON response indicating the phone ID switch.
    """

    print('DO SOMETHING HERE IF PHONE ID TWO')

    return JsonResponse(f"Switched to phone id {vapi_phone_id}", status=200, safe=False)

def phone_id_three_call(request_data, vapi_phone_id):
    """
    Handle calls for the third phone ID.

    Args:
        request_data (dict): The parsed request data.
        vapi_phone_id (str): The phone ID being handled.

    Returns:
        JsonResponse: A JSON response indicating the phone ID switch.
    """
    
    print('DO SOMETHING HERE IF PHONE ID THREE')

    return JsonResponse(f"Switched to phone id {vapi_phone_id}", status=200, safe=False)




  

    
