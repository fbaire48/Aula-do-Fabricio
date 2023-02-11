class Dia_um:
	def media(self,pedido):
		self.pedido=pedido

		espaco=[]


		for identificacao in range(1,self.pedido+1):
			numero=float(input())
			espaco.append(numero)


		media=sum(espaco)/len(espaco)

		print(media)
	






















	#Metodo intuitivo
	def ordem_alfabetica(self):
		letras=['c','m','b']




	


		for foco_e_espectro in range(0,len(letras)):
			for participantes_da_linha in range(0,len(letras)):
				if letras[foco_e_espectro]>letras[participantes_da_linha]:
					maior=letras[foco_e_espectro]
					menor=letras[participantes_da_linha]

					letras[foco_e_espectro]=menor
					letras[participantes_da_linha]=maior




		letras_final=[]





		for caractere in letras:
			letras_final=[caractere]+letras_final



		print(letras_final)
	

	




















	#Metodo auto-inverte
	def ordem_alfabetica_cidades(self):
		cidades=['ceara','maranhao','bahia']







		for foco_e_espectro in range(0,len(cidades)):
			for participantes_da_linha in range(0,len(cidades)):
				if cidades[foco_e_espectro]<cidades[participantes_da_linha]:
					maior=cidades[participantes_da_linha]
					menor=cidades[foco_e_espectro]

					cidades[foco_e_espectro]=maior
					cidades[participantes_da_linha]=menor





		print(cidades)

#a=Dia_um().media(5)
#b=Dia_um().ordem_alfabetica()
#c=Dia_um().ordem_alfabetica_cidades()

