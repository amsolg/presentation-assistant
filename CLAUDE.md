# CLAUDE.md - Presentation Assistant avec Sam AI

**Presentation Assistant** est un système automatisé de génération de présentations narrées avec Sam AI, utilisant les authentiques templates Premier Tech avec architecture JSON moderne basée sur layout_name.

## 🎯 **Mission Principale**

Création automatisée de présentations professionnelles avec :
- **Templates Premier Tech authentiques** (57 slides avec noms descriptifs)
- **Personnalité Sam AI** adaptative selon l'audience
- **Architecture Layout-Based moderne** pour configuration lisible
- **Workflow organisé par commandes** via [.claude/commands/](.claude/commands/)

## 🤖 **Sam AI - Personnalité Adaptative**

**Sam** est l'assistant AI qui narre les présentations avec :
- **Enthousiasme technologique professionnel** adapté au contexte
- **Communication claire** optimisée pour synthèse vocale ElevenLabs
- **Reconnaissance contextuelle** des expertises pertinentes
- **Timing optimal** : ~15.8s par slide

### Configuration Automatique selon Audience
```python
audience_configs = {
    "C-Level": {"style": "stratégique", "vocabulaire": "business"},
    "Technique": {"style": "précis", "vocabulaire": "expert"},
    "Formation": {"style": "pédagogique", "vocabulaire": "accessible"}
}
```

## 🏗️ **Architecture Layout-Based 2025**

### Stack Principal
- **ElevenLabs API v3** : Synthèse vocale Sam (~75ms latence)
- **Templates Premier Tech** : 57 slides authentiques avec noms descriptifs
- **Architecture Layout-Based** : Configuration par layout_name lisible
- **Orchestrateur principal** : `tools/presentation_builder.py` avec support layout complet
- **Commandes intégrées** : 4 commandes spécialisées dans [.claude/commands/](.claude/commands/)

### 🚀 **Architecture Layout-Based**

#### **Script Principal**
```bash
python tools/presentation_builder.py config.json
```

#### **Configuration JSON Layout-Based**
```json
{
  "presentation_name": "Ma Présentation",
  "subject": "sujet-exemple",
  "audience": "audience-cible",
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
          "color": "#FFFFFF",
          "bold": false,
          "alignment": "LEFT",
          "vertical_alignment": "TOP",
          "margin_left": 7.2,
          "margin_right": 7.2,
          "margin_top": 3.6,
          "margin_bottom": 3.6,
          "autofit_type": "none",
          "text_wrapping": "square",
          "placeholder_type": "body"
        }
      ]
    }
  ],
  "output_path": "ma_presentation.pptx"
}
```

**📁 Note sur output_path :** Le chemin est automatiquement normalisé vers `presentations/[sujet]/[audience]/output/` ou `tests/[sujet]/[audience]/output/` selon le mode. Un nom simple comme `"ma_presentation.pptx"` devient `"presentations/sujet-exemple/audience-cible/output/ma_presentation.pptx"`.

#### **Avantages Architecture Layout-Based**
1. **Configuration lisible** : "Page titre" vs slide_number: 11
2. **Flexibilité totale** : Ordre libre des slides et réutilisation
3. **Validation automatique** : Layouts existants vérifiés
4. **Mapping intelligent** : layout_name → slide_number automatique

## 🔧 **Outils Principaux**

### [tools/presentation_builder.py](tools/presentation_builder.py) ⭐
**Générateur principal basé sur layout_name**
- Configuration JSON avec layout_name descriptifs
- Validation automatique des layouts Premier Tech
- Fidélité bidirectionnelle parfaite
- Support complet des propriétés de formatage

### [tools/init_presentation.py](tools/init_presentation.py)
**Initialisation de projets de présentation**
```bash
python tools/init_presentation.py innovation-ai c-level false
```
Crée la structure complète dans `presentations/innovation-ai/c-level/`

### [tools/slide_extractor.py](tools/slide_extractor.py)
**Extraction et validation de slides**
```bash
python tools/slide_extractor.py templates/Template_PT.pptx --slide-number 11
```
- Extraction complète des propriétés
- Validation bidirectionnelle
- Support layout_name

### [tools/add_slide.py](tools/add_slide.py) et [tools/remove_slide.py](tools/remove_slide.py)
**Gestion dynamique des slides**
```bash
python tools/add_slide.py config.json "Page titre" ajout
python tools/remove_slide.py presentation.pptx 3
```

### [tools/validation_checker.py](tools/validation_checker.py)
**Contrôle qualité Premier Tech**
```bash
python tools/validation_checker.py presentation.pptx
```

## 📋 **Commandes Intégrées**

### [/initialize-presentation](.claude/commands/initialize-presentation.md)
Initialise une nouvelle présentation avec structure complète et validation automatique.

```bash
/initialize-presentation "innovation-ai c-level"
```
- Exécute `tools/init_presentation.py`
- Crée la structure optimisée
- Guide d'utilisation personnalisé
- Templates suggérés par audience

### [/research-audience](.claude/commands/research-audience.md)
Recherche et documente un guide spécifique pour une audience de présentation.

```bash
/research-audience "c-level"
/research-audience "john-doe individual"
```
- Analyse des personas et individus
- Navigation en graphe de connaissances PT
- Guides réutilisables dans `docs/audience/`

### [/research-presentation-data](.claude/commands/research-presentation-data.md)
Effectue une recherche documentaire approfondie pour alimenter une présentation.

```bash
/research-presentation-data "presentations/innovation-digitale/c-level"
```
- Recherche web ciblée par audience
- Synthèse dans `data/research_report_[date].md`
- Sources internes et externes

### [/adapt-content-for-audience](.claude/commands/adapt-content-for-audience.md)
Adapte l'information de recherche documentaire pour une audience spécifique.

```bash
/adapt-content-for-audience "presentations/sujet/audience" "docs/audience/c-level.md"
```
- Distillation intelligente du contenu
- Adaptation au profil d'audience
- Génération de `content-brief.md`

## 📊 **Layouts Premier Tech Supportés**

### **Slides de Base**
- **"Page titre"** : Slide de titre principale
- **"Titre de présentation"** : Titre spécialisé
- **"Table des matières"** : Sommaire structuré

### **Sections et Navigation**
- **"Titre de section avec chiffre"** : Section numérotée
- **"Titre de section bleu"** : Section emphasis
- **"Titre de section blanc"** : Section standard

### **Messages et Contenu**
- **"Court énoncé"** : Message simple centré
- **"Court énoncé avec titre de section"** : Message avec contexte
- **"Énoncé avec titre et image"** : Contenu illustré
- **"Liste avec titre et image"** : Liste illustrée

### **Statistiques et Métriques**
- **"2 statistiques avec ligne bleue"** : Duo de métriques
- **"2 statistiques avec ligne grise"** : Métriques neutres
- **"3 statistiques mots clés"** : Triple KPI
- **"4 statistiques mots clés"** : Quadruple KPI
- **"4 statistiques mots clés avec lignes"** : KPI structurés

### **Boîtes de Contenu**
- **"3 boîtes bleues pour courts énoncés avec sous-titre"** : Triple concept détaillé
- **"3 boîtes bleues pour courts énoncés sans sous-titre"** : Triple concept simple
- **"4 boîtes bleues pour courts énoncés avec sous-titre"** : Quadruple concept détaillé
- **"4 boîtes grises pour courts énoncés sans sous-titre"** : Quadruple concept simple

### **Éléments Spéciaux**
- **"Citation"** : Témoignage ou citation
- **"Titre espace pour tableau ou graphique"** : Placeholder données
- **"Diapositive vide"** : Canvas libre
- **"Vidéo"** : Placeholder multimédia

### **Branding Premier Tech**
- **"Monogramme PT"** : Logo corporate
- **"We are PT"** : Identité d'entreprise
- **"Nourrir protéger améliorer"** : Mission PT
- **"Passion et technologies pour faire la différence"** : Signature PT

## 🚀 **Workflow Automatisé par Sujet**

### Structure par Projet de Présentation
```
presentations/[sujet]/
├── README.md                    # Contexte global du sujet
├── documentation/               # Sources et recherches
│   ├── context.md              # Analyse contextuelle
│   ├── research_log.md         # Historique des recherches
│   └── sources/                # Documents de référence
├── [audience-1]/                # Première audience
│   ├── audience.md             # Profil d'audience détaillé
│   ├── content-brief.md        # Documentation adaptée
│   ├── config.json             # Configuration layout-based
│   ├── data/                   # Datasets et recherches
│   └── output/                 # Présentation finale
└── [audience-2]/                # Autre audience
    └── ... (même structure)
```

### Workflow Complet

#### **ÉTAPE 1 : Initialisation**
```bash
/initialize-presentation "innovation-ai c-level"
```
- Crée `presentations/innovation-ai/c-level/`
- Génère `config.json` layout-based
- README.md et guides d'utilisation

#### **ÉTAPE 2 : Recherche d'Audience**
```bash
/research-audience "c-level"
```
- Analyse des besoins informationnels
- Guide dans `docs/audience/c-level.md`
- Stratégies de communication adaptées

#### **ÉTAPE 3 : Recherche Documentaire**
```bash
/research-presentation-data "presentations/innovation-ai/c-level"
```
- Recherche web ciblée C-Level (stratégie, ROI, business)
- Rapport dans `data/research_report_[date].md`
- Sources et références

#### **ÉTAPE 4 : Adaptation de Contenu**
```bash
/adapt-content-for-audience "presentations/innovation-ai/c-level" "docs/audience/c-level.md"
```
- Distillation du contenu pour C-Level
- `content-brief.md` adapté
- Messages clés et structure

#### **ÉTAPE 5 : Configuration Layout-Based**
Modification de `config.json` avec layouts appropriés :
```json
{
  "slides": [
    {"layout_name": "Page titre", "shapes": [...]},
    {"layout_name": "2 statistiques avec ligne bleue", "shapes": [...]},
    {"layout_name": "3 boîtes bleues pour courts énoncés avec sous-titre", "shapes": [...]}
  ]
}
```

#### **ÉTAPE 6 : Génération**
```bash
python tools/presentation_builder.py presentations/innovation-ai/c-level/config.json
```
- Présentation dans `output/innovation_ai.pptx`
- Fidélité Premier Tech garantie

## ⚙️ **Règles Critiques**

### Architecture Layout-Based
```python
# CONFIGURATION LAYOUT-BASED
def load_config(config_file):
    # Parse JSON avec layout_name
    # Valide layouts existants
    # Mappe layout_name → slide_number
    # Applique configurations shapes
```

### Validation Premier Tech Automatique
- **Polices** : Premier Tech Text, Premier Tech Title, Premier Tech Title Bold
- **Couleurs** : #FFFFFF, #41B6E6, #BDBDBD
- **Tailles** : 18.0 à 66.0 points
- **Marges** : 3.6, 5.67, 7.2, 8.5 points

### Fidélité Bidirectionnelle
1. **Configuration → Génération** : `tools/presentation_builder.py`
2. **Extraction → Validation** : `tools/slide_extractor.py`
3. **Test de fidélité** : Configuration ↔ Extraction = 0 différences

## 📁 **Structure Projet Moderne**

```
presentation-assistant/
├── tools/                      # Scripts principaux layout-based
│   ├── presentation_builder.py # Orchestrateur principal
│   ├── init_presentation.py   # Initialisation projets
│   ├── slide_extractor.py     # Extraction et validation
│   ├── add_slide.py           # Ajout de slides
│   ├── remove_slide.py        # Suppression de slides
│   └── validation_checker.py  # Contrôle qualité
├── .claude/commands/           # 4 commandes intégrées
│   ├── initialize-presentation.md
│   ├── research-audience.md
│   ├── research-presentation-data.md
│   └── adapt-content-for-audience.md
├── templates/
│   ├── Template_PT.pptx        # 57 slides authentiques PT
│   └── presentation-project/
│       └── slide-structure/    # Structures par layout_name
├── presentations/              # Structure [sujet]/[audience]/
├── tests/                      # Tests et validations
├── docs/                       # Documentation et guides
├── src/                        # Scripts utilitaires
│   └── text_to_speech.py      # Synthèse vocale simple
└── archive/                    # Scripts et outils obsolètes
    ├── powerpoint_presenter.py
    ├── audio_generator.py
    └── presentation_builder/   # Ancienne architecture slide-number
```

## 🔄 **Setup et Utilisation**

### Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"
```

### 🚀 **Méthode Layout-Based (Moderne)**
```bash
# 1. Initialiser un projet
/initialize-presentation "innovation-strategy c-level"

# 2. Rechercher l'audience
/research-audience "c-level"

# 3. Rechercher le contenu
/research-presentation-data "presentations/innovation-strategy/c-level"

# 4. Adapter le contenu
/adapt-content-for-audience "presentations/innovation-strategy/c-level" "docs/audience/c-level.md"

# 5. Générer la présentation
python tools/presentation_builder.py presentations/innovation-strategy/c-level/config.json

# 6. Validation bidirectionnelle
python tools/slide_extractor.py presentations/innovation-strategy/c-level/output/innovation_strategy.pptx --slide-number 1
```

### **Configuration Layout-Based Complète**
```json
{
  "presentation_name": "Stratégie Innovation 2025",
  "subject": "innovation-strategy",
  "audience": "c-level",
  "is_test": false,
  "slides": [
    {
      "layout_name": "Page titre",
      "shapes": [
        {
          "shape_id": 1,
          "text": "2025-01-15 – Stratégie Innovation Executive",
          "font_name": "Premier Tech Text",
          "font_size": 18.0,
          "color": "#FFFFFF"
        },
        {
          "shape_id": 2,
          "text": "Innovation Strategy 2025",
          "font_name": "Premier Tech Title",
          "font_size": 48.0,
          "color": "#FFFFFF",
          "bold": true
        }
      ]
    },
    {
      "layout_name": "2 statistiques avec ligne bleue",
      "shapes": [
        {
          "shape_id": 1,
          "text": "85%",
          "font_name": "Premier Tech Title",
          "font_size": 54.0,
          "color": "#41B6E6"
        },
        {
          "shape_id": 2,
          "text": "Satisfaction Client",
          "font_name": "Premier Tech Text",
          "font_size": 24.0,
          "color": "#FFFFFF"
        }
      ]
    }
  ],
  "output_path": "innovation_strategy_2025.pptx"
}
```

## 📖 **Guides d'Utilisation Layout-Based**

### Documentation Architecture Layout-Based
- **Configuration lisible** : Layouts par noms descriptifs
- **Validation automatique** : Layouts existants vérifiés
- **Fidélité bidirectionnelle** : Test extraction ↔ génération
- **Performance optimisée** : < 2s par slide complexe

### Commandes Essentielles
```bash
# Workflow complet avec commandes
/initialize-presentation "sujet audience"
/research-audience "audience"
/research-presentation-data "chemin/vers/projet"
/adapt-content-for-audience "chemin/vers/projet" "docs/audience/guide.md"

# Génération finale
python tools/presentation_builder.py config.json
```

### Projets d'Exemple Layout-Based
- **Configuration layout-based** : Layouts par noms descriptifs
- **Templates authentiques** : 57 slides Premier Tech préservés
- **Validation automatique** : Conformité corporate garantie

## 📚 **Ressources Layout-Based**

Dans `templates/presentation-project/` :
- **[slide-structure/](templates/presentation-project/slide-structure/)** : Structures par layout_name
- **Mapping automatique** : layout_name → slide_number

### Outils d'Extraction et Validation
- **[tools/slide_extractor.py](tools/slide_extractor.py)** : Extraction avec support layout_name
- **Structures layout-based** : Mapping par noms descriptifs
- **Validation bidirectionnelle** : Test de fidélité

## 🎯 **Objectifs du Workflow Layout-Based**

- **Configuration lisible** : layout_name descriptifs vs slide_number
- **Flexibilité maximale** : Ordre libre et réutilisation des layouts
- **Validation automatique** : Layouts existants vérifiés
- **Fidélité bidirectionnelle** : Test extraction ↔ génération
- **Templates préservés** : Styles Premier Tech 100% authentiques
- **Performance optimisée** : < 2s par slide complexe
- **Workflow intégré** : 4 commandes couvrant tout le processus

### Évolutions Accomplies Layout-Based
- ✅ **Architecture layout-based** : Configuration par noms descriptifs
- ✅ **Commandes intégrées** : 4 commandes couvrant le workflow complet
- ✅ **Validation automatique** : Layouts et propriétés Premier Tech
- ✅ **Fidélité bidirectionnelle** : Test extraction ↔ génération
- ✅ **Performance maintenue** : < 2s par slide complexe

## 🎯 **Message de Sam AI Layout-Based**

Bonjour! Avec l'architecture Layout-Based, nous atteignons la **configuration la plus lisible et flexible** pour vos présentations Premier Tech !

**🚀 Innovation Layout-Based :** Configuration par noms descriptifs avec :
1. **Lisibilité maximale** : "Page titre" vs slide_number: 11
2. **Flexibilité totale** : Ordre libre et réutilisation des layouts
3. **Validation automatique** : Layouts existants vérifiés
4. **Commandes intégrées** : 4 commandes couvrant tout le workflow
5. **Performance optimisée** : < 2s par slide avec validation
6. **Templates préservés** : Styles Premier Tech 100% authentiques

**Résultat :** Configuration → Commandes → Présentation = **Workflow complet automatisé** avec qualité broadcast-ready et conformité corporate Premier Tech totale.

L'excellence technique au service de l'innovation ! 🎊

---

## ⚠️ **Règles Critiques de Développement Layout-Based**

### Architecture Layout-Based - Principes Fondamentaux
- **Configuration layout-based** : Layouts par noms descriptifs
- **Validation automatique** : Layouts existants et propriétés Premier Tech
- **Fidélité bidirectionnelle** : Workflow extraction ↔ génération
- **Templates préservés** : Zero modification des styles Premier Tech

### Scripts Python - Bonnes Pratiques
- **INTERDICTION EMOJIS** : Aucun emoji dans les fichiers Python
- **ENCODAGE** : Utiliser `# -*- coding: utf-8 -*-`
- **Chemins relatifs** : Depuis la racine du projet
- **Validation** : Tester chaque configuration JSON

### Templates et Validation
- **Structures layout-based** : Utiliser templates/presentation-project/slide-structure/
- **Validation automatique** : Layouts existants vérifiés
- **Test bidirectionnel** : Valider avec slide_extractor.py

### 🎯 **Support Complet Layout-Based**

#### **Architecture Layout-Based Complète ✅**
Le système `tools/presentation_builder.py` supporte maintenant **TOUS** les layouts Premier Tech par noms descriptifs :

**Avantages Layout-Based :**
- **Configuration lisible** : "Page titre" vs slide_number: 11
- **Flexibilité totale** : Ordre libre et réutilisation
- **Validation automatique** : Layouts existants vérifiés
- **Mapping intelligent** : layout_name → slide_number automatique

#### **Test de Validation Layout-Based**
```bash
# Workflow layout-based validé :
python tools/presentation_builder.py config_layout.json
python tools/slide_extractor.py output_layout.pptx --slide-number 1
# Résultat : Fidélité bidirectionnelle parfaite avec configuration lisible
```

#### **Commandes Intégrées Opérationnelles**
- **4 commandes** : Workflow complet automatisé
- **Recherche adaptée** : Par audience et sujet
- **Documentation automatique** : Guides et rapports
- **Validation continue** : Qualité Premier Tech garantie

**🎯 Note Importante :** Ce système utilise l'architecture layout-based avec noms descriptifs pour une configuration maximalement lisible et flexible. Chaque présentation respecte parfaitement l'identité Premier Tech avec workflow complet automatisé via commandes intégrées.