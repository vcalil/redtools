import sys
import random

def _calculaDV(numeroCNPJ,formatacao):
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

def gerarNumeros(quantidadeCNPJs, formatacao):
  nomeDoArquivo = str(quantidadeCNPJs)+'_CNPJs_' +'.txt'
  arquivo = open(nomeDoArquivo, 'w')

  for integer in range(int(quantidadeCNPJs)):
    numeroCNPJ = [random.randrange(10) for i in range(8)] + [0, 0, 0, 1]
    arquivo.write(_calculaDV(numeroCNPJ,formatacao)+'\n')

  arquivo.close()