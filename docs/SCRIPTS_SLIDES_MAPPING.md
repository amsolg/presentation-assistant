# Mapping Complet Scripts → Slides → Templates

## Vue d'Ensemble

Ce document de référence liste les 9 scripts disponibles dans `presentation_builder/`, les slides Premier Tech supportées par chaque script, et les chemins vers les templates correspondants dans `template_analysis_output/`.

## Architecture

- **9 Scripts Spécialisés** : Chaque script gère un type de contenu spécifique
- **57 Slides Premier Tech** : Templates authentiques avec styles préservés
- **Templates JSON** : Analyses structurées dans `template_analysis_output/`

---

## 1. presentation_builder.py

**Rôle :** Orchestrateur principal de l'architecture JSON
**Fonction :** Coordonne tous les autres scripts et gère le workflow global

### Slides Directement Gérées
- **Slide 11** (index 10) - Page titre principale
  - Template : `template_analysis_output/slide_11.json`
  - Usage : Slide titre automatique pour chaque présentation

- **Slide 57** (index 56) - Monogramme Premier Tech
  - Template : `template_analysis_output/slide_57.json`
  - Usage : Slide de fermeture automatique (signature corporate)

### Responsabilités
- Parse la configuration JSON
- Orchestre l'appel aux autres scripts
- Gère la structure de sortie `presentations/[sujet]/[audience]/`
- Ajoute automatiquement slides titre et fermeture

---

## 2. navigation_builder.py

**Rôle :** Construction de tables des matières et navigation
**Fonction :** Crée des tables des matières structurées pour la navigation dans la présentation

### Slides Supportées
- **Slide 13** (index 12) - Table des matières
  - Template : `template_analysis_output/slide_13.json`
  - Usage : Navigation principale avec 3 sections et sous-sections
  - Structure : Titre + 3 colonnes de navigation

---

## 3. section_header_builder.py

**Rôle :** Création de pages de section et titres de transition
**Fonction :** Marque les transitions entre sections majeures de la présentation

### Slides Supportées
- **Slide 15** (index 14) - Titre de section bleu
  - Template : `template_analysis_output/slide_15.json`
  - Usage : Transitions majeures, séparations importantes
  - Style : "major" - Pour leaders et managers

- **Slide 16** (index 15) - Titre de section blanc
  - Template : `template_analysis_output/slide_16.json`
  - Usage : Transitions modérées, sous-sections
  - Style : "moderate" - Pour audiences mixtes

---

## 4. simple_message_builder.py

**Rôle :** Messages courts et mots-clés
**Fonction :** Affiche des messages simples, mots-clés ou énoncés courts

### Slides Supportées
- **Slide 17** (index 16) - Court énoncé
  - Template : `template_analysis_output/slide_17.json`
  - Usage : Message principal centré
  - Structure : Un bloc de texte principal

- **Slide 18** (index 17) - Mots-clés & Mots complémentaires
  - Template : `template_analysis_output/slide_18.json`
  - Usage : Mots-clés avec texte complémentaire
  - Structure : Shape 0 = mots-clés, Shape 1 = complément

- **Slide 19** (index 18) - Mots-clés & Court énoncé
  - Template : `template_analysis_output/slide_19.json`
  - Usage : Mots-clés avec message court
  - Structure : Shape 0 = mots-clés, Shape 1 = message

---

## 5. statistics_builder.py

**Rôle :** Affichage de statistiques et métriques
**Fonction :** Présente des données chiffrées avec mise en forme visuelle

### Slides Supportées
- **Slide 22** (index 21) - 2 statistiques ligne bleue
  - Template : `template_analysis_output/slide_22.json`
  - Usage : Deux métriques principales avec séparateur bleu

- **Slide 23** (index 22) - 2 statistiques ligne grise
  - Template : `template_analysis_output/slide_23.json`
  - Usage : Deux métriques avec séparateur gris

- **Slide 24** (index 23) - 3 statistiques & Mots-clés
  - Template : `template_analysis_output/slide_24.json`
  - Usage : Trois statistiques avec mots-clés associés

- **Slide 25** (index 24) - 4 statistiques & Mots-clés
  - Template : `template_analysis_output/slide_25.json`
  - Usage : Quatre statistiques avec descriptions

- **Slide 26** (index 25) - 4 statistiques & Mots-clés avec lignes
  - Template : `template_analysis_output/slide_26.json`
  - Usage : Quatre statistiques avec séparateurs visuels

---

## 6. content_boxes_builder.py

**Rôle :** Création de boîtes de contenu structurées
**Fonction :** Affiche du contenu dans des boîtes visuelles (3 ou 4 éléments)

### Slides Supportées - 3 Boîtes
- **Slide 27** (index 26) - 3 boîtes grises avec sous-titres
  - Template : `template_analysis_output/slide_27.json`
  - Usage : Trois concepts avec sous-titres descriptifs

- **Slide 28** (index 27) - 3 boîtes grises sans sous-titres
  - Template : `template_analysis_output/slide_28.json`
  - Usage : Trois concepts simples

- **Slide 29** (index 28) - 3 boîtes bleues avec sous-titres
  - Template : `template_analysis_output/slide_29.json`
  - Usage : Trois points clés avec descriptions

- **Slide 30** (index 29) - 3 boîtes bleues sans sous-titres
  - Template : `template_analysis_output/slide_30.json`
  - Usage : Trois éléments principaux

### Slides Supportées - 4 Boîtes
- **Slide 31** (index 30) - 4 boîtes grises avec sous-titres
  - Template : `template_analysis_output/slide_31.json`
  - Usage : Quatre concepts détaillés

- **Slide 32** (index 31) - 4 boîtes grises sans sous-titres
  - Template : `template_analysis_output/slide_32.json`
  - Usage : Quatre éléments simples

- **Slide 33** (index 32) - 4 boîtes bleues avec sous-titres
  - Template : `template_analysis_output/slide_33.json`
  - Usage : Quatre points stratégiques

- **Slide 34** (index 33) - 4 boîtes bleues sans sous-titres
  - Template : `template_analysis_output/slide_34.json`
  - Usage : Quatre éléments clés

---

## 7. detailed_explanation_builder.py

**Rôle :** Explications détaillées et énoncés structurés
**Fonction :** Présente des explications approfondies avec plusieurs points

### Slides Supportées
- **Slide 35** (index 34) - 4 énoncés & Mots-clés
  - Template : `template_analysis_output/slide_35.json`
  - Usage : Quatre points détaillés avec mots-clés

- **Slide 39** (index 38) - 2 énoncés avec sous-titres et ligne bleue
  - Template : `template_analysis_output/slide_39.json`
  - Usage : Deux explications avec sous-titres, séparateur bleu

- **Slide 40** (index 39) - 2 énoncés avec sous-titres et ligne grise
  - Template : `template_analysis_output/slide_40.json`
  - Usage : Deux explications avec sous-titres, séparateur gris

- **Slide 41** (index 40) - 2 énoncés avec titre et ligne bleue
  - Template : `template_analysis_output/slide_41.json`
  - Usage : Deux points principaux avec titre, ligne bleue

- **Slide 42** (index 41) - 2 énoncés avec titre et ligne grise
  - Template : `template_analysis_output/slide_42.json`
  - Usage : Deux points principaux avec titre, ligne grise

- **Slide 43** (index 42) - 2 listes avec ligne bleue
  - Template : `template_analysis_output/slide_43.json`
  - Usage : Deux listes structurées, séparateur bleu

- **Slide 44** (index 43) - 2 listes avec ligne grise
  - Template : `template_analysis_output/slide_44.json`
  - Usage : Deux listes structurées, séparateur gris

---

## 8. testimonial_builder.py

**Rôle :** Citations et témoignages
**Fonction :** Affiche des citations avec attribution et contexte

### Slides Supportées
- **Slide 45** (index 44) - Citation
  - Template : `template_analysis_output/slide_45.json`
  - Usage : Témoignage ou citation avec auteur
  - Structure : Quote + Attribution + Context

---

## 9. charts_builder.py

**Rôle :** Graphiques et visualisations de données
**Fonction :** Crée et insère des graphiques basés sur des données CSV

### Slides Supportées
- **Slide 46** (index 45) - Graphique générique 1
  - Template : `template_analysis_output/slide_46.json`
  - Usage : Graphiques personnalisés

- **Slide 47** (index 46) - Graphique générique 2
  - Template : `template_analysis_output/slide_47.json`
  - Usage : Graphiques personnalisés

- **Slide 48** (index 47) - Graphique générique 3
  - Template : `template_analysis_output/slide_48.json`
  - Usage : Graphiques personnalisés

- **Slide 49** (index 48) - Graphique générique 4
  - Template : `template_analysis_output/slide_49.json`
  - Usage : Graphiques personnalisés

- **Slide 50** (index 49) - Graphique générique 5
  - Template : `template_analysis_output/slide_50.json`
  - Usage : Graphiques personnalisés

- **Slide 51** (index 50) - Graphique générique 6
  - Template : `template_analysis_output/slide_51.json`
  - Usage : Graphiques personnalisés

### Types de Graphiques Supportés
- Bar charts (horizontaux)
- Column charts (verticaux)
- Line charts (tendances)
- Pie charts (répartitions)
- Multi-series charts (comparaisons)

---

## Slides Non Utilisées

Les slides suivantes du template Premier Tech ne sont pas directement utilisées par les scripts mais restent disponibles dans le template :

- Slides 1-10 : Variantes de pages titre
- Slide 12 : Titre de présentation
- Slide 14 : Titre section avec chiffre
- Slides 20-21 : Autres formats de messages
- Slides 36-38 : Contenus avec images
- Slides 52-56 : Slides utilitaires et fermeture alternatives

---

## Navigation Rapide

### Par Type de Contenu

**Titres et Navigation**
- presentation_builder.py → Slides 11, 57
- navigation_builder.py → Slide 13
- section_header_builder.py → Slides 15-16

**Messages et Texte**
- simple_message_builder.py → Slides 17-19
- testimonial_builder.py → Slide 45

**Données et Métriques**
- statistics_builder.py → Slides 22-26
- charts_builder.py → Slides 46-51

**Contenu Structuré**
- content_boxes_builder.py → Slides 27-34
- detailed_explanation_builder.py → Slides 35, 39-44

### Par Nombre d'Éléments

**2 Éléments**
- Slides 22-23 (statistics)
- Slides 39-44 (detailed)

**3 Éléments**
- Slide 13 (navigation)
- Slide 24 (statistics)
- Slides 27-30 (content_boxes)

**4 Éléments**
- Slides 25-26 (statistics)
- Slides 31-34 (content_boxes)
- Slide 35 (detailed)

---

## Utilisation

Pour utiliser un script spécifique avec l'architecture JSON :

1. **Créer la configuration JSON** avec le script souhaité
2. **Spécifier le payload** pour le script
3. **Exécuter via presentation_builder.py**

Exemple :
```json
{
  "slides": [
    {
      "position": 2,
      "script_name": "statistics_builder",
      "payload_path": "stats.json",
      "description": "Statistiques clés"
    }
  ]
}
```

Le script `statistics_builder.py` sera appelé automatiquement et utilisera la slide appropriée selon le nombre de statistiques dans le payload.

---

## Maintenance

- **Ajout de nouveaux scripts** : Mettre à jour ce document avec les slides supportées
- **Modification des mappings** : Vérifier l'impact sur les présentations existantes
- **Templates** : Les analyses JSON dans `template_analysis_output/` documentent la structure de chaque slide

---

*Document généré le 2025-01-16*
*Version : Architecture JSON 2025*