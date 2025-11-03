# Découpage automatisé des projections climatiques (QGIS + Python)
Ce dépôt contient le code Python utilisé dans le cadre de mon mémoire de maîtrise pour automatiser le téléchargement et le découpage de fichiers GeoTIFF climatiques à l’aide de QGIS et d’un shapefile régional du Québec.

---

## Description des fichiers

| Fichier | Description |
|----------|--------------|
| **téléchargement_tiffs_portaits.py** | Script permettant de télécharger les dossiers ZIP contenant des fichiers .TIFF de projections climatiques provenant de https://portraits.ouranos.ca/donnees/
| **découpe_QGIS.py** | Script principal. Initialise QGIS, lit les fichiers ZIP contenant les rasters climatiques et effectue le découpage selon un shapefile. |
| **criteres_indicateurs_portraits.py** | Dictionnaire des critères par fichier ZIP (scénarios, périodes, récurrences, etc.). |
| **regio_s.shp** *(non inclus)* | Shapefile du Québec utilisé pour découper les rasters (exclu pour taille). |
| **ZIPS/** *(non inclus)* | Dossier contenant les fichiers ZIP climatiques téléchargés depuis ESPO-G. |


---

Données originales : [Portraits climatiques (Ouranos)](https://portraits.ouranos.ca/donnees/)

Analyse réalisée dans le cadre du mémoire de maîtrise de Jean-Cédric Faucher, 2025.
