# Scripts de Construction de Présentations Premier Tech

## 🎯 Vue d'Ensemble

Ce dossier contient les scripts spécialisés pour créer automatiquement des slides selon les standards Premier Tech. Chaque script correspond à un besoin spécifique et utilise les vraies slides du template Premier Tech.

## 📋 Scripts Disponibles

| Script | Besoin | Slides | Usage Rapide |
|--------|--------|--------|--------------|
| **`01_slide_title_creator.py`** | Couverture/Intro | 11 | `python 01_slide_title_creator.py "Mon Titre"` |
| **`02_navigation_builder.py`** | Navigation | 13 | `python 02_navigation_builder.py --sections "Intro" "Développement" "Conclusion"` |
| **`03_section_header_builder.py`** | Nouvelle section | 14-16 | `python 03_section_header_builder.py "Ma Section" --style major` |
| **`04_simple_message_builder.py`** | Message simple | 17-22 | `python 04_simple_message_builder.py "Mon message impactant"` |
| **`05_statistics_builder.py`** | 2 statistiques | 23-24 | `python 05_statistics_builder.py "85%" "Satisfaction" "127M$" "Revenus"` |
| **`06_dashboard_builder.py`** | 3-4 statistiques | 25-28 | `python 06_dashboard_builder.py --kpi-values "85%" "127M$" "23%" --kpi-labels "CSAT" "Revenus" "Croissance"` |
| **`07_content_boxes_builder.py`** | 3 concepts égaux | 29-31 | `python 07_content_boxes_builder.py "Innovation" "Qualité" "Croissance"` |
| **`08_pillars_builder.py`** | 4 piliers/axes | 32-35 | `python 08_pillars_builder.py "Architecture" "Sécurité" "Performance" "Monitoring"` |
| **`09_comparison_builder.py`** | Comparaison A vs B | 36-44 | `python 09_comparison_builder.py "Solution A" "Solution B" --title "Comparaison"` |
| **`10_charts_builder.py`** | Graphiques/Visualisations | 46-51 | `python 10_charts_builder.py "Titre Graphique" --insert-into ma_presentation.pptx --style bar_chart` |

## ⚠️ **ARCHITECTURE IMPORTANTE : Seul le Script 01 Crée une Présentation**

**Règle Fondamentale :**
- **Script 01** (`01_slide_title_creator.py`) : **SEUL script autorisé à créer une nouvelle présentation**
- **Scripts 02-10** : **Ne peuvent QUE s'insérer dans une présentation existante** via `--insert-into`

## 🚀 Démarrage Rapide

### 1. Prérequis
```bash
# Vérifier que le template Premier Tech est disponible
ls ../templates/Template_PT.pptx

# Installer les dépendances
pip install python-pptx
```

### 2. Premier Usage (Workflow Obligatoire)
```bash
# ÉTAPE 1 : Créer une présentation (SEUL SCRIPT AUTORISÉ)
python 01_slide_title_creator.py "Ma Première Présentation"

# ÉTAPE 2 : Ajouter les slides dans la présentation créée (via --insert-into)

# Ajouter une navigation
python 02_navigation_builder.py --insert-into "ma_presentation.pptx" --sections "Introduction" "Analyse" "Recommandations" "Questions"

# Ajouter un header de section
python 03_section_header_builder.py "Introduction" --insert-into "ma_presentation.pptx" --style major

# Ajouter un message simple
python 04_simple_message_builder.py "Message percutant pour l'audience" --insert-into "ma_presentation.pptx"

# Ajouter des statistiques
python 05_statistics_builder.py "92%" "Satisfaction client" "15M$" "Économies générées" --insert-into "ma_presentation.pptx"

# Ajouter un dashboard KPI
python 06_dashboard_builder.py --kpi-values "99.9%" "1.2ms" "156%" "2.8M" --kpi-labels "Uptime" "Latence" "Croissance" "Clients" --insert-into "ma_presentation.pptx"

# Ajouter 3 concepts égaux
python 07_content_boxes_builder.py "Innovation" "Qualité" "Croissance" --style blue_detailed --insert-into "ma_presentation.pptx"

# Ajouter 4 piliers/axes
python 08_pillars_builder.py "Architecture" "Sécurité" "Performance" "Monitoring" --style blue_detailed --insert-into "ma_presentation.pptx"

# Ajouter une comparaison A vs B
python 09_comparison_builder.py "Solution Actuelle" "Solution Proposée" --title "Analyse Comparative" --style blue_line --insert-into "ma_presentation.pptx"

# Ajouter des graphiques et visualisations
python 10_charts_builder.py "Performance Q4" --insert-into "ma_presentation.pptx" --style bar_chart --data-labels "Ventes" "Marketing" "R&D" --data-values "125M$" "45M$" "78M$"
```

### 3. Options Communes

Tous les scripts supportent :
- `--insert-into fichier.pptx` : Insérer dans une présentation existante
- `--validate` : Valider le template seulement
- `--list-styles` : Lister les styles disponibles (scripts 3, 4, 5, 6)
- `--output chemin.pptx` : Spécifier le fichier de sortie
- `--no-widen` : Désactiver l'élargissement automatique des objets texte

### 4. Workflow Complet
```bash
# 1. Créer la structure de base
python 01_slide_title_creator.py "Transformation Numérique 2024"
python 02_navigation_builder.py --sections "Contexte" "Analyse" "Solutions" "ROI" "Plan d'action"

# 2. Insérer dans une présentation
python 03_section_header_builder.py "Contexte" --insert-into ma_presentation.pptx --style major
python 04_simple_message_builder.py "Le numérique transforme notre industrie" --insert-into ma_presentation.pptx
python 05_statistics_builder.py "85%" "Entreprises impactées" "3.2M$" "Investissement moyen" --insert-into ma_presentation.pptx

# 3. Ajouter énumérations et piliers
python 07_content_boxes_builder.py "Analyse" "Solution" "Livraison" --insert-into ma_presentation.pptx
python 08_pillars_builder.py "Architecture" "Sécurité" "Performance" "Monitoring" --insert-into ma_presentation.pptx

# 4. Ajouter une comparaison
python 09_comparison_builder.py "Avant" "Après" --subtitle-a "État actuel" --subtitle-b "État cible" --insert-into ma_presentation.pptx --style detailed

# 5. Ajouter des graphiques et visualisations
python 10_charts_builder.py "Métriques Performance" --insert-into ma_presentation.pptx --style bar_chart --data-labels "Q1" "Q2" "Q3" "Q4" --data-values "2.1M$" "2.8M$" "3.2M$" "3.7M$" --insights "Croissance constante sur l'année"

# 6. Ajouter un dashboard final
python 06_dashboard_builder.py --kpi-values "127%" "95%" "2.3M" "6 mois" --kpi-labels "ROI attendu" "Satisfaction équipe" "Budget alloué" "Délai mise en œuvre" --insert-into ma_presentation.pptx --title "Synthèse du Projet"
```

## 🎨 Styles et Variantes

### Scripts avec Styles Multiples

#### `03_section_header_builder.py`
- `numbered` : Slide 14 - Avec numérotation
- `major` : Slide 15 - Transitions importantes (défaut)
- `moderate` : Slide 16 - Sous-sections

#### `04_simple_message_builder.py`
- `simple` : Slide 21 - Message centré (défaut)
- `centered` : Slide 17 - Message unique focus maximal
- `illustrated` : Slide 18 - Avec image
- `keyword_simple` : Slide 19 - Avec mots-clés
- `keyword_short` : Slide 20 - Mots-clés + court énoncé
- `alternative` : Slide 22 - Format alternatif

#### `05_statistics_builder.py`
- `blue_line` : Slide 23 - Comparaison valorisée (défaut)
- `grey_line` : Slide 24 - Comparaison technique

#### `06_dashboard_builder.py`
- `triple_kpi` : Slide 25 - 3 KPI + mots-clés (défaut)
- `quad_kpi` : Slide 26 - 4 KPI complet
- `quad_structured` : Slide 27 - 4 KPI avec lignes
- `alternative` : Slide 28 - Format alternatif

#### `07_content_boxes_builder.py`
- `blue_simple` : Slide 29 - 3 boîtes bleues simples (défaut)
- `blue_detailed` : Slide 30 - 3 boîtes bleues avec sous-titres
- `grey_simple` : Slide 31 - 3 boîtes grises neutres

#### `08_pillars_builder.py`
- `blue_detailed` : Slide 34 - 4 boîtes bleues avec sous-titres (défaut)
- `blue_simple` : Slide 33 - 4 boîtes bleues simples
- `grey_detailed` : Slide 32 - 4 boîtes grises avec sous-titres
- `grey_simple` : Slide 35 - 4 boîtes grises simples

#### `09_comparison_builder.py`
- `blue_line` : Slide 39 - 2 énoncés avec ligne bleue (défaut)
- `grey_line` : Slide 40 - 2 énoncés avec ligne grise
- `detailed` : Slide 41 - 2 énoncés avec sous-titres
- `blue_variant` : Slide 42 - 2 énoncés ligne bleue variante
- `grey_variant` : Slide 43 - 2 énoncés ligne grise variante
- `illustrated` : Slide 37 - 2 énoncés avec image
- `concept_visual` : Slide 38 - Énoncé avec titre et image
- `detailed_pillars` : Slide 36 - 4 énoncés détaillés
- `structured_list` : Slide 44 - Liste structurée ligne bleue

#### `10_charts_builder.py`
- `simple_chart` : Slide 46 - Template graphique de base
- `bar_chart` : Slide 47 - Graphiques en barres (défaut)
- `pie_chart` : Slide 48 - Graphiques en secteurs
- `line_chart` : Slide 49 - Graphiques linéaires/temporels
- `data_table` : Slide 50 - Tableaux de données
- `complex_chart` : Slide 51 - Visualisations avancées

## 📚 Documentation Détaillée

Pour des instructions complètes, consultez :
- [Guide d'Utilisation des Scripts](../docs/Guide_Utilisation_Scripts_Presentation.md)
- [Guide de Création Premier Tech](../docs/Guide_Creation_Presentations_PT.md)

## 🔧 Avantages Techniques

- ✅ **Styles Premier Tech** 100% préservés
- ✅ **Méthode de clonage** éprouvée sans duplication
- ✅ **Insertion directe** dans présentations existantes
- ✅ **Sauvegardes automatiques** avant modifications
- ✅ **Traçabilité complète** avec rapports JSON
- ✅ **Validation** et exploration des templates
- ✅ **Workflow intégré** entre tous les scripts

## 📈 Scripts Développés vs Planifiés

### ✅ Scripts Terminés (10/10+)
- ✅ `01_slide_title_creator.py` - Couverture/Intro
- ✅ `02_navigation_builder.py` - Navigation
- ✅ `03_section_header_builder.py` - Nouvelle section
- ✅ `04_simple_message_builder.py` - Message simple
- ✅ `05_statistics_builder.py` - 2 statistiques
- ✅ `06_dashboard_builder.py` - 3-4 statistiques
- ✅ `07_content_boxes_builder.py` - 3 concepts égaux
- ✅ `08_pillars_builder.py` - 4 piliers/axes
- ✅ `09_comparison_builder.py` - Comparaisons A vs B
- ✅ `10_charts_builder.py` - **NOUVEAU** - Graphiques et visualisations

### 🚧 Prochains Scripts Planifiés
- `11_conclusion_builder.py` - Conclusions Premier Tech
- `12_agenda_builder.py` - Agendas et planning
- `13_timeline_builder.py` - Chronologies et roadmaps