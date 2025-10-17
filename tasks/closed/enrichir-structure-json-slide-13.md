# Enrichir Structure JSON Détaillée pour Slide 13 (Table des matières)

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
Le fichier `templates/presentation-project/slide-structure/slide_13_structure.json` existe mais manque d'informations essentielles :
- Les descriptions de chaque shape sont vides
- Les font_size sont tous null
- Pas de documentation sur l'usage prévu de chaque élément
- Pas de contraintes de contenu (nombre de caractères recommandé, etc.)

**Impact sur l'utilisateur :**
- Incertitude sur comment utiliser correctement la slide Table des matières
- Risque de dépasser les limites visuelles recommandées
- Difficulté à comprendre la relation entre les numéros et les titres de section
- Impossible de valider automatiquement si le contenu respecte les bonnes pratiques

## 💡 Solution Proposée

**Expérience cible :**
L'utilisateur devrait pouvoir consulter un fichier JSON enrichi qui documente précisément chaque élément de la slide 13 (Table des matières), avec les tailles de police exactes, des descriptions claires de l'usage de chaque shape, et des recommandations de contenu.

**Bénéfices attendus :**
- Documentation complète de la slide Table des matières
- Développement plus rapide du module navigation_builder
- Validation automatique du contenu des sections
- Préservation garantie du design Premier Tech

## 🛠️ Implémentation

### Ce qui doit changer
- **Fichier à enrichir :** `templates/presentation-project/slide-structure/slide_13_structure.json`
- **Script existant :** Utiliser `tools/extract_slide_structure.py` pour extraire les propriétés manquantes
- **Enrichissement manuel :** Ajouter les descriptions et recommandations pour chaque shape

### Structure JSON enrichie attendue
```json
{
  "slide_number": 13,
  "slide_title": "Table des matières",
  "layout_name": "Table des matières",
  "slide_dimensions": {
    "width": 1280.0,
    "height": 720.0
  },
  "usage_guidelines": {
    "purpose": "Navigation principale de la présentation avec sections numérotées",
    "max_sections": 5,
    "recommended_title_length": "30-40 caractères par section"
  },
  "shapes": [
    {
      "shape_id": 2,
      "element_id": "shape_1",
      "type": "text_box",
      "name": "Section Number 1",
      "position": {"left": 471.54, "top": 208.68},
      "dimensions": {"width": 71.81, "height": 48.47},
      "text_content": "1",
      "font_size": 24,
      "font_name": "Calibri",
      "font_color": "#FFFFFF",
      "description": "Numéro de la première section - Cercle bleu avec chiffre blanc",
      "constraints": {
        "max_characters": 2,
        "content_type": "numeric",
        "editable": true
      }
    },
    {
      "shape_id": 7,
      "element_id": "shape_6",
      "type": "text_box",
      "name": "Section Title 1",
      "position": {"left": 543.35, "top": 208.68},
      "dimensions": {"width": 613.89, "height": 48.47},
      "text_content": "Lorem ipsum dolor sit amet",
      "font_size": 18,
      "font_name": "Calibri Light",
      "font_color": "#333333",
      "description": "Titre de la première section - Texte aligné avec le numéro",
      "constraints": {
        "max_characters": 50,
        "content_type": "text",
        "recommended_length": "30-40 caractères"
      }
    }
    // ... autres shapes avec descriptions complètes
  ]
}
```

### Tests de validation
- [ ] Script extrait correctement les font_size de la slide 13
- [ ] Script récupère les couleurs et styles de police
- [ ] Descriptions manuelles ajoutées pour les 12 shapes
- [ ] Guidelines d'usage documentées
- [ ] Contraintes de contenu définies pour chaque élément

### Documentation à ajuster
- [ ] Mettre à jour `docs/SCRIPTS_SLIDES_MAPPING.md` avec les détails de la slide 13
- [ ] Documenter la structure dans le module `navigation_builder.py`

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Comprend immédiatement comment structurer une table des matières
- [ ] Sait combien de sections peuvent être affichées (max 5)
- [ ] Connaît les limites de caractères pour chaque titre
- [ ] Peut valider que son contenu respecte les contraintes

**Pour le système :**
- [ ] JSON enrichi avec toutes les propriétés de style
- [ ] Descriptions claires pour chaque shape
- [ ] Contraintes documentées et validables
- [ ] Format cohérent avec les autres fichiers de structure

## 🚀 Prochaines Étapes

1. **Extraire** les propriétés manquantes avec le script Python
2. **Analyser** visuellement la slide pour comprendre l'usage de chaque élément
3. **Enrichir** le JSON avec descriptions et contraintes
4. **Valider** que le navigation_builder peut utiliser ces informations
5. **Documenter** la structure dans les guides appropriés

---

**Créé :** 2025-10-16
**Priorité :** Élevée
**Estimation :** 2 heures