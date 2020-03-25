from Bibliotheque import Bibliotheque
from Documents import Documents
from Volumes import Volumes
from Livres import Livres
from Adherents import Adherents

if __name__ == "__main__":
    pass

    biblio1 = Bibliotheque(1)
    # biblio1.creer_bibliotheque(biblio1.getId_bibliotheque())
    # biblio1.liste_bibliotheques()
    
    # biblio.liste_bibliotheques()
    
    doc1 = Documents(1,'Harry Potter à l ecole des sorciers',biblio1.getId_bibliotheque())
    
    doc2 = Documents(2,'Harry Potter et la Chambre des secrets',biblio1.getId_bibliotheque())
    doc3 = Documents(3,'Harry Potter et le Prisonnier d Azkaban',biblio1.getId_bibliotheque())
    doc4 = Documents(4,'Harry Potter et la Coupe de feu',biblio1.getId_bibliotheque())
    doc5 = Documents(5,'Harry Potter et l Ordre du Phénix ',biblio1.getId_bibliotheque())
    doc6 = Documents(6,'Harry Potter et le Prince de sang-mêlé',biblio1.getId_bibliotheque())
    doc7 = Documents(7,'Harry Potter et les Reliques de la Mort',biblio1.getId_bibliotheque())
    
    # doc1.creer_document(doc1.getId_document(),doc1.getId_bibliotheque(),doc1.getTitre())
    # doc2.creer_document(doc2.getId_document(),doc2.getId_bibliotheque(),doc2.getTitre())
    # doc3.creer_document(doc3.getId_document(),doc3.getId_bibliotheque(),doc3.getTitre())
    # doc4.creer_document(doc4.getId_document(),doc4.getId_bibliotheque(),doc4.getTitre())
    # doc5.creer_document(doc5.getId_document(),doc5.getId_bibliotheque(),doc5.getTitre())
    # doc6.creer_document(doc6.getId_document(),doc6.getId_bibliotheque(),doc6.getTitre())
    # doc7.creer_document(doc7.getId_document(),doc7.getId_bibliotheque(),doc7.getTitre())

    # doc1.liste_documents()
    
    vol1 = Volumes(1,'JK Rolling',doc1.getId_document(),doc1.getTitre(),biblio1.getId_bibliotheque())
    vol2 = Volumes(2,'JK Rolling',doc2.getId_document(),doc2.getTitre(),biblio1.getId_bibliotheque())
    vol3 = Volumes(3,'JK Rolling',doc3.getId_document(),doc3.getTitre(),biblio1.getId_bibliotheque())
    vol4 = Volumes(4,'JK Rolling',doc4.getId_document(),doc4.getTitre(),biblio1.getId_bibliotheque())
    vol5 = Volumes(5,'JK Rolling',doc5.getId_document(),doc5.getTitre(),biblio1.getId_bibliotheque())
    vol6 = Volumes(6,'JK Rolling',doc6.getId_document(),doc6.getTitre(),biblio1.getId_bibliotheque())
    vol7 = Volumes(7,'JK Rolling',doc7.getId_document(),doc7.getTitre(),biblio1.getId_bibliotheque())
    
    # vol1.creer_volume(vol1.getId_volume(),vol1.getId_document(),vol1.getAuteur())
    # vol2.creer_volume(vol2.getId_volume(),vol2.getId_document(),vol2.getAuteur())
    # vol3.creer_volume(vol3.getId_volume(),vol3.getId_document(),vol3.getAuteur())
    # vol4.creer_volume(vol4.getId_volume(),vol4.getId_document(),vol4.getAuteur())
    # vol5.creer_volume(vol5.getId_volume(),vol5.getId_document(),vol5.getAuteur())
    # vol6.creer_volume(vol6.getId_volume(),vol6.getId_document(),vol6.getAuteur())
    # vol7.creer_volume(vol7.getId_volume(),vol7.getId_document(),vol7.getAuteur())

    # vol1.liste_volumes()
    
    liv1 = Livres(1,vol1.getId_volume(),vol1.getAuteur(),doc1.getId_document(),doc1.getTitre(),biblio1.getId_bibliotheque())
    liv2 = Livres(2,vol2.getId_volume(),vol2.getAuteur(),doc2.getId_document(),doc2.getTitre(),biblio1.getId_bibliotheque())
    liv3 = Livres(3,vol3.getId_volume(),vol3.getAuteur(),doc3.getId_document(),doc3.getTitre(),biblio1.getId_bibliotheque())
    liv4 = Livres(4,vol4.getId_volume(),vol4.getAuteur(),doc4.getId_document(),doc4.getTitre(),biblio1.getId_bibliotheque())
    liv5 = Livres(5,vol5.getId_volume(),vol5.getAuteur(),doc5.getId_document(),doc5.getTitre(),biblio1.getId_bibliotheque())
    liv6 = Livres(6,vol6.getId_volume(),vol6.getAuteur(),doc6.getId_document(),doc6.getTitre(),biblio1.getId_bibliotheque())
    liv7 = Livres(7,vol7.getId_volume(),vol7.getAuteur(),doc7.getId_document(),doc7.getTitre(),biblio1.getId_bibliotheque())
    
    # liv1.creer_livre(liv1.getId_livre(),liv1.getId_volume())
    # liv2.creer_livre(liv2.getId_livre(),liv2.getId_volume())
    # liv3.creer_livre(liv3.getId_livre(),liv3.getId_volume())
    # liv4.creer_livre(liv4.getId_livre(),liv4.getId_volume())
    # liv5.creer_livre(liv5.getId_livre(),liv5.getId_volume())
    # liv6.creer_livre(liv6.getId_livre(),liv6.getId_volume())
    # liv7.creer_livre(liv7.getId_livre(),liv7.getId_volume())

    # liv1.liste_livres()
    
    adhe1 = Adherents(1,'Martin','Paul',True,'2020-01-01',biblio1.getId_bibliotheque())
    adhe2 = Adherents(2,'Durand','Henry',True,'2020-01-10',biblio1.getId_bibliotheque())
    adhe3 = Adherents(3,'Dupond','Jacques',True,'2020-01-20',biblio1.getId_bibliotheque())
    
    # adhe1.creer_adherent(adhe1.getId_adherent(),adhe1.getId_bibliotheque(),adhe1.getNom(),adhe1.getPrenom(),adhe1.getInscrit(),adhe1.getDate())
    # adhe2.creer_adherent(adhe2.getId_adherent(),adhe2.getId_bibliotheque(),adhe2.getNom(),adhe2.getPrenom(),adhe2.getInscrit(),adhe2.getDate())
    # adhe3.creer_adherent(adhe3.getId_adherent(),adhe3.getId_bibliotheque(),adhe3.getNom(),adhe3.getPrenom(),adhe3.getInscrit(),adhe3.getDate())
    
    # adhe1.liste_adherents()
    liste_livres = []
    liste_livres = liv1.liste_livres()
    
    for i , j in enumerate(liste_livres) :
        print(j.getId_livre())
    
    