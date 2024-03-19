#Ideia: criar um algoritmo que leia uma sequencia de DNA e um padrão de enzima de 
#restrição e retorne todos os fragmentos advindos do corte. Os fragmentos não
#consideram o padrão da enzima nem seu padrão real de corte, sendo impressos sem
#ela no momento.

import random

#Essa função cria uma sequência de DNA aleatória de tamanho n
def gerar_sequencia_dna(tamanho):
  nucleotideos = ['A', 'T', 'C', 'G']
  sequencia_dna = ''.join(random.choice(nucleotideos) for _ in range(tamanho))

  return sequencia_dna

seq_DNA = gerar_sequencia_dna(1000)
print("A sequência de DNA é:", seq_DNA)

#Essa função cria uma sequência de enzima de restrição aleatória de tamanho n
def gerar_padrão_de_busca(tamanho):
  nucleotideos = ['A', 'T', 'C', 'G']
  padrao_de_busca = ''.join(random.choice(nucleotideos) for _ in range(tamanho))

  return padrao_de_busca

padrao_enzima = gerar_padrão_de_busca(6)
print("O padrão da enzima de restrição é:", padrao_enzima)

#Essa função busca pelo padrão fornecido na sequência de DNA 
# e divide a sequencia a partir do mesmo
def separar_fragmentos(seq_DNA, padrao_enzima):
  fragmentos = []
  posicao = seq_DNA.find(padrao_enzima)
  posicao_anterior = 0

  while posicao != -1:
    fragmento = seq_DNA[posicao_anterior:posicao]
    fragmentos.append(fragmento)
    posicao_anterior = posicao + len(padrao_enzima)
    posicao = seq_DNA.find(padrao_enzima, posicao + 1)

  fragmento_final = seq_DNA[posicao_anterior:]
  fragmentos.append(fragmento_final)
  
  return fragmentos

print("Os fragmentos encontrados são:")
fragmentos = separar_fragmentos(seq_DNA,padrao_enzima)
#for fragmento in fragmentos:
  #print(fragmento)

for i, fragmento in enumerate(fragmentos):
  print(fragmento)
  if i != len(fragmentos) - 1:
    print()
