import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta

from ..models import SVPollingBooth


@csrf_exempt
def boothRequest(request, booth_id=None):
	if request.method == "POST":
		return createBooth(request)
	else:
		return getBooth(request, booth_id)



@csrf_exempt
def createBooth(request):
	booth_name = request.POST.get('booth_name','')
	booth_address = request.POST.get('booth_address','')
	
	booth = None
	existing_booths = SVPollingBooth.objects.filter(booth_name=booth_name)

	if len(existing_booths) >= 1:
		# Booth Exists!
		booth = existing_booths[0]
		errorMessage = "Error! Booth already exists."
		return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")

	if booth is None:
		booth = SVPollingBooth()
	booth.booth_name = booth_name
	booth.booth_address = booth_address
	
	booth.save()

	response_data = booth.getResponseData()
	
	return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def getBooth(request, booth_id):
	response_data = {}
	if booth_id:
		booths = SVPollingBooth.objects.filter(id=booth_id)
		
		#Ideally there shouldn't be duplicate booths.

		if len(booths)>0:
			booth = booths[0]
			response_data = booth.getResponseData()

		else:
			errorMessage = "Error! This booth doesn't exist."
			return HttpResponse(json.dumps({'success': False, "error":errorMessage}), content_type="application/json")			

	return HttpResponse(json.dumps(response_data), content_type="application/json")

@csrf_exempt
def boothSMS(request, booth_id):
	booth_id = request.GET.get('booth_id','')
	response_data = []
	if booth_id:
		booths = SVPollingBooth.objects.filter(id=booth_id)

		if len(booths)>0:
			booth = booths[0]
			# response_data = booth.getResponseData()
			users = booth.assigned_to_user.all()
			for user in users:
				#Code for sending SMS goes here

				#Response data with whatever response you want. I've currently listed out the users but you might want
				#something like {success: true}
				response_data.append(user.getResponseData())

	# return HttpResponse(json.dumps({"success":True}), content_type="application/json")
	return HttpResponse(json.dumps(response_data), content_type="application/json")



