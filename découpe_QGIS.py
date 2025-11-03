import os
import sys
import zipfile
import shutil
import re
from tqdm import tqdm


##############################################################################################
# Commande à exécuter dans CMD :
# "C:\Program Files\QGIS 3.34.3\bin\python-qgis.bat" "C:\Users\jc_12\Documents\1 - Maîtrise\2 - Recherche\QGIS\portraits climatiques\ESPO-G_Telechargement\découpe_QGIS.py"
##############################################################################################


# === Préparation environnement QGIS ===
QGIS_PREFIX_PATH = r"C:\Program Files\QGIS 3.34.3\apps\qgis"
 
os.environ['QGIS_PREFIX_PATH'] = QGIS_PREFIX_PATH
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = os.path.join(QGIS_PREFIX_PATH, 'qt5', 'plugins')


sys.path.append(os.path.join(QGIS_PREFIX_PATH, 'python'))
sys.path.append(os.path.join(QGIS_PREFIX_PATH, 'python', 'plugins'))


# Import des modules QGIS
from qgis.core import (
    QgsApplication, QgsRasterLayer, QgsVectorLayer, QgsProcessingFeatureSourceDefinition,
    QgsProcessingFeedback, QgsProject, QgsCoordinateReferenceSystem
)
import processing
from processing.core.Processing import Processing
from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry

# Initialisation de l'application QGIS
print("🔧 Initialisation de QGIS...")
qgs = QgsApplication([], False)
qgs.initQgis()
print("✅ QGIS initialisé.")

# Initialisation des outils de traitement (processing)
Processing.initialize()
print("✅ Module 'processing' initialisé.")

# === Paramètres ===
chemin_qgis = r"C:/Program Files/QGIS 3.34.3" 
dossier_zip = r"C:\Users\jc_12\Documents\1 - Maîtrise\2 - Recherche\QGIS\portraits climatiques\Téléchargements_ZIP"  # 🔁 Remplace par ton vrai chemin local
shapefile_path = r"C:\Users\jc_12\Documents\1 - Maîtrise\2 - Recherche\QGIS\portraits climatiques\regio_s\regio_s.shp"
dossier_sortie = r"C:\Users\jc_12\Documents\1 - Maîtrise\2 - Recherche\QGIS\portraits climatiques\Découpe_cartes_Portraits"  # 🔁 Remplace par ton vrai chemin local
os.makedirs("temp_extraction", exist_ok=True)

# === Dictionnaire des critères par ZIP ===
from criteres_indicateurs_portraits_copy import criteres_par_zip

print("🔍 Début du script")
print(f"Dossier de travail : {os.getcwd()}")
print(f"Contenu du dossier ZIPS : {os.listdir(dossier_zip)}")
print(f"Clés des critères : {list(criteres_par_zip.keys())}")

print(">>> QGIS initialisé.")

# Pour les traitements (GDAL, clipping, etc.)

sys.path.append(os.path.join(QGIS_PREFIX_PATH, 'python', 'plugins'))

from processing.core.Processing import Processing
Processing.initialize()



# === Boucle sur les ZIP ===
zip_files = [f for f in os.listdir(dossier_zip) if f.endswith(".zip") and f in criteres_par_zip]

print("📁 Fichiers ZIP détectés dans le dossier :", os.listdir(dossier_zip))
print("🔍 Clés de filtrage disponibles :", list(criteres_par_zip.keys()))
print("✅ ZIPs à traiter :", zip_files)


for zip_filename in tqdm(zip_files, desc="📦 Traitement des ZIP"):
    print(f"\n🔍 Traitement du fichier ZIP : {zip_filename}")
    if not zip_filename.endswith(".zip") or zip_filename not in criteres_par_zip:
        continue

    zip_path = os.path.join(dossier_zip, zip_filename)
    base_name = os.path.splitext(zip_filename)[0]
    output_dir = os.path.join(dossier_sortie, base_name)
    os.makedirs(output_dir, exist_ok=True)

    temp_dir = os.path.join("temp_extraction", base_name)
    os.makedirs(temp_dir, exist_ok=True)

    # Décompresser le zip
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        print(f"   ➜ Décompression dans : {temp_dir}")
        zip_ref.extractall(temp_dir)

    # Critères de filtrage
    filtres = criteres_par_zip[zip_filename]
    mots_cles = filtres["recurence"] + filtres["scenario"] + filtres["percentile"] + filtres["periode"]

    # Parcours des TIFF
    for root, _, files in os.walk(temp_dir):
        for f in tqdm(files, desc=f"   🎯 Fichiers TIFF dans {base_name}", leave=False):
            if f.lower().endswith(".tiff") or f.endswith(".tif"):
                if all(any(m.lower() in f.lower() for m in groupe) for groupe in [filtres["recurence"], filtres["scenario"], filtres["percentile"], filtres["periode"]]):
                    tiff_path = os.path.join(root, f)
                    sortie_path = os.path.join(output_dir, f)

                    # Découpage avec le shapefile
                    print(f"      ✂ Découpage du fichier : {f}")
                    processing.run("gdal:cliprasterbymasklayer", {
                        'INPUT': tiff_path,
                        'MASK': shapefile_path,
                        'SOURCE_CRS': None,
                        'TARGET_CRS': None,
                        'NODATA': -9999,
                        'ALPHA_BAND': False,
                        'CROP_TO_CUTLINE': True,
                        'KEEP_RESOLUTION': True,
                        'OUTPUT': sortie_path
                    }, feedback=QgsProcessingFeedback())
                    print(f"      ✅ Fichier sauvegardé : {sortie_path}")

    # Nettoyage
    shutil.rmtree(temp_dir)
    print(f"   🧹 Temporaire supprimé : {temp_dir}")

# Fermer QGIS
print("\n✅ Traitement terminé pour tous les ZIP.")
qgs.exitQgis()
