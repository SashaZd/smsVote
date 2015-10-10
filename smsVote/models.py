from django.db import models

# Create your models here.

# Table for Users
class SVUser(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	phone_number = models.EmailField(max_length=30)
	polling_Booth = models.ForeignKey('SVPollingBooth', related_name="assigned_to_user")

	def __unicode__(self):
		return self.first_name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["user_id"] = self.id
		response_data["first_name"] = self.first_name
		response_data["last_name"] = self.last_name
		response_data["phone_number"] = self.phone_number
		response_data["polling_Booth"] = self.polling_Booth

		return response_data


class SVPollingBooth(models.Model):
	booth_name = models.CharField(max_length=200)
	booth_address = models.CharField(max_length=200)

	def __unicode__(self):
	    return self.booth_name

	def getResponseData(self):

		#Create Resposne Dictionary
		response_data = {}
		response_data["booth_name"] = self.booth_name
		response_data["booth_address"] = self.booth_address
		response_data["booth_id"] = self.id
		
		electorate = []

		voters = SVUser.objects.filter(polling_Booth=self.id)
		if voters and len(voters) > 0:
			for voter in voters:
				electorate.append(voter.getResponseData())

		return response_data
