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

**📖 Méthodologie complète d'adaptation :** [docs/strategie-diffusion-connaissances.md](docs/strategie-diffusion-connaissances.md)

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
**Générateur principal basé sur layout_name** avec architecture JSON moderne

### Outils Complémentaires
- **[tools/init_presentation.py](tools/init_presentation.py)** : Initialisation projets
- **[tools/slide_extractor.py](tools/slide_extractor.py)** : Extraction et validation
- **[tools/add_slide.py](tools/add_slide.py)** / **[tools/remove_slide.py](tools/remove_slide.py)** : Gestion dynamique
- **[tools/validation_checker.py](tools/validation_checker.py)** : Contrôle qualité PT

**📖 Documentation technique :** [archive/presentation_builder/README.md](archive/presentation_builder/README.md)

**⚠️ Scripts Archive :** [archive/presentation_builder/](archive/presentation_builder/) contient les scripts spécialisés 02-10 pour compatibilité, mais l'architecture layout-based via `presentation_builder.py` est recommandée.

## 📋 **Commandes Intégrées**

### 🤖 **Usage Autonome des Commandes**

**Toutes les commandes peuvent être utilisées de manière autonome** par Claude selon les besoins identifiés. Claude détermine automatiquement quelles commandes exécuter selon le contexte et peut enchaîner intelligemment les commandes dans l'ordre optimal.

### 🔄 **Ordre d'Exécution Recommandé**

Pour une présentation complète, l'ordre optimal est :

1. **[/initialize-presentation](.claude/commands/initialize-presentation.md)** ⭐ - Démarrage projet
2. **[/research-audience](.claude/commands/research-audience.md)** - Analyse audience (si nécessaire)
3. **[/research-presentation-data](.claude/commands/research-presentation-data.md)** - Recherche contenu (si nécessaire)
4. **[/adapt-content-for-audience](.claude/commands/adapt-content-for-audience.md)** - Adaptation intelligente
5. **[/create-presentation-plan](.claude/commands/create-presentation-plan.md)** - Plan stratégique
6. **[/add-slide](.claude/commands/add-slide.md)** - Ajout de slides (répétable)
7. **[/generate-presentation](.claude/commands/generate-presentation.md)** ⭐ - Génération finale avec validation

### Détail des Commandes

#### [/initialize-presentation](.claude/commands/initialize-presentation.md) ⭐
**Utilisation :** Démarrage d'un nouveau projet de présentation

```bash
/initialize-presentation "innovation-ai c-level"
```

**Claude orchestration automatique :**
- **Toujours exécuté :** Structure de base et validation
- **Si audience nouvelle :** Déclenche automatiquement `/research-audience`
- **Si sujet complexe :** Propose automatiquement `/research-presentation-data`
- **Si adaptation requise :** Suggère automatiquement `/adapt-content-for-audience`

#### [/research-audience](.claude/commands/research-audience.md)
**Usage autonome :** Analyse et documentation d'audience spécifique
**Déclenchement automatique :** Audience non documentée ou individu spécifique

#### [/research-presentation-data](.claude/commands/research-presentation-data.md)
**Usage autonome :** Recherche documentaire approfondie sur un sujet
**Déclenchement automatique :** Sujet technique complexe ou besoin documentaire identifié

#### [/adapt-content-for-audience](.claude/commands/adapt-content-for-audience.md)
**Usage autonome :** Adaptation de contenu pour audience spécifique
**Déclenchement automatique :** Après recherche documentaire pour optimiser l'adaptation

#### [/create-presentation-plan](.claude/commands/create-presentation-plan.md) 🆕
**Usage autonome :** Génération d'un plan stratégique de présentation
**Exécution recommandée :** Après `/adapt-content-for-audience`

#### [/add-slide](.claude/commands/add-slide.md) 🆕
**Usage autonome :** Ajout ou insertion de slides avec personnalisation automatique
**Exécution :** Selon les besoins pendant la création de présentation

#### [/generate-presentation](.claude/commands/generate-presentation.md) ⭐🆕
**Usage autonome :** Génération finale PowerPoint avec validation automatique complète
**Exécution finale :** Dernière étape du workflow avec contrôle qualité Premier Tech

**📖 Documentation complète :** Voir [.claude/commands/](.claude/commands/) pour détails techniques

## 📊 **Layouts Premier Tech Supportés**

**57 layouts authentiques Premier Tech** avec noms descriptifs pour configuration intuitive.

**📖 Liste complète :** [docs/reports/slide_structures_analysis_report.md](docs/reports/slide_structures_analysis_report.md)

### **Catégories Principales**
- **Slides de Base** : Page titre, Table des matières
- **Sections** : Titres avec numérotation et emphasis
- **Statistiques** : 2-4 KPI avec lignes bleues/grises
- **Boîtes de Contenu** : 3-4 concepts avec sous-titres
- **Branding PT** : Logos et signatures corporate

**Exemples d'usage layout-based :**
```json
{"layout_name": "Page titre", "shapes": [...]}
{"layout_name": "2 statistiques avec ligne bleue", "shapes": [...]}
{"layout_name": "3 boîtes bleues pour courts énoncés avec sous-titre", "shapes": [...]}
```

## 🚀 **Workflow Automatisé par Sujet**

### Structure Moderne par Projet
```
presentations/[sujet]/[audience]/
├── config.json                  # Configuration layout-based
├── README.md                    # Guide d'utilisation
├── data/                        # Recherches et datasets
└── output/                      # Présentation finale
```

### Workflow Orchestré Automatiquement

**Commande Unique :** `/initialize-presentation "innovation-ai c-level"`

**Claude orchestration intelligente :**
1. **Initialisation** : Structure et config.json layout-based
2. **Auto-détection** : Si audience/sujet nécessite recherche
3. **Recherche automatique** : Documentation et adaptation
4. **Configuration finale** : Layouts optimisés par audience
5. **Génération** : `python tools/presentation_builder.py config.json`

**📖 Méthodologie d'adaptation :** [docs/strategie-diffusion-connaissances.md](docs/strategie-diffusion-connaissances.md)

**📁 Structure détaillée :** [presentations/README.md](presentations/README.md)

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
├── tools/                      # Scripts layout-based principaux
├── .claude/commands/           # 7 commandes orchestrées
├── templates/                  # Template PT + structures
├── presentations/              # Projets [sujet]/[audience]/
├── docs/                       # Documentation spécialisée
│   ├── strategie-diffusion-connaissances.md  # Méthodologie
│   ├── reports/                # Analyses techniques
│   └── audience/              # Guides d'audience générés
├── tests/                      # Validations
└── archive/                    # Anciens scripts et outils
```

**📖 Documentation :** [docs/README.md](docs/README.md) pour navigation complète

## 🔄 **Setup et Utilisation**

### Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"
```

### 🚀 **Méthode Layout-Based (Moderne)**
```bash
# Workflow automatisé avec orchestration intelligente
/initialize-presentation "innovation-strategy c-level"
# Claude détermine automatiquement les commandes suivantes à exécuter

# Génération finale
python tools/presentation_builder.py presentations/innovation-strategy/c-level/config.json

# Validation technique (optionnelle)
python tools/slide_extractor.py output/innovation_strategy.pptx --slide-number 1
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
# Workflow automatisé avec orchestration Claude
/initialize-presentation "sujet audience"
# Les autres commandes sont déclenchées automatiquement selon le contexte

# Génération finale
python tools/presentation_builder.py config.json
```

### Projets d'Exemple Layout-Based
- **Configuration layout-based** : Layouts par noms descriptifs
- **Templates authentiques** : 57 slides Premier Tech préservés
- **Validation automatique** : Conformité corporate garantie

## 📚 **Ressources Techniques**

**Templates et Structures :**
- **[templates/presentation-project/slide-structure/](templates/presentation-project/slide-structure/)** : Structures par layout_name
- **[templates/presentation-project/content-brief.md.template](templates/presentation-project/content-brief.md.template)** : Template adaptation audience

**Documentation Technique :**
- **[docs/technical-reports/POWERPOINT_FORMATTING_EXTRACTION_REPORT.md](docs/technical-reports/POWERPOINT_FORMATTING_EXTRACTION_REPORT.md)** : Analyse architecture layout-based
- **[docs/strategie-diffusion-connaissances.md](docs/strategie-diffusion-connaissances.md)** : Méthodologie complète d'adaptation

**Validation et Test :**
- **[tools/slide_extractor.py](tools/slide_extractor.py)** : Validation bidirectionnelle
- **[tools/validation_checker.py](tools/validation_checker.py)** : Conformité Premier Tech

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