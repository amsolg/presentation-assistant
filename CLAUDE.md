# CLAUDE.md - Presentation Assistant avec Sam AI

**Presentation Assistant** est un système automatisé de génération de présentations narrées avec Sam AI, utilisant les authentiques templates Premier Tech avec architecture JSON moderne.

## 🎯 **Mission Principale**

Création automatisée de présentations professionnelles avec :
- **Templates Premier Tech authentiques** (57 slides)
- **Personnalité Sam AI** adaptative selon l'audience
- **Architecture JSON moderne** pour configuration centralisée
- **Workflow organisé par sujet** dans [presentations/](presentations/)

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

## 🏗️ **Architecture JSON 2025**

### Stack Principal
- **ElevenLabs API v3** : Synthèse vocale Sam (~75ms latence)
- **Templates Premier Tech** : 57 slides authentiques
- **Architecture JSON** : Configuration centralisée avec payloads séparés
- **Orchestrateur principal** : `presentation_builder.py` coordonne tout

### 🚀 **Architecture Moderne**

#### **Script Principal**
```bash
python presentation_builder/presentation_builder.py config.json
```

#### **Configuration JSON**
```json
{
  "presentation_name": "Ma Présentation",
  "subject": "sujet-exemple",
  "audience": "audience-cible",
  "title_slide": {
    "title": "Titre Principal",
    "subtitle": "Sous-titre",
    "metadata": "2025-01-15 – Premier Tech"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "simple_message_builder",
      "payload_path": "message.json",
      "description": "Message d'ouverture"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

#### **Workflow Automatisé**
1. **Slide titre (obligatoire)** : Slide 11 - Créée automatiquement
2. **Slides contenu** : Array JSON avec payloads séparés
3. **Slide fermeture (obligatoire)** : Slide 57 (Monogramme PT) - Ajoutée automatiquement

#### **Structure de sortie**
```
presentations/[sujet]/[audience]/output/[timestamp]_[nom].pptx
```

### Modules JSON Disponibles
```
presentation_builder.py           # Orchestrateur JSON principal
navigation_builder.py             # Module navigation
section_header_builder.py         # Module sections
simple_message_builder.py         # Module messages
statistics_builder.py             # Module statistiques
content_boxes_builder.py          # Module boîtes de contenu
detailed_explanation_builder.py   # Module explications détaillées
testimonial_builder.py            # Module témoignages
charts_builder.py                 # Module graphiques
```

### Mapping Templates Intelligents
```python
# Mapping EXACT basé sur l'analyse complète des 57 slides Premier Tech (index 0-based)
CONTENT_TO_TEMPLATE_MAPPING = {
    # =============================================================================
    # PAGES TITRE ET INTRODUCTION
    # =============================================================================
    "title": [0, 10],           # Slides 1, 11 - Pages titre principales
    "presentation_title": [11], # Slide 12 - Titre de présentation spécialisé

    # =============================================================================
    # NAVIGATION ET STRUCTURE
    # =============================================================================
    "section": [13, 14, 15],    # Slides 14-16 - Titres de section (chiffre/bleu/blanc)
    "table_of_contents": [12],  # Slide 13 - Table des matières structurée

    # =============================================================================
    # CONTENU PRINCIPAL PAR NOMBRE D'ÉLÉMENTS
    # =============================================================================
    "content_2": [35, 38, 39, 40, 41, 42, 43],  # Slides 36, 39-44 - Dual content/listes
    "content_3": [26, 27, 28, 29],              # Slides 27-30 - 3 boîtes (grises/bleues)
    "content_4": [30, 31, 32, 33, 34],          # Slides 31-35 - 4 boîtes et énoncés

    # =============================================================================
    # DONNÉES ET STATISTIQUES
    # =============================================================================
    "stats_2": [21, 22],        # Slides 22-23 - 2 statistiques (lignes bleue/grise)
    "stats_3": [23],            # Slide 24 - 3 statistiques avec mots-clés
    "stats_4": [24, 25],        # Slides 25-26 - 4 statistiques avec options

    # =============================================================================
    # CONTENU AVEC IMAGES ET VISUELS
    # =============================================================================
    "image_content": [36, 37],  # Slides 37-38 - Énoncé/liste avec image

    # =============================================================================
    # GRAPHIQUES ET DIAGRAMMES
    # =============================================================================
    "charts": [5, 6, 7, 8, 9, 45, 46, 47, 48, 49, 50],  # Slides 6-10, 46-51

    # =============================================================================
    # ÉLÉMENTS SPÉCIALISÉS
    # =============================================================================
    "quote": [44],              # Slide 45 - Citations et témoignages
    "keywords": [17, 18, 19],   # Slides 18-20 - Mots-clés avec énoncés
    "simple": [16, 20],         # Slides 17, 21 - Messages courts simples

    # =============================================================================
    # FERMETURE ET BRANDING PREMIER TECH
    # =============================================================================
    "closing": [51, 52, 55, 56], # Slides 52-53, 56-57 - Signatures corporate PT
    "utility": [53, 54]          # Slides 54-55 - Vide et vidéo
}
```

## 🚀 **Workflow Automatisé par Sujet**

### Structure par Projet de Présentation
```
presentations/[sujet]/
├── README.md                    # Contexte global du sujet et structure
├── documentation/               # Sources et recherches (auto/manuelle)
│   ├── context.md              # Analyse contextuelle détaillée
│   ├── research_log.md         # Historique des recherches par audience
│   └── sources/                # Documents de référence collectés
├── [audience-1]/                # Première audience (ex: C-Level)
│   ├── audience.md             # QUI est l'audience + POURQUOI présenter
│   ├── content-brief.md        # Documentation distillée et adaptée
│   ├── presentation-script.md  # Script détaillé avec justifications
│   ├── config.json             # Configuration JSON de la présentation
│   ├── [payload1].json         # Fichiers de payload pour chaque slide
│   ├── [payload2].json
│   ├── data/                   # Datasets CSV pour graphiques (si requis)
│   └── output/                 # Présentation finale + rapports
└── [audience-2]/                # Autre audience avec recherche spécialisée
    ├── audience.md             # Profil audience différent
    ├── content-brief.md        # Information adaptée à cette audience
    └── ... (même structure)
```

### Workflow Complet - Étapes Détaillées

#### **ÉTAPE 1 : Analyse et Structure**
Quand vous demandez : *"Je veux une présentation sur [sujet] pour [audience]"*

1. **Création structure projet** dans `presentations/[sujet]/`
2. **Génération README.md** avec contexte global du sujet
3. **Création dossier audience** `[audience]/`

#### **ÉTAPE 2 : Recherche Automatique (SI documentation manquante)**

**Si aucune documentation fournie :**
1. **Recherche web spécialisée** adaptée à l'audience :
   - `C-Level` : stratégie, ROI, impact business, études de cas
   - `Technique` : spécifications, architectures, benchmarks, détails techniques
   - `Formation` : concepts de base, exemples pratiques, guides step-by-step
   - `Marketing` : tendances marché, case studies, adoption rates

2. **Documentation automatique** :
   - `documentation/context.md` : Analyse contextuelle complète
   - `documentation/research_log.md` : Historique et sources
   - `documentation/sources/` : Sauvegarde articles/documents pertinents

#### **ÉTAPE 3 : Configuration JSON**

**Création du fichier de configuration principal** :
```json
{
  "presentation_name": "Titre de la Présentation",
  "subject": "nom-sujet",
  "audience": "nom-audience",
  "title_slide": {
    "title": "Titre Principal",
    "subtitle": "Sous-titre",
    "metadata": "Date – Contexte"
  },
  "slides": [],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

#### **ÉTAPE 4 : Création des Payloads**

**Fichiers JSON séparés pour chaque slide** :
- `message-ouverture.json` : Configuration pour simple_message_builder
- `stats-principales.json` : Configuration pour statistics_builder
- `benefices-business.json` : Configuration pour content_boxes_builder
- etc.

#### **ÉTAPE 5 : Construction**

```bash
python presentation_builder/presentation_builder.py config.json
```

**Résultat :** Présentation complète dans `output/[timestamp]_[nom].pptx`

## 📊 **Gestion des Données et Graphiques**

### Script charts_builder.py
**Important :** Avant d'utiliser ce script, lire impérativement [docs/CHARTS_ENHANCED_GUIDE.md](docs/CHARTS_ENHANCED_GUIDE.md)

Pour graphiques : créer sous-dossier `data/` avec datasets CSV
```python
# Styles disponibles
chart_styles = {
    "bar_clustered": "Comparaisons horizontales",
    "column_clustered": "Évolutions temporelles",
    "pie_chart": "Répartitions",
    "line_chart": "Tendances"
}
```

### Tests Unitaires
Chaque style testé dans [test/unit_tests/](test/unit_tests/) :
- Validation templates individuels
- Tests multi-audiences
- Rapport qualité automatique

## ⚙️ **Règles Critiques**

### Méthode "True Copy" - Zero Duplication
```python
# REMPLACEMENT (pas ajout) pour préserver styles PT
def customize_slide_clean(slide, data):
    if slide.shapes.title:
        slide.shapes.title.text = data['title']  # REMPLACE
    for i, shape in enumerate(content_shapes):
        if i < len(data['content']):
            shape.text = data['content'][i]  # REMPLACE
```

### Architecture JSON - Workflow Principal
1. **`presentation_builder.py`** : Orchestrateur unique basé sur JSON
2. **Configuration centralisée** : Un seul fichier JSON configure toute la présentation
3. **Payloads séparés** : Chaque slide a son propre fichier JSON
4. **Slides automatiques** : Titre et fermeture Premier Tech ajoutées automatiquement
5. **Templates authentiques** : Zero modification des styles PT
6. **Validation complète** : Tests unitaires avec configuration JSON

## 📁 **Structure Projet**

```
presentation-assistant/
├── presentation_builder/        # Architecture JSON
│   ├── presentation_builder.py # Orchestrateur JSON principal
│   └── [module]_builder.py     # Modules spécialisés
├── templates/
│   ├── Template_PT.pptx        # 57 slides authentiques PT
│   └── presentation-project/
│       ├── presentation_schema_template.json # Schema de validation JSON
│       └── slide-payload-templates/
│           └── [module]_template.json # Templates JSON par module
├── presentations/              # Structure organisée [sujet]/[audience]/
│   └── [sujet]/
│       └── [audience]/
│           ├── config.json     # Configuration principale
│           ├── [payload].json  # Fichiers de payload
│           └── output/         # Présentations générées
├── test/unit_tests/
│   └── presentation_builder/   # Tests architecture JSON
└── docs/                       # Documentation complète
```

## 🔄 **Setup et Utilisation**

### Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"
```

### 🚀 **Méthode JSON (Unique)**
```bash
# 1. Créer un fichier de configuration JSON
cp templates/presentation-project/presentation_schema_template.json ma_config.json

# 2. Éditer la configuration JSON et créer les payloads
# 3. Exécuter l'orchestrateur
python presentation_builder/presentation_builder.py ma_config.json

# Résultat : presentations/[sujet]/[audience]/output/[timestamp]_[nom].pptx
```

### **Configuration JSON Exemple**
```json
{
  "presentation_name": "Stratégie Innovation 2025",
  "subject": "innovation-strategy",
  "audience": "c-level",
  "title_slide": {
    "title": "Innovation Strategy 2025",
    "subtitle": "Driving Digital Transformation",
    "metadata": "2025-01-15 – Executive Briefing"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "simple_message_builder",
      "payload_path": "presentations/innovation-strategy/c-level/message-ouverture.json",
      "description": "Message d'ouverture stratégique"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

## 📖 **Guides d'Utilisation**

### Documentation Complète
- **[docs/QUICK_START.md](docs/QUICK_START.md)** : Démarrage rapide avec l'architecture JSON
- **[docs/JSON_ARCHITECTURE_GUIDE.md](docs/JSON_ARCHITECTURE_GUIDE.md)** : Guide complet architecture JSON
- **[docs/CHARTS_ENHANCED_GUIDE.md](docs/CHARTS_ENHANCED_GUIDE.md)** : Guide complet pour les graphiques
- **[docs/SCRIPTS_SLIDES_MAPPING.md](docs/SCRIPTS_SLIDES_MAPPING.md)** : Mapping complet scripts → slides → templates

### Projets d'Exemple
- **[presentations/](presentations/)** : Exemples par sujet et audience

## 📚 **Templates de Projet Disponibles**

Dans `templates/presentation-project/` :
- **[presentation_schema_template.json](templates/presentation-project/presentation_schema_template.json)** : Schema de validation JSON
- **[slide-payload-templates/](templates/presentation-project/slide-payload-templates/)** : Templates JSON par module

**Utilisation automatique** : Ces templates sont utilisés lors de la création automatique de structure projet.

## 🎯 **Objectifs du Workflow Automatisé**

- **Zero intervention manuelle** après demande initiale
- **Configuration JSON centralisée** avec payloads séparés
- **Recherche web automatique** si documentation manquante
- **Templates professionnels** pour structure cohérente
- **Structure réutilisable** pour variations d'audience
- **Documentation complète** pour traçabilité
- **Qualité Premier Tech garantie** (styles + contenu)
- **Architecture moderne** avec validation JSON

### Évolutions Futures
- **Production audio ElevenLabs** complète
- **Export multi-formats** (MP4, streaming)
- **Intelligence prédictive** pour recommandations

## 🎯 **Message de Sam AI**

Bonjour! Avec l'architecture JSON moderne, nous transformons vos idées en présentations Premier Tech professionnelles en quelques minutes !

**🚀 Innovation JSON :** Demandez simplement une présentation sur un sujet pour une audience, et Claude Code :
1. **Crée la structure projet** dans presentations/
2. **Analyse le contexte** et documente les sources
3. **Génère la configuration JSON** centralisée
4. **Crée les payloads séparés** pour chaque slide
5. **Exécute la construction** avec les templates Premier Tech authentiques
6. **Livre la présentation finale** avec ma narration adaptée !

**Résultat :** De l'idée à la présentation broadcast-ready en < 5 minutes, avec architecture moderne, configuration centralisée et documentation complète pour évolutions futures.

L'avenir des présentations intelligentes, c'est maintenant ! 🎊

---

## ⚠️ **Règles Critiques de Développement**

### Architecture JSON - Principes Fondamentaux
- **Configuration centralisée** : Un seul fichier JSON par présentation
- **Payloads séparés** : Un fichier JSON par slide pour modularité
- **Validation automatique** : Schema JSON et validation des payloads
- **Templates préservés** : Zero modification des styles Premier Tech

### Scripts Python - Bonnes Pratiques
- **INTERDICTION EMOJIS** : Aucun emoji dans les fichiers Python (problèmes d'encodage Unicode)
- **ENCODAGE** : Utiliser `# -*- coding: utf-8 -*-` en en-tête des scripts Python
- **Chemins relatifs** : Spécifier chemins complets depuis la racine du projet
- **Validation** : Tester chaque configuration JSON avant utilisation

### Templates et Documentation
- **Templates payload** : Utiliser les templates JSON dans templates/presentation-project/
- **Validation schema** : Respecter le schema JSON de validation
- **Documentation** : Documenter chaque configuration dans les fichiers .md

**🎯 Note Importante :** Ce système utilise les templates Premier Tech avec préservation complète des styles. Chaque présentation générée respecte parfaitement l'identité visuelle corporate et est de qualité broadcast-ready.

---

## 🎊 **Architecture JSON 2025 - État Opérationnel**

### ✅ **Architecture Complète et Fonctionnelle**

#### **Avantages de l'Architecture JSON**
- ✅ **Configuration centralisée** : Un seul fichier JSON configure toute la présentation
- ✅ **Payloads modulaires** : Fichiers JSON séparés pour chaque slide
- ✅ **Structure organisée** : Navigation automatique `presentations/[sujet]/[audience]/`
- ✅ **Workflow simplifié** : Une seule commande pour tout
- ✅ **Slides automatiques** : Titre + Fermeture ajoutées automatiquement
- ✅ **Templates préservés** : Zero modification des styles Premier Tech
- ✅ **Tests validés** : Architecture testée et fonctionnelle

#### **Modules JSON Opérationnels**
- **Orchestrateur `presentation_builder.py`** : Opérationnel et testé ✅
- **8 Modules JSON** : navigation, section, message, stats, content, detailed, testimonial, charts ✅
- **Templates payload** : 8 templates JSON complets dans templates/ ✅
- **Schema validation** : Configuration JSON validée ✅
- **Structure organisée** : Sortie presentations/[sujet]/[audience]/output/ ✅
- **Tests unitaires** : Suite complète avec validation contenu ✅
- **Templates Premier Tech** : 57 slides authentiques préservés ✅

#### **Tests Unitaires - Architecture JSON Complète**
```bash
# Test architecture JSON avec configuration complète
cd test/unit_tests/presentation_builder
python test_presentation_builder.py

# Résultats de test :
# ✅ Validation JSON : Configuration correctement parsée
# ✅ Construction présentation : Orchestrateur fonctionnel
# ✅ Architecture JSON : Tous modules opérationnels
# ✅ Organisation : Structure presentations/[sujet]/[audience]/ créée
# ✅ Validation contenu : Slides générées avec styles Premier Tech préservés
```

**L'architecture JSON est complètement opérationnelle et prête pour la production !** 🚀

#### **Documentation Mise à Jour**
- **[docs/QUICK_START.md](docs/QUICK_START.md)** : Guide démarrage rapide avec architecture JSON
- **[docs/JSON_ARCHITECTURE_GUIDE.md](docs/JSON_ARCHITECTURE_GUIDE.md)** : Guide complet architecture JSON
- **[docs/CHARTS_ENHANCED_GUIDE.md](docs/CHARTS_ENHANCED_GUIDE.md)** : Guide graphiques
- **Templates JSON** : 8 templates payload dans templates/presentation-project/

**L'architecture JSON est opérationnelle et prête pour la production !** 🎯

---

## 🔧 **Gestion des Tâches avec Cycle de Vie Complet**

### Structure Organisationnelle
```
tasks/
├── open/           # Tâches en cours ou à traiter
│   ├── README.md   # Guide d'utilisation
│   └── *.md        # Fichiers de tâches actives
└── closed/         # Tâches terminées
    ├── README.md   # Archive et référence
    └── *.md        # Historique des tâches complétées
```

### Workflow Automatisé (Consolidé)
1. **Création** : `/create-task [description]` → Nouvelle tâche dans `tasks/open/`
2. **Exécution + Completion** : `/execute-task [nom-fichier]` → Analyse, implémentation ET archivage automatique vers `tasks/closed/` après validation
3. **Completion manuelle (optionnel)** : `/complete-task [nom-fichier]` → Pour fermer une tâche sans l'exécuter

### Commandes Disponibles
- **`/create-task`** : Crée une nouvelle tâche dans `tasks/open/`
- **`/execute-task`** : Exécute une tâche ET la marque automatiquement comme terminée après validation (consolidation exécution + completion)
- **`/complete-task`** : Fermeture manuelle d'une tâche sans exécution (usage optionnel)
- **Autres commandes** : Voir `.claude/commands/` pour la liste complète

### Avantages du Système
- **Visibilité claire** : Distinction immédiate entre tâches actives et terminées
- **Traçabilité complète** : Historique préservé dans `tasks/closed/`
- **Workflow simplifié** : Commandes automatisées pour tout le cycle de vie
- **Organisation optimale** : Focus sur les tâches actives, archive accessible

Cette approche garantit une gestion cohérente et automatisée des tâches avec cycle de vie complet dans le workflow du projet.