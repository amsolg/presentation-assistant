# Gestion des Tâches - Presentation Assistant

## 🎯 Organisation

### Structure
```
tasks/
├── open/           # Tâches en cours ou à traiter
├── closed/         # Tâches terminées
└── reports/        # Rapports d'exécution automatiques
```

### Workflow
1. **Nouvelle tâche** : Créée dans `open/` via `/create-task`
2. **En cours** : Reste dans `open/` pendant le développement
3. **Exécution** : `/execute-task` génère automatiquement un rapport dans `reports/`
4. **Terminée** : Déplacée vers `closed/` via `/complete-task` ou automatiquement après exécution

## 📋 Tâches Ouvertes

| Tâche | Priorité | Description |
|-------|----------|-------------|
| [extracteur-contenu-pptx-agnostique](open/extracteur-contenu-pptx-agnostique.md) | Élevée | Extracteur PowerPoint avec hiérarchie d'héritage |
| [validation-nettoyage-title-creator](open/validation-nettoyage-title-creator.md) | Élevée | Validation architecture JSON |
| [refactorisation-integration-title-creator](open/refactorisation-integration-title-creator.md) | Élevée | Intégration logique title creator |
| [generer-structure-json-slide-11](open/generer-structure-json-slide-11.md) | Élevée | Générer structure JSON détaillée pour slide 11 |

## ✅ Tâches Terminées

| Tâche | Date | Description |
|-------|------|-------------|
| [ameliorer-creation-rapports-automatiques](closed/ameliorer-creation-rapports-automatiques.md) | 2025-01-16 | ✅ Système de rapports automatiques |
| [implementation-systeme-gestion-taches-open-closed](closed/implementation-systeme-gestion-taches-open-closed.md) | 2025-10-16 | ✅ Système de gestion des tâches |

## 🛠️ Commandes Disponibles

- `/create-task [description]` : Crée une nouvelle tâche dans open/
- `/complete-task [nom-fichier]` : Déplace une tâche vers closed/
- `/execute-task [chemin]` : Exécute une tâche spécifique et génère un rapport dans reports/

## 📊 Rapports d'Exécution

Les rapports sont générés automatiquement dans `tasks/reports/` après chaque exécution de tâche. Format : `[YYYY-MM-DD]_[HH-MM]_[nom-tache]_report.md`

Dernier rapport généré : [2025-01-16_14-30_ameliorer-creation-rapports_report.md](reports/2025-01-16_14-30_ameliorer-creation-rapports_report.md)

---
**Dernière mise à jour :** 2025-01-17