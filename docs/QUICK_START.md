# ⚡ Démarrage Rapide - Presentation Assistant

## 🎯 Que voulez-vous créer ?

### 🚀 **Architecture JSON** (Méthode Unique)

**Approche moderne basée sur JSON :**
```bash
# 1. Créer un fichier de configuration JSON
cp templates/presentation-project/presentation_schema_template.json ma_config.json

# 2. Éditer la configuration (titre, slides, payloads)
# 3. Construire la présentation
python presentation_builder/presentation_builder.py ma_config.json
```

**Avantages :**
- Configuration centralisée dans un seul fichier JSON
- Payloads modulaires pour chaque slide
- Slides automatiques : titre + fermeture Premier Tech
- Structure organisée : `presentations/[sujet]/[audience]/`
- Templates préservés (styles Premier Tech authentiques)
- Tests unitaires validés

### 🤖 **Workflow Automatisé** (Production Complète avec Claude)

Demandez simplement à Claude Code :
```
"Je veux une présentation sur [sujet] pour [audience]"
```

**Résultat automatique :**
- Structure projet dans `presentations/[sujet]/`
- Recherche web automatique et documentation
- Configuration JSON centralisée
- Payloads JSON séparés pour chaque slide
- Configuration Sam AI adaptée à l'audience
- Présentation finale avec narration intégrée

### 📊 **Modules JSON Disponibles**

| **Type de contenu** | **Module JSON** | **Template de payload** |
|---------------------------|----------------------|------------------------|
| 🏷️ **Nouvelle section** | `section_header_builder` | `section_header_builder_template.json` |
| 💬 **Message important** | `simple_message_builder` | `simple_message_builder_template.json` |
| 📈 **Statistiques** | `statistics_builder` | `statistics_builder_template.json` |
| 📝 **Boîtes de contenu** | `content_boxes_builder` | `content_boxes_builder_template.json` |
| 📖 **Explications détaillées** | `detailed_explanation_builder` | `detailed_explanation_builder_template.json` |
| 💬 **Témoignage client** | `testimonial_builder` | `testimonial_builder_template.json` |
| 📈 **Graphiques** | `charts_builder` | `charts_builder_template.json` |
| 🧭 **Navigation** | `navigation_builder` | `navigation_builder_template.json` |

**Note :** Slide titre et fermeture Premier Tech ajoutées automatiquement.

### 🤖 **Sam AI - Configuration Automatique**

**Sam** s'adapte automatiquement selon l'audience :
- **C-Level** : Style stratégique, vocabulaire business
- **Technique** : Style précis, vocabulaire expert
- **Formation** : Style pédagogique, vocabulaire accessible

```bash
# Configuration ElevenLabs requise
export ELEVENLABS_API_KEY="your_key"
```

---

## 🚀 **Exemple Complet - Architecture JSON**

### 1. Configuration JSON (hygiene_mains.json)
```json
{
  "presentation_name": "Hygiène des Mains : Enjeu Stratégique Premier Tech",
  "subject": "hygiene-mains",
  "audience": "c-level",
  "title_slide": {
    "title": "Hygiène des Mains",
    "subtitle": "Un Levier Stratégique pour Premier Tech",
    "metadata": "2025-01-15 – Équipe Exécutive"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "simple_message_builder",
      "payload_path": "presentations/hygiene-mains/c-level/message-ouverture.json",
      "description": "Message d'ouverture stratégique"
    },
    {
      "position": 3,
      "script_name": "statistics_builder",
      "payload_path": "presentations/hygiene-mains/c-level/stats-roi.json",
      "description": "ROI et métriques financières"
    },
    {
      "position": 4,
      "script_name": "content_boxes_builder",
      "payload_path": "presentations/hygiene-mains/c-level/benefices-business.json",
      "description": "Bénéfices business concrets"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

### 2. Construction
```bash
python presentation_builder/presentation_builder.py hygiene_mains.json
```

**Résultat :** `presentations/hygiene-mains/c-level/output/[timestamp]_hygiene_des_mains_enjeu_strategique_premier_tech.pptx`

---

## ⚠️ **Règles Importantes**

### Architecture JSON (Unique)
1. **Configuration centralisée** : Un seul fichier JSON configure toute la présentation
2. **Payloads modulaires** : Chaque slide a son propre fichier JSON de payload
3. **Slides automatiques** : Titre et fermeture Premier Tech ajoutées automatiquement
4. **Structure organisée** : Sortie dans `presentations/[sujet]/[audience]/output/`
5. **Templates préservés** : 57 slides Premier Tech authentiques
6. **Tests validés** : Architecture testée avec tests unitaires
7. **Schema validation** : Validation automatique des configurations JSON

---

## 📖 **Besoin de plus de détails ?**

### Documentation Complète
- [JSON_ARCHITECTURE_GUIDE.md](JSON_ARCHITECTURE_GUIDE.md) : Guide complet architecture JSON
- [CHARTS_ENHANCED_GUIDE.md](CHARTS_ENHANCED_GUIDE.md) : Guide graphiques avec CSV
- [../CLAUDE.md](../CLAUDE.md) : Architecture complète et workflow automatisé
- [../templates/presentation-project/](../templates/presentation-project/) : Templates JSON

### Projets d'Exemple
- [../presentations/](../presentations/) : Exemples par sujet et audience avec configurations JSON

---

## 🔧 **Setup et Commandes Utiles**

```bash
# Installation
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"

# Architecture JSON
python presentation_builder/presentation_builder.py config.json
python presentation_builder/presentation_builder.py config.json --validate

# Templates disponibles
ls templates/presentation-project/slide-payload-templates/

# Structure d'un projet automatisé
ls presentations/[sujet]/[audience]/

# Tests unitaires
cd test/unit_tests/presentation_builder && python test_presentation_builder.py
```

## 🎯 **Architecture JSON 2025 - Production Ready**

**Approche Moderne** : Configuration centralisée JSON avec payloads modulaires
**Workflow Automatisé** : Création complète via Claude Code intégrant :
- Documentation automatique via recherche web
- Configuration JSON centralisée avec validation
- Payloads JSON séparés pour modularité
- Configuration Sam AI adaptative
- Structure réutilisable multi-audiences
- Templates Premier Tech préservés
- Qualité broadcast-ready garantie