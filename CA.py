import os
repertoire={}


def Ajout_contact(nom,prenom,num_tel=None):
	contact={"prenom":prenom,"nom":nom}
	index=nom[0]
	if num_tel:
		contact["telephone"]=num_tel
	if index not in repertoire:
		repertoire[index]=[]
	repertoire[index].append(contact)


#repertoire.sort(cmp(repertoire.keys(),[]))
def afficher():
	import pprint
	pp=pprint.PrettyPrinter()
	texte = format_txt()
	pp.pprint(texte)

def sauvegarder():
	fichier=open("carnet_adresse.txt","w")
	texte=format_txt()
	fichier.write(texte)

def format_txt():
	texte=[]
	for index in repertoire.keys():
		list_contact = repertoire[index]
		for contact in list_contact:       
			texte.append("%(nom)s - %(prenom)s - %(telephone)s"%contact)
	return os.linesep.join(texte)


if __name__ == "__main__":
	Ajout_contact("Dupont","Robert","02 99 50 60 11")
	Ajout_contact("Durant","Marc","02 99 50 30 40")
	Ajout_contact("Richard","Johann","02 99 60 40 50")
	Ajout_contact("Pansard","Elodie","02 99 30 50 60")
	format_txt()
	format_txt()
	afficher()
	sauvegarder()
