class Atividades():
	#Atividade 1
	def media(self):
		lista=[1,2,3,4,5]
		media=sum(lista)/len(lista)
		print(media)
	#Atividade 2 (metodo 1)
	def metodo_intuitivo(self):
		lista=['c','m','b']
		for foco_e_espectro in range(0,len(lista)):
			for participantes_da_lista in range(0,len(lista)):
				if lista[foco_e_espectro]>lista[participantes_da_lista]:
					maior=lista[foco_e_espectro]
					menor=lista[participantes_da_lista]
					lista[foco_e_espectro]=menor
					lista[participantes_da_lista]=maior
		lista.reverse()
		print(lista)
	#Atividade 3 (metodo 2)
	def auto_inverte(self):
		lista=['ceara','maranhao','bahia']
		for foco_e_espectro in range(0,len(lista)):
			for participantes_da_lista in range(0,len(lista)):
				if lista[foco_e_espectro]<lista[participantes_da_lista]:
					maior=lista[participantes_da_lista]
					menor=lista[foco_e_espectro]
					lista[foco_e_espectro]=maior
					lista[participantes_da_lista]=menor
		print(lista)
#a=Atividades().media()
#b=Atividades().metodo_intuitivo()
#c=Atividades().auto_inverte()
