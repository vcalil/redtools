import requests
import json
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
		if variables != null:
			myVariables = []
			for count in range(len(variables)):
				myVariables.append(jsonResponseContent[variables[count]])

			return myVariables

		return null

	def postRequest(self, url, headers, data, variables):
		response = requests.post(url, headers=headers, data=data, verify=False)
		jsonResponseContent = json.loads(response.content)
		if variables != null:
			myVariables = []
			for count in range(len(variables)):
				myVariables.append(jsonResponseContent[variables[count]])

			return myVariables

		return null