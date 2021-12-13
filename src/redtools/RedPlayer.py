import requests


class RedPlayer:

	def readJSON(rota):
		with open(rota) as f:
    		jsonFile = json.load(f)
    	return jsonFile

    def getRequest(url, headers, data, variables):
		response = requests.get(url, headers=headers, data=data, verify=False)

		jsonResponseContent = json.loads(response.content)
		myVariable = jsonResponseContent[variable]

		return myVariable


	def postRequest(url, headers, data, variables):
		response = requests.post(url, headers=headers, data=data, verify=False)

		jsonResponseContent = json.loads(response.content)
		for in range(variables):
			myVariable
		myVariable = jsonResponseContent[variable]

		return myVariable