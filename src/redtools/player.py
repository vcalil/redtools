import requests
import json


class RedPlayer:
	def __init__(self):
    		self.data = []

	def readJSON(self, rota):
		with open(rota) as f:
			jsonFile = json.load(f)

		return jsonFile

	def getRequest(self, url, headers, data, variables):
		response = requests.get(url, headers=headers, data=data, verify=False)
		jsonResponseContent = json.loads(response.content)
		for count in range(variables):
			myVariables[count] = jsonResponseContent[variables[count]]
			
		return myVariables

	def postRequest(self, url, headers, data, variables):
		response = requests.post(url, headers=headers, data=data, verify=False)
		jsonResponseContent = json.loads(response.content)
		for count in range(variables):
			myVariables[count] = jsonResponseContent[variables[count]]
		
		return myVariables