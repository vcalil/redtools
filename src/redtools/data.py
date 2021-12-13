import sys
import random
import requests
import json
import re
from html.parser import HTMLParser
import bs4 as bs
import time
import urllib3

class GenerateData:
	def __init__(self):
    		self.data = []

	def geraPersona(quantidade):
		urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

		domain="https://rogertakemiya.com.br"
		host = "rogertakemiya.com.br"
		endpoint = "/lab/php-snippets/gerador-de-pessoas.php?gen=1&tipos=0&sobrenome=1&rg=1&cpf=1&dtnasc=1&endereco=1&numero=1&bairro=1&cep=1&cidade=1&estado=1&estadocivil=0&fixo=0&celular=0&email=0&_=163777445829"

		my_headers = {"Host":host, "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29"}
		proxies = {"http":"http://127.0.0.1:8080", "https":"http://127.0.0.1:8080"}

		url = domain + endpoint


		arquivo1 = open('Nome_Wordlist.txt', 'a')
		arquivo2 = open('Sobrenome_Wordlist.txt', 'a')
		arquivo3 = open('RG_Wordlist.txt', 'a')
		arquivo4 = open('CPF_Wordlist.txt', 'a')
		arquivo5 = open('DtNasc_Wordlist.txt', 'a')
		arquivo6 = open('Logradouro_Wordlist.txt', 'a')
		arquivo7 = open('Localidade_Wordlist.txt', 'a')
		arquivo8 = open('CEP_Wordlist.txt', 'a')
		arquivo9 = open('Nr_Wordlist.txt', 'a')
		arquivo10 = open('Bairro_Wordlist.txt', 'a')
		arquivo11 = open('Cidade_Wordlist.txt', 'a')
		arquivo12 = open('Estado_Wordlist.txt', 'a')
		arquivo13 = open('Endereco_Wordlist.txt', 'a')
		arquivo14 = open('Email_Wordlist.txt', 'a')
		arquivo15 = open('Password_Wordlist.txt', 'a')

		for count in range(quantidade):
		    print("[+]Creating the Fake People ...")
		    r = requests.get(url,headers=my_headers,proxies=proxies,verify=False)
		    file = bs.BeautifulSoup(r.content, "lxml")
		    res = r.text
		    time.sleep(5)
		    if r.status_code == 200:
		        Nome = re.match(r'.*<td>Nome</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo1.write(Nome + '\n')
		        Sobrenome = re.match(r'.*<td>Sobrenome</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo2.write(Sobrenome + '\n')
		        Email = Sobrenome + "." + Nome + str(random.randrange(1970,2021)) + "@gmail.com"
		        arquivo14.write(Email + '\n')
		        Password = Sobrenome + "@" + str(random.randrange(1000,9999)) + "$"
		        arquivo15.write(Password + '\n')
		        RG = re.match(r'.*<td>RG</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo3.write(RG + '\n')
		        CPF = re.match(r'.*<td>CPF</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo4.write(CPF + '\n')
		        DtNasc = re.match(r'.*<td>Dt\. Nasc</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo5.write(DtNasc + '\n')
		        Endereco = re.match(r'.*<td>Endereço</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        Nr = re.match(r'.*<td>Número</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        Bairro = re.match(r'.*<td>Bairro</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        Cidade = re.match(r'.*<td>Cidade</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        Estado = re.match(r'.*<td>Estado</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        Logradouro = Endereco + ", " + Nr + " - " + Bairro + ", " + Cidade + "-" +Estado
		        Localidade = Cidade + " - " + Estado
		        arquivo6.write(Logradouro + '\n')
		        arquivo7.write(Localidade + '\n')
		        arquivo9.write(Nr + '\n')
		        arquivo10.write(Bairro + '\n')
		        arquivo11.write(Cidade + '\n')
		        arquivo12.write(Estado + '\n')
		        arquivo13.write(Endereco + '\n')
		        CEP = re.match(r'.*<td>CEP</td><td><input type=\'text\' value=\'([^\']+)\'.*', res).group(1)
		        arquivo8.write(CEP + '\n')    
    
		arquivo1.close()
		arquivo2.close()
		arquivo3.close()
		arquivo4.close()
		arquivo5.close()
		arquivo6.close()
		arquivo7.close()
		arquivo8.close()
		arquivo9.close()
		arquivo10.close()
		arquivo11.close()
		arquivo12.close()
		arquivo13.close()
		arquivo14.close()
		arquivo15.close()

	def _calculaDVPJ(numeroCNPJ,formatacao):
	  validador = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5, 6]
	  # calcula dígito 1 e acrescenta ao total
	  somatoria1 = sum(indiceCNPJ * indiceValidador for indiceCNPJ, indiceValidador in zip(reversed(numeroCNPJ), validador))
	  d1 = 11 - somatoria1 % 11
	  if d1 >= 10:
	    d1 = 0
	  numeroCNPJ.append(d1)
	  # idem para o dígito 2
	  somatoria2 = sum(indiceCNPJ * indiceValidador for indiceCNPJ, indiceValidador in zip(reversed(numeroCNPJ), validador))
	  d2 = 11 - somatoria2 % 11
	  if d2 >= 10:
	    d2 = 0
	  numeroCNPJ.append(d2)
	  if formatacao:
	    return "%d%d.%d%d%d.%d%d%d/%d%d%d%d-%d%d" % tuple(numeroCNPJ)
	  else:
	    return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(numeroCNPJ)

	def gerarNumerosPJ(quantidadeCNPJs, formatacao):
	  nomeDoArquivo = str(quantidadeCNPJs)+'_CNPJs_' +'.txt'
	  arquivo = open(nomeDoArquivo, 'w')

	  for integer in range(int(quantidadeCNPJs)):
	    numeroCNPJ = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
	    arquivo.write(_calculaDVPJ(numeroCNPJ,formatacao)+'\n')

	  arquivo.close()

	def _calculaDVPF(numeroCPF,formatacao):
	  validador = [10, 9, 8, 7, 6, 5, 4, 3, 2]
	  # calcula dígito 1 e acrescenta ao total
	  somatoria1 = sum(indiceCPF * indiceValidador for indiceCPF, indiceValidador in zip(numeroCPF, validador))
	  d1 = 11 - somatoria1 % 11
	  if d1 >= 10:
	    d1 = 0
	  numeroCPF.append(d1)
	  # idem para o dígito 2
	  validador.insert(0,11)
	  somatoria2 = sum(indiceCPF * indiceValidador for indiceCPF, indiceValidador in zip(numeroCPF, validador))
	  d2 = 11 - somatoria2 % 11
	  if d2 >= 10:
	    d2 = 0
	  numeroCPF.append(d2)
	  if formatacao:
	    return "%d%d%d.%d%d%d.%d%d%d-%d%d" % tuple(numeroCPF)
	  else:
	    return "%d%d%d%d%d%d%d%d%d%d%d%d%d%d" % tuple(numeroCPF)

	def gerarNumerosPF(quantidadeCPFs, formatacao, estado):
	  nomeDoArquivo = str(quantidadeCPFs)+'_CPFs_' +'.txt'
	  arquivo = open(nomeDoArquivo, 'w')

	  for integer in range(int(quantidadeCPFs)):
	    numeroCPF = [random.randrange(10) for i in range(8)] 
	    if estado == 'SP':
	      numeroCPF += [8]
	    elif estado == 'RJ':
	      numeroCPF += [9]
	    arquivo.write(_calculaDVPF(numeroCPF,formatacao)+'\n')

	  arquivo.close()
