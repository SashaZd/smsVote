import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

from ..models import SVUser, SVPollingBooth


@csrf_exempt
def userRequest(request, user_id=None):
	if request.method == "POST":
		return createUser(request)
	else:
		return getUser(request, user_id)



@csrf_exempt
def createUser(request):
	first_name = request.POST.get('first_name','')
	last_name = request.POST.get('last_name','')
	phone_number = request.POST.get('phone_number','')
	polling_Booth = request.POST.get('polling_Booth','')

	user = None
	existing_users = SVUser.objects.filter(phone_number=phone_number)

	if len(existing_users) > 1:
		# User Exists!
		existing_user = existing_users[0]
		errorMessage = "Error! User with this phone_number already exists."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if user is None:
		user = SVUser()
	user.first_name = first_name
	user.last_name = last_name
	user.phone_number = phone_number
	# user.polling_Booth = polling_Booth

	booth = None
	if polling_Booth:
		booths = SVPollingBooth.objects.filter(id=polling_Booth)

		if len(booths)>0:
			booth = booths[0]
		else: 
			errorMessage = "Error! This booth doesn't exist."
			return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if booth is not None:
		user.polling_Booth = booth

	user.save()

	response_data = user.getResponseData()
	# response_data = SVPollingBooth.objects.filter(id=polling_Booth)
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getUser(request, user_id):
	response_data = {}
	if user_id:
		users = SVUser.objects.filter(id=user_id)
		
		#Ideally there shouldn't be duplicate users.

		if len(users)>0:
			user = users[0]
			response_data = user.getResponseData()

		else:
			existing_user = existing_users[0]
			errorMessage = "Error! This user doesn't exist."
			return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")			

	return HttpResponse(json.dumps(response_data), content_type="application/json")





