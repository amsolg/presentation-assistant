# Enrichir l'Extraction avec les Vraies Valeurs de Formatage

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
Le script `src/slide_extractor.py` indique correctement qu'il ne peut pas extraire les valeurs héritées, mais n'utilise pas les vraies valeurs découvertes lors de l'analyse XML directe.

**Impact sur l'utilisateur :**
- Les fichiers JSON générés contiennent des valeurs `null` avec des notes d'extraction
- L'utilisateur doit consulter plusieurs documents pour connaître les vraies valeurs
- **Impossible d'utiliser directement les JSON comme payload** pour la création de présentations

## 💡 Solution Proposée

**Expérience cible :**
Créer un nouveau script dans `tools/` qui génère des JSON **directement utilisables comme payload** pour les modules de création de présentation, avec toutes les vraies valeurs de formatage enrichies.

**Objectif principal :**
Le JSON produit doit pouvoir être utilisé directement comme payload sans modification pour la personnalisation des slides lors de la création de présentation.

## 🛠️ Implémentation

### 1. Créer un nouveau script `tools/enhanced_slide_extractor.py`

**Ne pas déplacer le script existant** - créer un nouveau script optimisé pour la production de payload.

### 2. Structure complète de données de formatage Premier Tech

Créer une base de données complète avec TOUTES les vraies valeurs documentées :

```python
PREMIER_TECH_FORMATTING = {
    "layouts": {
        9: {  # Layout Page Titre (slide 11)
            "layout_name": "Page Titre",
            "slide_examples": [11],
            "placeholders": {
                "Titre 2": {
                    "font_name": "Premier Tech Title",
                    "font_size": 48.0,
                    "color": "#040E1E",
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "LEFT",
                    "vertical_alignment": "MIDDLE",
                    "text_wrap": True,
                    "auto_fit": "NONE"
                },
                "Espace réservé du texte 3": {
                    "font_name": "Premier Tech Title",
                    "font_size": 32.0,
                    "color": "#040E1E",
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "LEFT",
                    "vertical_alignment": "MIDDLE",
                    "text_wrap": True,
                    "auto_fit": "NONE"
                },
                "Espace réservé du texte 1": {
                    "font_name": "Calibri",
                    "font_size": 18.0,
                    "color": "#040E1E",
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "LEFT",
                    "vertical_alignment": "MIDDLE",
                    "text_wrap": True,
                    "auto_fit": "NONE"
                }
            }
        },
        11: {  # Layout Table des matières (slide 13)
            "layout_name": "Table des matières",
            "slide_examples": [13],
            "placeholders": {
                "Titre 38": {
                    "font_name": "Premier Tech Title",
                    "font_size": 36.0,
                    "color": "#040E1E",
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "LEFT",
                    "vertical_alignment": "TOP",
                    "text_wrap": True,
                    "auto_fit": "NONE"
                },
                "body_numbers": {  # Indices 11-18 - Numéros
                    "font_name": "Calibri",
                    "font_size": 24.0,
                    "color": "#41B6E6",  # accent1
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "CENTER",
                    "vertical_alignment": "MIDDLE",
                    "text_wrap": False,
                    "auto_fit": "NONE"
                },
                "body_titles": {  # Indices 19-23 - Titres sections
                    "font_name": "Calibri",
                    "font_size": 24.0,
                    "color": "#040E1E",  # tx1
                    "bold": False,
                    "italic": False,
                    "underline": False,
                    "alignment": "LEFT",
                    "vertical_alignment": "MIDDLE",
                    "text_wrap": True,
                    "auto_fit": "NONE"
                }
            }
        }
        # Ajouter TOUS les autres layouts identifiés...
    },
    "theme_colors": {
        "accent1": "#41B6E6",
        "accent2": "#A6A6A6",
        "accent3": "#0077C8",
        "accent4": "#92D050",
        "accent5": "#F79646",
        "accent6": "#9F4C96",
        "tx1": "#040E1E",
        "tx2": "#FFFFFF",
        "bg1": "#FFFFFF",
        "bg2": "#F2F2F2",
        "lt1": "#FFFFFF",
        "lt2": "#F2F2F2",
        "dk1": "#040E1E",
        "dk2": "#A6A6A6"
    },
    "font_mappings": {
        "+mn-lt": "Calibri Light",
        "+mn-ea": "Calibri",
        "+mj-lt": "Calibri",
        "+mj-ea": "Calibri",
        "Premier Tech Title": "Premier Tech Title"
    }
}
```

### 3. Format des valeurs pour compatibilité avec presentation_builder

**IMPORTANT - Analyser le format exact attendu par python-pptx et les scripts presentation_builder :**

**Questions à résoudre AVANT l'implémentation :**
1. **Couleurs** : Les scripts utilisent-ils `"#41B6E6"` (hex) ou `"accent1"` (scheme color) ?
2. **Polices** : Faut-il `"Calibri"` ou `"+mn-lt"` ?
3. **Tailles** : Format `48.0` (float) ou `Pt(48)` (objet) ?
4. **Alignement** : String `"LEFT"` ou constante `PP_ALIGN.LEFT` ?

**Action requise :**
```python
# ANALYSER le code dans presentation_builder/ pour déterminer :
# 1. Comment les couleurs sont passées à python-pptx
# 2. Comment les polices sont définies
# 3. Le format exact des tailles de police
# 4. Les constantes d'alignement utilisées

# Exemple à vérifier dans les scripts existants :
font.color.rgb = RGBColor.from_string("#41B6E6")  # Format hex ?
# ou
font.color.theme_color = MSO_THEME_COLOR.ACCENT_1  # Format scheme ?
```

**Le mapping devra convertir vers le format EXACT attendu, par exemple :**
- Si python-pptx attend hex → Convertir `scheme:accent1` en `#41B6E6`
- Si python-pptx attend scheme → Garder `accent1` tel quel
- Si les polices doivent être résolues → Convertir `+mn-lt` en `Calibri Light`

### 4. Format JSON de sortie optimisé pour payload

Le script doit produire un JSON **directement compatible** avec les modules de création :

```json
{
  "slide_number": 11,
  "layout_id": 9,
  "layout_name": "Page Titre",
  "extraction_metadata": {
    "extracted_at": "2025-10-17T14:30:00Z",
    "script_version": "1.0.0",
    "confidence": "high",
    "source": "enhanced_extraction_with_mapping"
  },
  "title_slide_payload": {
    "title": {
      "text": "Page Titre",
      "formatting": {
        "font_name": "Premier Tech Title",
        "font_size": 48.0,
        "color": "#040E1E",
        "bold": false,
        "italic": false,
        "underline": false,
        "alignment": "LEFT",
        "vertical_alignment": "MIDDLE"
      },
      "placeholder_info": {
        "name": "Titre 2",
        "type": "TITLE",
        "index": 0
      }
    },
    "subtitle": {
      "text": "Sous-titre de la présentation",
      "formatting": {
        "font_name": "Premier Tech Title",
        "font_size": 32.0,
        "color": "#040E1E",
        "bold": false,
        "italic": false,
        "underline": false,
        "alignment": "LEFT",
        "vertical_alignment": "MIDDLE"
      },
      "placeholder_info": {
        "name": "Espace réservé du texte 3",
        "type": "SUBTITLE",
        "index": 1
      }
    },
    "metadata": {
      "text": "2025-10-17 – Premier Tech",
      "formatting": {
        "font_name": "Calibri",
        "font_size": 18.0,
        "color": "#040E1E",
        "bold": false,
        "italic": false,
        "underline": false,
        "alignment": "LEFT",
        "vertical_alignment": "MIDDLE"
      },
      "placeholder_info": {
        "name": "Espace réservé du texte 1",
        "type": "CONTENT",
        "index": 2
      }
    }
  },
  "raw_extraction": {
    "placeholders_found": 3,
    "text_runs_analyzed": 15,
    "inherited_values_resolved": 12
  }
}
```

### 4. Fonctionnalités avancées du script

**Enrichissement automatique :**
- Détection automatique du layout utilisé
- Résolution des valeurs héritées via mapping
- Validation de la cohérence des données
- Génération de payload structuré par type de contenu

**Formats de sortie multiples :**
- Format payload pour `simple_message_builder`
- Format payload pour `navigation_builder`
- Format payload pour `section_header_builder`
- Format générique avec toutes les informations

**Validation et qualité :**
- Vérification de la complétude des données
- Score de confiance pour chaque valeur
- Détection des incohérences
- Suggestions d'amélioration

### 5. Utilisation du script

**Arguments du script :**
```bash
python tools/enhanced_slide_extractor.py <presentation.pptx> [slide_number]
```

**Paramètres :**
- `<presentation.pptx>` : **OBLIGATOIRE** - Chemin vers le fichier PowerPoint à analyser
- `[slide_number]` : **OPTIONNEL** - Numéro de la slide à extraire
  - Si absent : TOUTES les slides sont extraites
  - Si présent : Seule la slide spécifiée est extraite

**Exemples d'utilisation :**
```bash
# Extraire TOUTES les slides d'une présentation
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx

# Extraire uniquement la slide 11
python tools/enhanced_slide_extractor.py templates/Template_PT.pptx 11

# Extraire la slide 13 d'une autre présentation
python tools/enhanced_slide_extractor.py presentations/ma_presentation.pptx 13
```

**Format de sortie :**
- Si une seule slide : `slide_[N]_enriched.json`
- Si toutes les slides : Dossier `output/` avec un fichier par slide

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] JSON directement utilisable comme payload sans modification
- [ ] Toutes les vraies valeurs de formatage incluses
- [ ] Format compatible avec les modules de création existants
- [ ] Documentation claire pour chaque champ

**Pour le système :**
- [ ] Script autonome dans tools/ avec dépendances claires
- [ ] Base de données complète des valeurs Premier Tech
- [ ] Validation automatique de la qualité des données
- [ ] Support de tous les layouts identifiés

**Pour la production :**
- [ ] Performance optimisée pour extraction batch
- [ ] Gestion d'erreurs robuste
- [ ] Logging détaillé pour debugging
- [ ] Format JSON validé et cohérent

## 🚀 Plan d'Action Détaillé

### Phase 1: Architecture et Base de Données
1. **Créer `tools/enhanced_slide_extractor.py`** avec architecture modulaire
2. **Construire la base complète `PREMIER_TECH_FORMATTING`** avec toutes les valeurs documentées
3. **Implémenter le moteur de résolution** des valeurs héritées
4. **Créer les templates de payload** pour chaque type de module

### Phase 2: Extraction et Enrichissement
1. **Développer l'analyseur de layout** automatique
2. **Implémenter l'enrichissement** des valeurs null
3. **Créer le générateur de payload** structuré
4. **Ajouter la validation** de cohérence

### Phase 3: Formats de Sortie
1. **Implémenter les formats payload spécialisés** par module
2. **Créer le format générique** avec toutes les informations
3. **Ajouter les métadonnées** de qualité et traçabilité
4. **Optimiser la structure JSON** pour réutilisation

### Phase 4: Tests et Validation
1. **Tester sur slides 11 et 13** comme cas de référence
2. **Valider la compatibilité** avec les modules existants
3. **Vérifier l'utilisabilité directe** des payload générés
4. **Documenter l'utilisation** et les formats

## 📊 Métriques de Qualité Attendues

- **Complétude :** 100% des propriétés formatage renseignées
- **Exactitude :** Valeurs identiques aux templates Premier Tech
- **Utilisabilité :** JSON utilisable directement sans modification
- **Performance :** < 2 secondes par slide analysée
- **Fiabilité :** Score de confiance > 95% pour les valeurs critiques

---

**Créé :** 2025-10-17
**Priorité :** Élevée
**Estimation :** 3-4 heures
**Complexité :** Moyenne-Élevée

**Note importante :** Cette tâche vise à créer un outil de production capable de générer des payload directement réutilisables pour l'automatisation de création de présentations Premier Tech.