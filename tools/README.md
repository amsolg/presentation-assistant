# Tools - Outils d'extraction avancés

Ce dossier contient des outils avancés pour l'extraction et l'enrichissement du contenu PowerPoint.

## enhanced_slide_extractor.py

### Description
Script d'extraction avancé qui résout automatiquement les valeurs de formatage héritées depuis les layouts et masters PowerPoint. Contrairement au script standard, celui-ci :

- Extrait les couleurs du thème directement depuis le XML
- Résout l'héritage des styles depuis les layouts
- Récupère les vraies valeurs de formatage des placeholders
- Produit un JSON enrichi avec toutes les informations nécessaires

### Utilisation

#### Extraire une slide spécifique
```bash
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx 11
```
Génère : `slide_11_enriched.json`

#### Extraire toutes les slides
```bash
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx
```
Génère : Dossier `enhanced_output/` avec un fichier JSON par slide

### Format de sortie

Le script produit un JSON structuré avec les vraies valeurs extraites :

```json
{
  "slide_number": 11,
  "layout_name": "Page Titre",
  "layout_id": 9,
  "shapes": [
    {
      "name": "Titre 2",
      "type": "placeholder",
      "text": "Objet de la présentation",
      "position": {
        "left": 54.17,
        "top": 296.9,
        "width": 887.45,
        "height": 87.24
      },
      "font_name": "Premier Tech Title",
      "font_size": 48.0,
      "color": "#040E1E",
      "bold": false,
      "italic": false,
      "underline": false,
      "alignment": "LEFT"
    }
  ]
}
```

### Fonctionnalités principales

1. **Extraction du thème** : Parse le XML du thème pour obtenir les vraies couleurs
2. **Analyse des layouts** : Extrait le formatage par défaut de chaque placeholder
3. **Résolution de l'héritage** : Combine les valeurs de la slide, du layout et du master
4. **Format utilisable** : Produit un JSON directement utilisable pour créer des présentations

### Différences avec slide_extractor.py

| Fonctionnalité | slide_extractor.py | enhanced_slide_extractor.py |
|---|---|---|
| Extraction du texte | ✅ | ✅ |
| Position des shapes | ✅ | ✅ |
| Formatage direct | ✅ Partiel | ✅ Complet |
| Héritage layout | ❌ | ✅ |
| Couleurs du thème | ❌ | ✅ |
| Polices héritées | ❌ | ✅ |
| Parsing XML | ❌ | ✅ |

### Cas d'usage

- **Documentation de templates** : Extraction complète des valeurs de formatage
- **Génération de payloads** : Création de JSON pour les scripts de construction
- **Analyse de présentations** : Comprendre la structure et le formatage réel
- **Migration de templates** : Capturer tous les styles pour réplication

### Limitations

- Nécessite python-pptx installé
- Les animations et transitions ne sont pas extraites
- Les objets médias sont identifiés mais leur contenu n'est pas extrait
- Performance : ~2 secondes par slide pour une extraction complète

### Exemples de commandes

```bash
# Extraire la slide titre
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx 11

# Extraire la table des matières
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx 13

# Extraire toutes les slides d'une présentation
python tools/enhanced_slide_extractor.py presentations/ma_presentation.pptx

# Extraire depuis n'importe quel dossier
cd C:\repos\presentation-assistant
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx 11
```