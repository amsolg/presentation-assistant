# Tools - Outils de Gestion de Présentations

Ce dossier contient les outils principaux pour la création et gestion automatisée de présentations Premier Tech.

## 🚀 Scripts Principaux

### [presentation_builder.py](presentation_builder.py) ⭐ **Script Principal**
**Générateur de présentations basé sur layout_name**

Nouvelle architecture qui utilise les noms de layouts au lieu des numéros de slides pour plus de lisibilité et flexibilité.

```bash
# Utilisation
python tools/presentation_builder.py config.json

# Avec options
python tools/presentation_builder.py config.json --validate --verbose
```

**Configuration JSON (format layout-based) :**
```json
{
  "presentation_name": "Ma Présentation",
  "subject": "innovation-strategy",
  "audience": "c-level",
  "is_test": false,
  "slides": [
    {
      "layout_name": "Page titre",
      "shapes": [
        {
          "shape_id": 1,
          "text": "Métadonnées - 2025-01-15",
          "font_name": "Premier Tech Text",
          "font_size": 18.0,
          "color": "#FFFFFF"
        }
      ]
    }
  ],
  "output_path": "ma_presentation.pptx"
}
```

> **💡 Note :** L'`output_path` est automatiquement normalisé vers `presentations/[sujet]/[audience]/output/` ou `tests/[sujet]/[audience]/output/` selon le mode. Plus besoin de spécifier le chemin complet !

**Avantages :**
- Configuration lisible ("Page titre" vs slide_number: 11)
- Flexibilité totale dans l'ordre des slides
- Réutilisation libre des mêmes layouts
- Validation automatique des layouts

---

### [init_presentation.py](init_presentation.py)
**Initialisation de nouveaux projets de présentation**

Crée la structure complète d'un projet de présentation avec configuration optimisée.

```bash
# Utilisation
python tools/init_presentation.py sujet audience [is_test]

# Exemples
python tools/init_presentation.py innovation-ai c-level false
python tools/init_presentation.py test-features technique true
```

**Structure créée :**
```
presentations/[sujet]/[audience]/
├── config.json          # Configuration layout-based
├── README.md            # Guide d'utilisation
├── data/               # Données et recherches
└── output/             # Présentations générées
```

---

### [slide_extractor.py](slide_extractor.py)
**Extraction et analyse de slides PowerPoint**

Outil avancé pour extraire les structures et propriétés des slides existantes.

```bash
# Extraire une slide spécifique
python tools/slide_extractor.py templates/Template_PT.pptx --slide-number 11 --output slide_11.json

# Extraire toutes les slides
python tools/slide_extractor.py ma_presentation.pptx --output-dir extracted_slides/

# Validation bidirectionnelle
python tools/slide_extractor.py ma_presentation.pptx --slide-number 1 --output extracted.json
```

**Fonctionnalités :**
- Extraction complète des propriétés de formatage
- Support des layouts Premier Tech
- Validation bidirectionnelle (extraction ↔ génération)
- Analyse XML détaillée
- Export JSON structuré

---

### [add_slide.py](add_slide.py)
**Ajout de slides à une présentation existante**

Ajoute des slides basées sur les templates Premier Tech à une présentation.

```bash
# Ajouter une slide par layout
python tools/add_slide.py config.json "Page titre" ajout

# Ajouter avec configuration personnalisée
python tools/add_slide.py config.json "Section" ajout --custom-config custom.json
```

---

### [remove_slide.py](remove_slide.py)
**Suppression de slides d'une présentation**

Supprime des slides spécifiques d'une présentation existante.

```bash
# Supprimer une slide par position
python tools/remove_slide.py ma_presentation.pptx 3

# Supprimer plusieurs slides
python tools/remove_slide.py ma_presentation.pptx 2,4,6
```

---

### [validation_checker.py](validation_checker.py)
**Validation et contrôle qualité**

Valide les présentations contre les standards Premier Tech.

```bash
# Validation complète d'une présentation
python tools/validation_checker.py ma_presentation.pptx

# Validation d'une configuration JSON
python tools/validation_checker.py --config config.json

# Rapport détaillé
python tools/validation_checker.py ma_presentation.pptx --report detailed_report.json
```

## 🎯 Workflow Complet

### 1. Initialisation d'un Projet
```bash
# Créer la structure
python tools/init_presentation.py innovation-digitale c-level false

# Résultat : presentations/innovation-digitale/c-level/ avec config.json
```

### 2. Ajout de Contenu
```bash
# Ajouter des slides via le config.json principal
python tools/add_slide.py presentations/innovation-digitale/c-level/config.json "Page titre" ajout
python tools/add_slide.py presentations/innovation-digitale/c-level/config.json "Titre de section bleu" ajout
python tools/add_slide.py presentations/innovation-digitale/c-level/config.json "2 statistiques avec ligne bleue" ajout
```

### 3. Génération de la Présentation
```bash
# Construire la présentation finale
python tools/presentation_builder.py presentations/innovation-digitale/c-level/config.json

# Résultat : presentations/innovation-digitale/c-level/output/innovation_digitale.pptx
```

### 4. Validation et Contrôle
```bash
# Valider la présentation générée
python tools/validation_checker.py presentations/innovation-digitale/c-level/output/innovation_digitale.pptx

# Extraction pour vérification bidirectionnelle
python tools/slide_extractor.py presentations/innovation-digitale/c-level/output/innovation_digitale.pptx --slide-number 1
```

## 📋 Layouts Premier Tech Supportés

Les layouts utilisables dans la configuration JSON (basés sur les noms de fichiers) :

### **Slides de Base**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Page titre" | Slide de titre principale | Ouverture de présentation |
| "Titre de présentation" | Titre spécialisé | Présentations formelles |
| "Table des matières" | Sommaire structuré | Navigation |

### **Sections et Navigation**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Titre de section avec chiffre" | Section numérotée | Parties principales |
| "Titre de section bleu" | Section emphasis | Transitions importantes |
| "Titre de section blanc" | Section standard | Sous-sections |

### **Messages et Contenu**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Court énoncé" | Message simple centré | Points clés |
| "Court énoncé avec titre de section" | Message avec contexte | Énoncés sectionnés |
| "Énoncé avec titre et image" | Contenu illustré | Présentations visuelles |
| "Liste avec titre et image" | Liste illustrée | Énumérations visuelles |

### **Mots-Clés et Concepts**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Mots clés court énoncé" | Concepts + message | Définitions |
| "Mots clés court énoncé avec titre de section" | Concepts sectionnés | Vocabulaire thématique |
| "Mots clés mots complémentaires" | Écosystème conceptuel | Relations complexes |

### **Statistiques et Métriques**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "2 statistiques avec ligne bleue" | Duo de métriques | Comparaisons |
| "2 statistiques avec ligne grise" | Métriques neutres | Données objectives |
| "3 statistiques mots clés" | Triple KPI | Tableaux de bord |
| "4 statistiques mots clés" | Quadruple KPI | Dashboards complets |
| "4 statistiques mots clés avec lignes" | KPI structurés | Métriques organisées |

### **Boîtes de Contenu**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "3 boîtes bleues pour courts énoncés avec sous-titre" | Triple concept détaillé | Piliers principaux |
| "3 boîtes bleues pour courts énoncés sans sous-titre" | Triple concept simple | Énumérations courtes |
| "3 boîtes grises pour courts énoncés avec sous-titre" | Triple concept neutre | Listes techniques |
| "4 boîtes bleues pour courts énoncés avec sous-titre" | Quadruple concept détaillé | Axes stratégiques |
| "4 boîtes grises pour courts énoncés sans sous-titre" | Quadruple concept simple | Listes pratiques |

### **Énoncés et Listes**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "2 énoncés avec sous-titres et ligne bleue" | Comparaison détaillée | Avant/Après |
| "2 énoncés avec sous-titres et ligne grise" | Comparaison neutre | Alternatives |
| "2 énoncés avec titre et ligne bleue" | Dualité avec emphasis | Choix stratégiques |
| "2 listes avec sous-titres et ligne bleue" | Listes comparatives | Avantages/Inconvénients |
| "4 énoncés mots clés" | Quadruple argumentation | Plans d'action |

### **Éléments Spéciaux**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Citation" | Témoignage ou citation | Validation externe |
| "Titre espace pour tableau ou graphique" | Placeholder données | Visualisations |
| "Énoncé avec sous-titres et image" | Contenu riche illustré | Cas d'usage |
| "Diapositive vide" | Canvas libre | Contenu personnalisé |
| "Vidéo" | Placeholder multimédia | Contenus vidéo |

### **Branding Premier Tech**
| Layout Name | Description | Usage |
|-------------|-------------|-------|
| "Monogramme PT" | Logo corporate | Branding |
| "We are PT" | Identité d'entreprise | Présentation corporate |
| "Nourrir protéger améliorer" | Mission PT | Valeurs corporate |
| "Passion et technologies pour faire la différence" | Signature PT | Closing inspirant |

## 🔧 Configuration Avancée

### Propriétés de Shapes Supportées

**Géométrie :**
- `left`, `top`, `width`, `height` (position et dimensions en points)

**Texte :**
- `text` : Contenu textuel
- `font_name` : Police (Premier Tech Text, Premier Tech Title, Premier Tech Title Bold)
- `font_size` : Taille (18.0 à 66.0 points)
- `color` : Couleur (#FFFFFF, #41B6E6, #BDBDBD)
- `bold` : Gras (true/false)
- `alignment` : Alignement (LEFT, CENTER, RIGHT)

**Formatage Avancé :**
- `vertical_alignment` : Alignement vertical (TOP, MIDDLE, BOTTOM)
- `margin_left`, `margin_right`, `margin_top`, `margin_bottom` : Marges
- `text_wrapping` : Habillage du texte

**PowerPoint Spécifique :**
- `autofit_type` : Ajustement automatique (none, normal)
- `placeholder_type` : Type de placeholder (body, title, ctrTitle)

## 🎨 Validation Premier Tech

Toutes les propriétés sont automatiquement validées contre les standards Premier Tech :
- **Polices** : Uniquement les 3 polices officielles
- **Couleurs** : Palette corporate Premier Tech
- **Tailles** : Gamme de tailles validées
- **Marges** : Valeurs standards respectées

## 📚 Documentation Connexe

- **Commandes disponibles** : [.claude/commands/](../.claude/commands/)
- **Templates** : [templates/](../templates/)
- **Tests** : [tests/](../tests/)
- **Documentation** : [docs/](../docs/)

## ✅ Avantages du Système

- **Architecture moderne** : Layout-based pour plus de flexibilité
- **Validation automatique** : Conformité Premier Tech garantie
- **Workflow intégré** : De l'initialisation à la génération finale
- **Fidélité bidirectionnelle** : Extraction ↔ Génération parfaite
- **Templates authentiques** : Préservation complète des styles PT
- **Performance optimisée** : < 2s par slide complexe