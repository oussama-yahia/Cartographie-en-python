import folium
import webbrowser
import tkinter as tk
from geopy.geocoders import Nominatim

# Fonction appelée lorsque le bouton est cliqué
def afficher_carte():
    ville = ville_entree.get()
    geolocator = Nominatim(user_agent="my-app")
    location = geolocator.geocode(ville)

    # Créer une carte centrée sur la ville
    ma_carte = folium.Map(location=[location.latitude, location.longitude], zoom_start=12)

    # Ajouter un marqueur à la carte
    folium.Marker(location=[location.latitude, location.longitude], popup=ville).add_to(ma_carte)

    # Ajouter des tuiles à la carte
    folium.TileLayer('Stamen Terrain').add_to(ma_carte)
    folium.TileLayer('Stamen Toner').add_to(ma_carte)
    folium.TileLayer('Stamen Water Color').add_to(ma_carte)
    folium.TileLayer('cartodbpositron').add_to(ma_carte)
    folium.TileLayer('cartodbdark_matter').add_to(ma_carte)

    # Ajouter une couche de contrôle pour choisir les tuiles affichées
    folium.LayerControl().add_to(ma_carte)

    # Enregistrer la carte en tant que fichier HTML
    ma_carte.save('ma_carte.html')
    
    # Ouvrir le fichier HTML dans le navigateur par défaut
    webbrowser.open_new_tab('ma_carte.html')

# Créer la fenêtre
fenetre = tk.Tk()
fenetre.title("Carte de la ville")
fenetre.geometry("400x150")

# Ajouter un champ de saisie pour le nom de la ville
ville_label = tk.Label(fenetre, text="Nom de la ville :")
ville_label.pack()
ville_entree = tk.Entry(fenetre)
ville_entree.pack()

# Ajouter un bouton pour afficher la carte
bouton_afficher = tk.Button(fenetre, text="Afficher la carte", command=afficher_carte)
bouton_afficher.pack()

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
# Récupérer les informations sur la ville
ville = ville_entree.get()
geolocator = Nominatim(user_agent="my-app")
location = geolocator.geocode(ville)

# Afficher les informations sur la ville dans une boîte de dialogue
tk.messagebox.showinfo("Informations sur la ville", f"Nom : {ville}\nLatitude : {location.latitude}\nLongitude : {location.longitude}\nPays : {location.raw['display_name'].split(',')[-1].strip()}")
