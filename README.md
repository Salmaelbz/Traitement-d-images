# Fondamentaux du Traitement d'Images — Redimensionnement, Filtres de Convolution, Morphologie et Transformée de Fourier

Ce projet explore les bases du traitement d'images avec OpenCV. Chaque script traite un sujet précis et peut être exécuté indépendamment.

---

## Objectifs et contenu

On part d'une image, on la manipule (redimensionnement), on applique différents filtres (flou, contours), on travaille sur des images binaires avec la morphologie mathématique, et on analyse le contenu fréquentiel avec la transformée de Fourier.

---

## Description des scripts

### Structure des données OpenCV et redimensionnement manuel
`opencv_mat_structure.py`

Présentation des matrices d’images dans OpenCV et redimensionnement manuel.

- Chargement d’une image en niveaux de gris (ou en couleur si le fichier l’est)
- Lecture directe des pixels via la structure `cv::Mat`
- Redimensionnement à la main de 512×512 vers 64×64 en sous-échantillonnant (un pixel tous les N)
- Affichage côte à côte : image originale et image redimensionnée  
- Appel : `python Tp_2/opencv_mat_structure.py`` ou en passant un chemin d’image en argument

**Image par défaut :** `peppers-512.png` (à placer dans le même dossier si absente).

---

### Méthodes de redimensionnement (zoom, interpolation)
`image_resizing.py`

Variantes de redimensionnement d’images (zoom, facteur, interpolation).

Complète le script 1 en explorant d’autres méthodes de redimensionnement fournies par OpenCV.

---

### Filtres de convolution (Gaussian, Sobel, Laplacian)
`convolution_filters.py`

Application de noyaux de convolution sur une image.

- **Gaussian** : flou gaussien via un kernel 3×3
- **Box** : moyenne sur une fenêtre 3×3
- **Sobel X** : contours horizontaux
- **Laplacian** : renforcement des contours
- **Kernels personnalisés** : exemples de filtres maison

Chaque filtre est appliqué avec `cv2.filter2D` puis affiché.  
**Image attendue :** `peppers-512.png` dans le dossier d’exécution.

---

### Morphologie mathématique (érosion, dilatation, ouverture, fermeture)
`morphology_operations.py`

Opérations de morphologie mathématique sur une image binaire.

- Chargement de l’image et seuillage pour obtenir une image binaire
- Élément structurant en forme de croix (3×3)
- Opérations implémentées :
  - **Érosion** : rétrécit les régions blanches
  - **Dilatation** : les agrandit
  - **Ouverture** : érosion puis dilatation (élimine le bruit)
  - **Fermeture** : dilatation puis érosion (combler les trous)
- Calcul de la différence dilatation − érosion (contours morphologiques)

Toutes ces opérations sont implémentées manuellement (boucles) plutôt que via les fonctions OpenCV.

---

### Transformée de Fourier et analyse fréquentielle
`frequency_analysis.py`

Analyse en domaine fréquentiel avec la transformée de Fourier discrète (DFT).

- Calcul de la DFT 2D sur une image en niveaux de gris
- Application de `fftshift` pour mettre la fréquence nulle au centre
- Visualisation du spectre d’amplitude (log pour mieux voir)
- Comparaison du spectre sur une image tournée de 90° pour montrer l’invariance à la rotation dans le domaine fréquentiel

**Images utilisées :** `D1r.pgm`, `D11r.pgm`, `D46r.pgm`, `peppers-512.png` (selon disponibilité dans le code).

---

## Installation des dépendances

```bash
pip install -r requirements.txt
```

ou :

```bash
pip install opencv-python numpy
```

---

## Arborescence du projet

```
TP2_ELBAZ/
├── Tp_2/
│   ├── opencv_mat_structure.py
│   ├── image_resizing.py
│   ├── convolution_filters.py
│   ├── morphology_operations.py
│   └── frequency_analysis.py
├── requirements.txt
└── README.md
```

---

## Informations pratiques

- Place les images test (par ex. `peppers-512.png`) dans `Tp_2/` avant de lancer les scripts.
- Les résultats s’affichent dans des fenêtres OpenCV (appuyer sur une touche pour fermer).

---

**Auteur :** ELBAZ
