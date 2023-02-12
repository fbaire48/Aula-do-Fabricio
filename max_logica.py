
class Lista:
	#remove/pop
	def remover(self):
		metodos=['append','clear','copy','count','extend','index','insert','pop','remove','reverse','sort']


		palavra=str(input())



		























		posicao_da_palavra=0


























		for elemento in range(0,len(metodos)):
			if metodos[elemento]==palavra:
				posicao_da_palavra=elemento

























		


		metodos=metodos[0:posicao_da_palavra]+metodos[posicao_da_palavra+1:]

		print(metodos)
	#remove/pop
	def remover_2(self):
		metodos=['append','clear','copy','count','extend','index','insert','pop','remove','reverse','sort']


		
		metodos_antes_dele=[]



		metodos_depois_dele=[]











		




		








		posicao_do_excluido=0




		for elemento in range(0,len(metodos)):
			if metodos[elemento]=='count':
				posicao_do_excluido=elemento







		for elemento in range(0,len(metodos)):
			if elemento<posicao_do_excluido:
				metodos_antes_dele=metodos_antes_dele+[metodos[elemento]]


			if elemento>posicao_do_excluido:
				metodos_depois_dele=metodos_depois_dele+[metodos[elemento]]



		metodos=metodos_antes_dele+metodos_depois_dele


		print(metodos)
























	#clear
	def remover_3(self):
		metodos=['append','clear','copy','count','extend','index','insert','pop','remove','reverse','sort']























		#metodos=[]

		#metodos=metodos[0:0]+metodos[0+len(metodos):]

		print(metodos)



















class Dicionario:

	def dicionario(self):
		metodos=['clear','pop','popitem','copy','keys','values','get','items','setdefault','update']
	
	def sort(self):
		dicionario={'nome':'nicolas','cidade':'marica','letra':'h'}



			

		lista_keys=[]

		dicionario_final={}	


		for palavra in dicionario:
			lista_keys=lista_keys+[palavra]



		for foco_e_espectro in range(0,len(lista_keys)):
			for participantes_da_linha in range(0,len(lista_keys)):
				if lista_keys[foco_e_espectro]<lista_keys[participantes_da_linha]:
					maior=lista_keys[participantes_da_linha]
					menor=lista_keys[foco_e_espectro]

					lista_keys[foco_e_espectro]=maior
					lista_keys[participantes_da_linha]=menor


		for palavra in lista_keys:
			dicionario_final[palavra]=dicionario[palavra]	


		#print(dicionario_final)
		
		

	


















	def copy(self):
	
		metodos=['clear','pop','popitem','copy','keys','values','get','items','setdefault','update']



		
		dicionario={'nome':'nicolas','cidade':'marica','letra':'h'}
		






		dicionario_copy={}




		for palavra in dicionario:
			key=palavra
			value=dicionario[palavra]
			dicionario_copy[key]=value


		print(dicionario_copy)

























	def remover(self):

		dicionario={'nome':'nicolas','cidade':'marica','letra':'h'}









		lista_keys=[]







		dicionario_final={}




		for palavra in dicionario:
			lista_keys=lista_keys+[palavra]


		



		for palavra in lista_keys:
			if palavra !='cidade':

				value=dicionario[palavra]








				dicionario_final[palavra]=value




		print(dicionario_final)


#a=Lista().remover_2()
#b=Lista().remover()
#c=Lista().remover_3()
#d=Dicionario().sort()
#e=Dicionario().copy()
#f=Dicionario().remover()
