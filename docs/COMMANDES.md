# 📋 Référence Architecture JSON - Presentation Builder

## 🎯 Architecture JSON 2025

### **Principe Fondamental**
- **Configuration centralisée** : Un seul fichier JSON configure toute la présentation
- **Payloads modulaires** : Chaque slide a son propre fichier JSON
- **Orchestrateur unique** : `presentation_builder.py` coordonne tout

### **Workflow JSON**
```bash
# 1. Créer la configuration JSON
python presentation_builder/presentation_builder.py config.json

# 2. Validation optionnelle
python presentation_builder/presentation_builder.py config.json --validate
```

---

## 📖 **Configuration JSON**

### **Structure de Base**
```json
{
  "presentation_name": "Nom de la Présentation",
  "subject": "nom-sujet",
  "audience": "nom-audience",
  "title_slide": {
    "title": "Titre Principal",
    "subtitle": "Sous-titre Optionnel",
    "metadata": "Date – Contexte"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "module_builder",
      "payload_path": "chemin/vers/payload.json",
      "description": "Description de la slide"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true,
    "preserve_styles": true
  }
}
```

### **Champs Obligatoires**
- `presentation_name` : Nom de la présentation
- `subject` : Nom du sujet (pour navigation presentations/[sujet]/)
- `audience` : Nom de l'audience (pour navigation presentations/[sujet]/[audience]/)
- `slides` : Array des slides (peut être vide pour présentation titre + fermeture uniquement)

### **Champs Optionnels**
- `title_slide` : Configuration de la slide titre (générée automatiquement si omis)
- `build_options` : Options de construction

---

## 🧩 **Modules JSON Disponibles**

### **Navigation - `navigation_builder`**
**Template payload** : `navigation_builder_template.json`
```json
{
  "sections": ["Section 1", "Section 2", "Section 3"],
  "style": "numbered",
  "options": {
    "auto_widen": true
  }
}
```

### **Section Header - `section_header_builder`**
**Template payload** : `section_header_builder_template.json`
```json
{
  "section_title": "Nom de la Section",
  "section_style": "numbered",
  "section_number": 1,
  "options": {
    "auto_widen": true
  }
}
```

### **Message Simple - `simple_message_builder`**
**Template payload** : `simple_message_builder_template.json`
```json
{
  "message_text": "Votre message principal",
  "keywords": "Mots-clés • Optionnels",
  "message_style": "centered",
  "options": {
    "auto_widen": true
  }
}
```

### **Statistiques - `statistics_builder`**
**Template payload** : `statistics_builder_template.json`
```json
{
  "title": "Titre des Statistiques",
  "style": "four_stats_lines",
  "statistics": [
    {
      "value": "92x",
      "label": "ROI Maximum"
    },
    {
      "value": "$260B",
      "label": "Économies Possibles"
    }
  ],
  "options": {
    "auto_widen": true
  }
}
```

### **Boîtes de Contenu - `content_boxes_builder`**
**Template payload** : `content_boxes_builder_template.json`
```json
{
  "title": "Titre des Concepts",
  "content_style": "blue_3_detailed",
  "concepts": [
    "Premier concept avec explication détaillée",
    "Deuxième concept avec contexte",
    "Troisième concept avec impact"
  ],
  "subtitles": [
    "Sous-titre 1",
    "Sous-titre 2",
    "Sous-titre 3"
  ],
  "options": {
    "auto_widen": true
  }
}
```

### **Explication Détaillée - `detailed_explanation_builder`**
**Template payload** : `detailed_explanation_builder_template.json`
```json
{
  "content": "Explication principale du concept",
  "title": "Titre de l'Explication",
  "additional_content": [
    "Point 1 : Détail important",
    "Point 2 : Contexte supplémentaire"
  ],
  "explanation_style": "dual_lists_blue"
}
```

### **Témoignage - `testimonial_builder`**
**Template payload** : `testimonial_builder_template.json`
```json
{
  "quote": "Citation ou témoignage client",
  "author": "Nom de l'Auteur",
  "position": "Poste et Entreprise",
  "style": "centered",
  "options": {
    "auto_widen": true
  }
}
```

### **Graphiques - `charts_builder`**
**Template payload** : `charts_builder_template.json`
```json
{
  "chart_type": "bar_clustered",
  "data_source": "data/dataset.csv",
  "title": "Titre du Graphique",
  "x_axis_label": "Axe X",
  "y_axis_label": "Axe Y",
  "options": {
    "auto_widen": true
  }
}
```

---

## 🎯 **Exemples Complets**

### **Présentation Simple (3 slides)**
```json
{
  "presentation_name": "Présentation Test",
  "subject": "test",
  "audience": "demo",
  "title_slide": {
    "title": "Titre Test",
    "subtitle": "Démonstration Architecture JSON",
    "metadata": "2025-01-15 – Demo"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "simple_message_builder",
      "payload_path": "presentations/test/demo/message.json",
      "description": "Message de démonstration"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

### **Présentation Business (7 slides)**
```json
{
  "presentation_name": "Stratégie Business 2025",
  "subject": "strategy",
  "audience": "executives",
  "title_slide": {
    "title": "Stratégie Business 2025",
    "subtitle": "Vision et Roadmap",
    "metadata": "2025-01-15 – Comité Exécutif"
  },
  "slides": [
    {
      "position": 2,
      "script_name": "navigation_builder",
      "payload_path": "presentations/strategy/executives/navigation.json",
      "description": "Table des matières"
    },
    {
      "position": 3,
      "script_name": "statistics_builder",
      "payload_path": "presentations/strategy/executives/kpi.json",
      "description": "KPI actuels"
    },
    {
      "position": 4,
      "script_name": "content_boxes_builder",
      "payload_path": "presentations/strategy/executives/pillars.json",
      "description": "Piliers stratégiques"
    },
    {
      "position": 5,
      "script_name": "detailed_explanation_builder",
      "payload_path": "presentations/strategy/executives/roadmap.json",
      "description": "Roadmap détaillée"
    },
    {
      "position": 6,
      "script_name": "charts_builder",
      "payload_path": "presentations/strategy/executives/projections.json",
      "description": "Projections financières"
    },
    {
      "position": 7,
      "script_name": "simple_message_builder",
      "payload_path": "presentations/strategy/executives/call-to-action.json",
      "description": "Appel à l'action"
    }
  ],
  "build_options": {
    "auto_widen_text": true,
    "generate_reports": true
  }
}
```

---

## 🔧 **Commandes Utiles**

### **Construction et Validation**
```bash
# Construction simple
python presentation_builder/presentation_builder.py config.json

# Avec validation préalable
python presentation_builder/presentation_builder.py config.json --validate

# Validation seule (sans construction)
python presentation_builder/presentation_builder.py config.json --validate-only
```

### **Gestion des Templates**
```bash
# Lister les templates disponibles
ls templates/presentation-project/slide-payload-templates/

# Copier un template pour démarrer
cp templates/presentation-project/slide-payload-templates/simple_message_builder_template.json mon_message.json

# Valider un payload JSON
python -m json.tool mon_payload.json
```

### **Structure et Organisation**
```bash
# Voir la structure d'un projet
tree presentations/[sujet]/[audience]/

# Vérifier les sorties
ls presentations/[sujet]/[audience]/output/

# Examiner les rapports
cat presentations/[sujet]/[audience]/output/*_build_report.json
```

---

## ⚙️ **Options Avancées**

### **Build Options Détaillées**
```json
{
  "build_options": {
    "base_template": "templates/Template_PT.pptx",
    "auto_widen_text": true,
    "generate_reports": true,
    "preserve_styles": true,
    "backup_before_changes": true,
    "validate_content": true
  }
}
```

### **Payload Options Communes**
```json
{
  "options": {
    "auto_widen": true,
    "insert_position": null,
    "preserve_aspect_ratio": true,
    "enable_text_wrapping": true
  }
}
```

---

## 🚀 **Tests et Validation**

### **Tests Unitaires**
```bash
# Tester l'architecture JSON
cd test/unit_tests/presentation_builder
python test_presentation_builder.py

# Tester un module spécifique
python test_statistics_builder.py
python test_content_boxes_builder.py
```

### **Validation Schema**
```bash
# Valider une configuration contre le schema
python scripts/validate_config.py config.json

# Valider tous les payloads d'un projet
python scripts/validate_project.py presentations/[sujet]/[audience]/
```

---

## 📈 **Métriques et Rapports**

### **Rapports Générés Automatiquement**
- `*_creation_report.json` : Rapport de création de la slide titre
- `*_build_report.json` : Rapport de construction complète
- `*_insertion_report.json` : Rapports d'insertion par module

### **Contenu des Rapports**
```json
{
  "timestamp": "2025-01-15T10:34:23",
  "presentation_path": "path/to/output.pptx",
  "slides_created": 9,
  "modules_used": ["simple_message_builder", "statistics_builder"],
  "total_duration": "2.3 seconds",
  "success": true,
  "errors": [],
  "warnings": []
}
```

---

## 🎯 **Bonnes Pratiques**

### **Organisation des Fichiers**
1. **Configuration JSON** : Un seul fichier par présentation
2. **Payloads modulaires** : Un fichier JSON par slide
3. **Nommage cohérent** : `[type]-[description].json`
4. **Documentation** : README.md par projet

### **Validation et Tests**
1. **Validation schema** : Toujours valider avant construction
2. **Tests unitaires** : Exécuter après modifications
3. **Rapports** : Consulter les rapports de construction
4. **Backup** : Les backups sont créés automatiquement

### **Performance et Optimisation**
1. **Payloads légers** : Éviter les contenus trop longs
2. **Chemins relatifs** : Utiliser des chemins depuis la racine
3. **Cache templates** : Les templates sont mis en cache automatiquement
4. **Parallélisation** : Les modules sont traités efficacement

**🎯 Note :** Cette architecture JSON remplace complètement l'approche CLI legacy et offre une configuration centralisée, modulaire et validée pour des présentations Premier Tech de qualité professionnelle.