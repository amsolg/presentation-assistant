# Dossier Presentations

Ce dossier contient tous les projets de présentations créés avec le système Presentation Assistant.

## Structure

### 📁 Projets Actifs

#### `dvaas/`
**Data Virtualization as a Service**
- Présentation complète DVaaS avec audio
- Contient : DVaaS.pptx, scripts générés, métadonnées
- Status : Projet terminé

#### `poc-fabric/`
**Proof of Concept Microsoft Fabric**
- Migration automatisée vers Microsoft Fabric
- Contient : POC_Fabric.pptx, documentation, scripts
- Status : Projet en cours

#### `hygiene-mains/`
**Hygiène des Mains**
- Projet de démonstration
- Status : En développement

#### `dmbok/`
**Data Management Body of Knowledge**
- Projet DMBoK (en préparation)
- Status : Planifié

## Convention de Nommage

Chaque projet de présentation suit cette structure :
```
nom-projet/
├── presentation.pptx          # Présentation finale
├── scripts/                   # Scripts générés
│   ├── enhanced_script.json
│   └── script_sam_complet.json
├── analysis/                  # Analyses contextuelles
│   └── rapport_analyse.json
├── audio/                     # Fichiers audio (si applicable)
├── metadata/                  # Métadonnées du projet
└── docs/                      # Documentation spécifique
```

## Workflow de Création

1. **Initialisation** : Créer la structure avec les templates dans `templates/presentation-project/`
2. **Configuration** : Adapter les fichiers `audience.md`, `content-brief.md`, `presentation-script.md`
3. **Script d'orchestration** : Générer `build_presentation.py` personnalisé selon l'audience
4. **Construction** : Exécuter le script pour construire la présentation

## Bonnes Pratiques

- **Un dossier par présentation**
- **Noms en minuscules avec tirets**
- **Conservation des scripts pour reproductibilité**
- **Documentation du contexte dans docs/**