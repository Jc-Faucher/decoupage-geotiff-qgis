import os
import requests

##############################################################################################
# Commande à exécuter dans CMD :
# pip install requests
# python "C:\Users\jc_12\Documents\1 - Maîtrise\2 - Recherche\QGIS\portraits climatiques\ESPO-G_Telechargement\téléchargement_tiffs_portaits.py"
##############################################################################################


# dossier de destination

output_folder = "C:/Users/jc_12/Documents/1 - Maîtrise/2 - Recherche/QGIS/portraits climatiques/Téléchargements_ZIP"
os.makedirs(output_folder, exist_ok=True)

# liste des URLs des fichiers ZIP à télécharger

zip_urls = [
    "https://portraits.ouranos.ca/donnees/horiz_anom/espog_tg_mean.zip", # Hausse des températures moyennes
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_dlyfrzthw.zip", # Redoux hivernaux - Évènements de gel-dégel
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_tg_mean.zip", # Établissement des moustiques – Moyenne des températures l'été
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_degree_days_above_0.zip", #Établissement des tiques – Degrés-jours au-dessus de 0°C
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_tx_mean.zip", # Températures maximales l'été
    "https://portraits.ouranos.ca/donnees/horiz_anom/espog_tn_days_above_20.zip", # Hausse des nuits très chaudes
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_heat_spell_frequency_class1.zip", # Nombre de vagues de chaleur
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_tx_max.zip", # Jour le plus chaud
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_tn_mean.zip", # Températures minimales l'hiver
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_tn_min.zip", # Nuit la plus froide
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_rx1day.zip", # Pluies intenses 
    "https://portraits.ouranos.ca/donnees/horiz_anom/espog_prcptot.zip", # Variation des précipitations neigeuses l'hiver
    "https://portraits.ouranos.ca/donnees/wl_abs/verglas_prfr_events_longer_6h.zip", # Nombre d'épisodes de pluies verglacantes de longue durée
    "https://portraits.ouranos.ca/donnees/horiz_abs/espog_dry_spell_frequency.zip" # Périodes sèches


]

# fonction pour télécharger

def download_zip_files(zip_urls, output_folder):
    for url in zip_urls:
        file_name = os.path.join(output_folder, os.path.basename(url))
        response = requests.get(url, stream=True)

        if response.status_code == 200:
            with open(file_name, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Téléchargement réussi : {file_name}")
        else:
            print(f"Échec du téléchargement : {url}")

download_zip_files(zip_urls, output_folder)




