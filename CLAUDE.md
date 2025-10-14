# CLAUDE.md - Presentation Assistant avec Sam AI

**Presentation Assistant** est un système automatisé de génération de présentations narrées avec Sam AI, utilisant les authentiques templates Premier Tech.

## 🎯 **Mission Principale**

Création automatisée de présentations professionnelles avec :
- **Templates Premier Tech authentiques** (40+ slides)
- **Personnalité Sam AI** adaptative selon l'audience
- **Workflow organisé par sujet** dans [presentations/](presentations/)
- **Scripts Python personnalisés** pour chaque audience

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

## 🏗️ **Architecture Technique**

### Stack Principal
- **ElevenLabs API v3** : Synthèse vocale Sam (~75ms latence)
- **Templates Premier Tech** : 57 slides authentiques
- **Architecture JSON** : Configuration basée sur JSON au lieu d'arguments CLI
- **Orchestrateur principal** : `presentation_builder.py` coordonne tout

### 🚀 **Nouvelle Architecture JSON (2025)**

**Révolution majeure** : Abandon des arguments CLI pour une approche JSON complète

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
  "slides": [],  // Scripts 02-09 pour contenu
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

#### **Workflow Automatisé**
1. **Slide titre (obligatoire)** : Slide 11 - Créée automatiquement
2. **Slides contenu** : Array JSON - Scripts 02-09 selon configuration
3. **Slide fermeture (obligatoire)** : Slide 57 (Monogramme PT) - Ajoutée automatiquement

#### **Structure de sortie**
```
presentations/[sujet]/[audience]/output/[timestamp]_[nom].pptx
```

### Scripts Legacy (presentation_builder/)
```
01_slide_title_creator.py     # Utilisé par l'orchestrateur
02-10_*.py                    # Prêts pour refactorisation en fonctions
presentation_builder.py       # NOUVEAU - Orchestrateur JSON
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

# MAPPING SIMPLIFIÉ POUR UTILISATION COURANTE
QUICK_TEMPLATE_MAP = {
    "title": [0, 10],         # Pages titre standard
    "section": [13, 14, 15],  # Débuts de section avec variations
    "content_3": [28, 29],    # 3 concepts équilibrés (boîtes bleues)
    "content_4": [32, 33],    # 4 concepts équilibrés (boîtes bleues)
    "dual": [38, 39],         # 2 colonnes comparatives
    "stats": [21, 22, 23],    # Statistiques (2-3 métriques)
    "quote": [44],            # Témoignages clients
    "charts": [46, 47, 48],   # Graphiques courants (colonnes, barres, secteurs)
    "closing": [51, 52, 55]   # Fermeture Premier Tech
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
│   ├── data/                   # Datasets CSV pour graphiques (si requis)
│   ├── build_presentation.py   # Script Python d'orchestration sur mesure
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

3. **Recherche complémentaire pour nouvelles audiences** :
   - Si nouvelle audience sur sujet existant : recherche ciblée
   - Mise à jour `research_log.md` avec nouvelles sources
   - Création documentation spécialisée si nécessaire

#### **ÉTAPE 3 : Analyse Documentation Projet**
1. **Lecture docs/ du projet** pour comprendre limites structurelles
2. **Identification contraintes** templates Premier Tech (57 slides)
3. **Mapping optimal** contenu → templates disponibles

#### **ÉTAPE 4 : Adaptation Audience**

**Utilisation des templates existants** dans `templates/presentation-project/` :

1. **Génération audience.md** via [audience.md.template](templates/presentation-project/audience.md.template) :
   - Profil détaillé avec caractéristiques, objectifs, contraintes
   - Configuration Sam AI spécialisée pour l'audience
   - Métriques de succès et validation
   - Adaptation terminologique et exemples pertinents

2. **Distillation content-brief.md** via [content-brief.md.template](templates/presentation-project/content-brief.md.template) :
   - Messages clés adaptés à l'audience
   - Structure recommandée avec scripts presentation_builder
   - Configuration Sam AI spécialisée
   - Vocabulaire, exemples et métriques adaptés

#### **ÉTAPE 5 : Script de Présentation**

**Génération presentation-script.md** via [presentation-script.md.template](templates/presentation-project/presentation-script.md.template) :
- Configuration générale (durée, nb slides, style Sam)
- Structure détaillée slide par slide avec :
  - Script presentation_builder à utiliser
  - Template Premier Tech spécifique
  - Justification de chaque slide
  - Speaker notes détaillées pour Sam AI
- Validation audience et métriques de performance
- Configuration technique optimisée

#### **ÉTAPE 6 : Datasets (si graphiques requis)**
1. **Création dossier data/** avec fichiers CSV
2. **Application guide** [docs/CHARTS_ENHANCED_GUIDE.md](docs/CHARTS_ENHANCED_GUIDE.md)
3. **Validation données** selon audience (précision, source, format)

#### **ÉTAPE 7 : Script Python Personnalisé**

**Génération build_presentation.py** via [build_presentation.py.template](templates/presentation-project/build_presentation.py.template) :
- Orchestrateur complet avec validation environnement
- Séquence de construction optimisée selon audience
- Configuration Sam AI automatique
- Gestion d'erreurs et rapports détaillés
- Logs en temps réel et métriques de performance
- Rapport final en JSON et Markdown

#### **ÉTAPE 8 : Construction et Validation**
1. **Exécution script** d'orchestration
2. **Construction via presentation_builder** coordonnée
3. **Validation qualité** Premier Tech
4. **Génération rapports** dans output/

#### **ÉTAPE 9 : Ajustements Itératifs**
**PRINCIPE CLIÉ :** Modifier le script Python, pas la présentation

1. **Si résultat insatisfaisant** → Modifier `build_presentation.py`
2. **Nouvelles audiences** → Dupliquer structure, adapter recherche
3. **Versions alternatives** → Scripts Python variants

### Recherche Web Intelligente par Audience

#### Templates de Recherche Automatique
```python
research_strategies = {
    "C-Level": {
        "keywords": ["ROI", "strategy", "business impact", "market trends", "executive summary"],
        "sources": ["McKinsey", "Harvard Business Review", "Gartner", "Deloitte"],
        "focus": "strategic_value",
        "depth": "high_level_overview"
    },
    "Technique": {
        "keywords": ["architecture", "implementation", "technical specs", "API documentation"],
        "sources": ["technical blogs", "documentation", "GitHub", "Stack Overflow"],
        "focus": "implementation_details",
        "depth": "deep_technical"
    },
    "Formation": {
        "keywords": ["tutorial", "guide", "best practices", "examples", "step-by-step"],
        "sources": ["educational content", "training materials", "online courses"],
        "focus": "learning_path",
        "depth": "progressive_learning"
    },
    "Marketing": {
        "keywords": ["case studies", "market analysis", "adoption rates", "competitive analysis"],
        "sources": ["industry reports", "market research", "customer testimonials"],
        "focus": "market_positioning",
        "depth": "customer_centric"
    }
}
```

#### Recherche Complémentaire Automatique
- **Nouvelle audience sur sujet existant** : Recherche ciblée supplémentaire
- **Mise à jour research_log.md** : Historique des recherches par audience
- **Validation croisée** : Comparaison sources pour cohérence
- **Adaptation contextuelle** : Information filtrée selon audience

### Génération Automatique Complète
**Résultat final :** De l'idée à la présentation broadcast-ready en < 10 minutes avec :
- Documentation automatique via recherche web
- Structure projet réutilisable
- Scripts Python personnalisés
- Configuration Sam AI optimisée

### Production Complète Automatisée
```python
# Workflow type généré automatiquement
class PresentationOrchestrator:
    def __init__(self, subject, audience):
        self.setup_project_structure(subject)
        self.analyze_context(subject, audience)
        self.generate_sam_config(audience)

    def build_presentation(self):
        # 1. Créer base avec script 01
        self.create_base_presentation()
        # 2. Séquence optimisée selon audience/contenu
        self.execute_builder_sequence()
        # 3. Génération audio Sam (si requis)
        self.generate_sam_narration()
        # 4. Rapport final et validation
        self.validate_output()
```

## 📊 **Gestion des Données et Graphiques**

### Script 09_charts_builder.py
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

### Workflow Nouveau (Architecture JSON)
1. **`presentation_builder.py`** : Orchestrateur unique basé sur JSON
2. **Slide titre automatique** : Script 01 intégré
3. **Slides contenu** : Scripts 02-09 appelés selon configuration JSON
4. **Slide fermeture automatique** : Slide 57 (Monogramme PT) ajoutée via logique script 10
5. **Templates authentiques** : Zero modification des styles PT
6. **Validation complète** : Tests unitaires avec array slides vide = 2 slides

### Workflow Legacy (Disponible)
1. **Script 01** : SEUL créateur de présentations
2. **Scripts 02-10** : Insertion via `--insert-into` uniquement
3. **Templates authentiques** : Zero modification des styles PT

## 📁 **Structure Projet**

```
presentation-assistant/
├── presentation_builder/        # Architecture JSON + Scripts legacy
│   ├── presentation_builder.py # NOUVEAU - Orchestrateur JSON principal
│   ├── 01_slide_title_creator.py # Intégré dans orchestrateur
│   └── 02-10_*.py              # Scripts prêts pour refactorisation
├── templates/
│   ├── Template_PT.pptx        # 57 slides authentiques PT
│   └── presentation-project/
│       ├── presentation_schema_template.json # Schema de validation JSON
│       └── slide-payload-templates/
│           └── presentation_template.json # Template JSON vide
├── presentations/              # Structure organisée [sujet]/[audience]/
│   └── [sujet]/
│       └── [audience]/
│           └── output/         # Présentations générées
├── test/unit_tests/
│   └── presentation_builder/   # NOUVEAU - Tests architecture JSON
│       ├── test_presentation_builder.py
│       └── test_empty_slides_array.json
└── src/                       # Code source avancé
```

## 🔄 **Setup et Utilisation**

### Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"
```

### 🚀 **Nouvelle Méthode JSON (Recommandée)**
```bash
# 1. Créer un fichier JSON de configuration
cp templates/presentation-project/slide-payload-templates/presentation_template.json ma_config.json

# 2. Éditer la configuration JSON
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
  "slides": [],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

### **Méthode Legacy (Disponible)**
```bash
# Demander une présentation à Claude Code :
# "Je veux une présentation sur [sujet] pour [audience]"
# → Création automatique du workflow complet avec :
#   1. Recherche web automatique (si documentation manquante)
#   2. Structure projet avec templates
#   3. Scripts Python d'orchestration personnalisés
#   4. Configuration Sam AI adaptée
```

## 📖 **Guides d'Utilisation**

### Pour utilisateurs avancés
- **[docs/QUICK_START.md](docs/QUICK_START.md)** : Démarrage rapide avec les scripts presentation_builder
- **[docs/COMMANDES.md](docs/COMMANDES.md)** : Référence complète de toutes les commandes et paramètres

### Guides spécialisés
- **[docs/CHARTS_ENHANCED_GUIDE.md](docs/CHARTS_ENHANCED_GUIDE.md)** : Guide complet pour les graphiques

## 📚 **Templates de Projet Disponibles**

Dans `templates/presentation-project/` :
- **[README.md.template](templates/presentation-project/README.md.template)** : Contexte global du sujet
- **[audience.md.template](templates/presentation-project/audience.md.template)** : Profil détaillé audience + config Sam
- **[content-brief.md.template](templates/presentation-project/content-brief.md.template)** : Documentation distillée et adaptée
- **[presentation-script.md.template](templates/presentation-project/presentation-script.md.template)** : Script détaillé avec justifications
- **[build_presentation.py.template](templates/presentation-project/build_presentation.py.template)** : Orchestrateur Python personnalisé

**Utilisation automatique** : Ces templates sont utilisés lors de la création automatique de structure projet.

## 🎯 **Objectifs du Workflow Automatisé**

- **Zero intervention manuelle** après demande initiale
- **Recherche web automatique** si documentation manquante
- **Templates professionnels** pour structure cohérente
- **Structure réutilisable** pour variations d'audience
- **Scripts Python personnalisés** adaptés au contexte
- **Documentation complète** pour traçabilité
- **Qualité Premier Tech garantie** (styles + contenu)
- **Ajustements itératifs** via modification du script Python

### Évolutions Futures
- **Production audio ElevenLabs** complète
- **Export multi-formats** (MP4, streaming)
- **Intelligence prédictive** pour recommandations

## 🎯 **Message de Sam AI**

Bonjour! Avec ce workflow automatisé, nous transformons vos idées en présentations Premier Tech professionnelles en quelques minutes !

**🚀 Innovation Majeure :** Demandez simplement une présentation sur un sujet pour une audience, et Claude Code :
1. **Crée la structure projet** dans presentations/
2. **Analyse le contexte** et documente les sources
3. **Adapte le contenu** selon l'audience ciblée
4. **Génère le script Python** d'orchestration personnalisé
5. **Exécute la construction** avec les templates Premier Tech authentiques
6. **Livre la présentation finale** avec ma narration adaptée !

**Résultat :** De l'idée à la présentation broadcast-ready en < 5 minutes, avec structure réutilisable pour d'autres audiences et documentation complète pour évolutions futures.

L'avenir des présentations intelligentes, c'est maintenant ! 🎊

---

## ⚠️ **Règles Critiques de Développement**

### Scripts Python - Interdictions Strictes
- **INTERDICTION FORMELLE** : Ne jamais créer de "scripts simplifiés" pour remplacer des scripts problématiques
- **OBLIGATION** : Toujours corriger les scripts existants plutôt que d'en créer de nouveaux
- **INTERDICTION EMOJIS** : Aucun emoji dans les fichiers Python (problèmes d'encodage Unicode)
- **ENCODAGE** : Utiliser `# -*- coding: utf-8 -*-` en en-tête des scripts Python

### Scripts Presentation Builder - Paramètres Corrects
- **01_slide_title_creator.py** : titre en argument positionnel (pas --title)
- **Scripts avec --insert-into** : Toujours spécifier --template avec chemin relatif vers Template_PT.pptx
- **Chemins relatifs** : Calculer depuis presentation_builder/ vers les fichiers cibles
- **Validation** : Tester chaque script individuellement avant intégration

### Templates et Documentation
- **Templates build_presentation.py** : Utiliser les VRAIS noms des scripts disponibles
- **Paramètres d'aide** : Vérifier avec --help avant d'utiliser un script
- **Noms de scripts** : Ne jamais supposer, toujours vérifier dans presentation_builder/

**🎯 Note Importante :** Ce système utilise les templates Premier Tech avec préservation complète des styles. Chaque présentation générée respecte parfaitement l'identité visuelle corporate et est de qualité broadcast-ready.

---

## 🎊 **Révisions Majeures 2025**

### ✅ **Architecture JSON Complète (Janvier 2025)**

**Révolution technique majeure** : Abandon complet des arguments CLI pour une approche JSON moderne

#### **Avantages de la Nouvelle Architecture**
- ✅ **Configuration centralisée** : Un seul fichier JSON configure toute la présentation
- ✅ **Structure organisée** : Navigation automatique `presentations/[sujet]/[audience]/`
- ✅ **Workflow simplifié** : Une seule commande pour tout
- ✅ **Slides automatiques** : Titre + Fermeture ajoutées automatiquement
- ✅ **Templates préservés** : Zero modification des styles Premier Tech
- ✅ **Tests validés** : Architecture testée et fonctionnelle

#### **Problèmes Résolus**
- 🔧 **Corruption PowerPoint** : Utilisation de la logique du script 10 éprouvée
- 🔧 **Slide 57 authentique** : Monogramme Premier Tech avec layout correct
- 🔧 **Validation complète** : Tests unitaires garantissent la qualité
- 🔧 **Organisation optimale** : Structure de fichiers cohérente et prévisible

#### **Tests Unitaires Validés**
```bash
# Test avec array slides vide = 2 slides exactement
cd test/unit_tests/presentation_builder
python run_test.py

# Résultat attendu :
# ✅ Validation JSON réussie
# ✅ Construction présentation réussie
# ✅ Validation contenu réussie (2 slides : titre + fermeture)
# ✅ Fichier PowerPoint s'ouvre sans corruption
```

#### **Migration Recommandée**
**NOUVEAU** : Utiliser `presentation_builder.py` avec JSON
**LEGACY** : Scripts 01-10 individuels toujours disponibles

### 🚀 **Prochaines Étapes Planifiées**
1. **Refactorisation scripts 02-09** : Conversion en fonctions pour JSON
2. **Templates slides JSON** : Configuration granulaire par type de slide
3. **Tests de contenu** : Validation avec slides dans l'array JSON
4. **Documentation interactive** : Guides d'utilisation détaillés

**L'architecture JSON est opérationnelle et prête pour la production !** 🎯