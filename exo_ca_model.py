import os

class Contact(object):
	"""Cette CLASSE definit un contact"""
	def __init__(self,nom,prenom):
		self.nom=nom
		self.prenom=prenom
		self.num_tel=None
	def __repr__(self):
		toto=self.nom+" "+self.prenom
		if self.num_tel:
			toto+= " "+self.num_tel
		return toto

class Indexation (object):
	"""Cette CLASSE definit l'index"""

	def __init__(self,lettre):
		self.lettre=lettre
		self.liste_contacts=[]

	def ajouter(self,contact):
		#import pdb;pdb.set_trace()
		self.liste_contacts.append (contact)

	def __repr__(self):
#		liste_chaine=[]
#		if self.liste_contacts:
		liste_chaine=[self.lettre, "="]
		for contact in self.liste_contacts:
#			liste_chaine.append(contact.__repr__())
			liste_chaine.append("  %s"% contact)
		liste_chaine.append('----------------')
		return os.linesep.join(liste_chaine)

class Carnet_adresse(object):
	"""Cette classe definit le carnet d'adresse"""

	def __init__(self):
		self.liste_index=[]
		alpha="abcdefghijklmnopqrstuvwxyz".upper()
		for lettre in alpha:
			self.liste_index.append (Indexation(lettre))
	
	def ajouter(self,contact):
		"""Ajout d un contact"""
		lettre=contact.nom[0]
		foo=self.getindex(lettre)
		foo.ajouter(contact)

	def rechercher(self,nom):
		contacts=[]
		lettre=nom[0]
		toto=self.getindex(lettre)
		for c in toto.liste_contacts:
			if nom==c.nom[:len(nom)]:
				contacts.append(c)
#                cc = [c for c in toto.liste_contacts if nom==c.nom[:len(nom)]]
		return contacts

	def getindex(self,lettre):
		var=None
		for index in self.liste_index:
			if lettre==index.lettre:
				var=index
		return var

	def __str__(self):
		liste_chaine = []
		for i in self.liste_index:
			if bool(i.liste_contacts)==True:
				liste_chaine.append("%s" % i)
		return os.linesep.join(liste_chaine)
				
		


#if __name__=="__main__":
#	a=index("A")
#	nom=raw_input("Nom:")
#	prenom=raw_input("Prenom")


#        contacts = CA1.rechercher("Gen")
#	indexG=CA1.liste_index[6]

#        print CA1





