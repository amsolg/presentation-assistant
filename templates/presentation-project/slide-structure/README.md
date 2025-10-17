# Slide Structure Documentation

## Vue d'ensemble

Ce dossier contient les structures JSON détaillées de chaque slide du template Premier Tech. Chaque fichier JSON documente précisément :
- La position exacte de chaque élément visuel (shape)
- Les dimensions et propriétés de formatage
- Les contraintes et bonnes pratiques d'utilisation
- Des exemples de contenu approprié

## Utilisation du script d'extraction

### Commande de base
```bash
python tools/extract_slide_structure.py template_analysis_output/slide_XX.json XX
```

### Exemples
```bash
# Extraire la structure de la slide 11
python tools/extract_slide_structure.py template_analysis_output/slide_11.json 11

# Extraire la structure de la slide 13 (Table des matières)
python tools/extract_slide_structure.py template_analysis_output/slide_13.json 13

# Avec fichier de sortie personnalisé
python tools/extract_slide_structure.py template_analysis_output/slide_15.json 15 custom_output.json
```

## Structure des fichiers JSON

### Informations principales
- `slide_number` : Numéro de la slide (1-57)
- `slide_index` : Index 0-based de la slide
- `layout_name` : Nom du layout PowerPoint utilisé
- `template_usage` : Description de l'usage recommandé

### Shapes (éléments visuels)
Chaque shape contient :
- **Identification** : `shape_id`, `element_id`, `type`, `name`
- **Positionnement** : Coordonnées absolues et relatives (%)
- **Dimensions** : Largeur et hauteur en points et pourcentages
- **Contenu** : Texte actuel, taille de police, alignement
- **Guidelines** :
  - `purpose` : Objectif de l'élément
  - `max_characters` : Limite de caractères recommandée
  - `content_examples` : Exemples de contenu approprié
  - `restrictions` : Contraintes à respecter

### Informations supplémentaires
- `visual_hierarchy` : Ordre de lecture et niveaux d'importance
- `branding_elements` : Éléments de marque Premier Tech
- `best_practices` : Recommandations d'utilisation
- `automation_notes` : Notes pour l'automatisation

## Fichiers disponibles

| Slide | Fichier | Description |
|-------|---------|-------------|
| 11 | `slide_11_structure.json` | Page titre principale avec métadonnées |
| 13 | `slide_13_structure.json` | Table des matières structurée |
| ... | ... | Autres slides à documenter |

## Workflow d'enrichissement

1. **Extraction automatique** : Le script extrait la structure de base
2. **Enrichissement manuel** : Ajouter les descriptions et guidelines
3. **Validation** : Vérifier la cohérence avec le template
4. **Documentation** : Mettre à jour ce README

## Integration avec presentation_builder

Les fichiers de structure peuvent être utilisés pour :
- Valider automatiquement le contenu avant insertion
- Vérifier les limites de caractères
- Suggérer des améliorations de contenu
- Garantir le respect de l'identité visuelle

## Prochaines étapes

- [ ] Extraire la structure de toutes les 57 slides
- [ ] Enrichir chaque fichier avec des descriptions détaillées
- [ ] Créer un validateur automatique basé sur ces structures
- [ ] Intégrer la validation dans presentation_builder.py

## Notes techniques

- Les positions et dimensions sont en points PowerPoint (1 inch = 72 points)
- Les pourcentages sont calculés par rapport aux dimensions de la slide (1280x720)
- L'ordre des shapes dans le JSON reflète la hiérarchie visuelle recommandée