import exo_ca_view
import exo_ca_model


def main():

    contact1=exo_ca_model.Contact("Richard","Johann")
    contact2=exo_ca_model.Contact("Lerouzic","Bertrand")
    contact3=exo_ca_model.Contact("Gendrot","Fabrice")
    contact4=exo_ca_model.Contact("Gendrot","Frederic")
    contact5=exo_ca_model.Contact("Gentric","Pascal")

    CA1=exo_ca_model.Carnet_adresse()
    CA1.ajouter(contact1)
    CA1.ajouter(contact2)
    CA1.ajouter(contact3)
    CA1.ajouter(contact4)
    CA1.ajouter(contact5)
    
    root, app = exo_ca_view.main()
    root.mainloop()

if __name__ == '__main__':
    main() 
    import pdb;pdb.set_trace()    
  
