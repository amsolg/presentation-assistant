---
description: "Exécute une tâche spécifique et la marque automatiquement comme terminée après validation"
argument-hint: "chemin/vers/la/tache"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "TodoWrite", "Task", "SlashCommand"]
---

# Execute Task

Exécute une tâche ciblée spécifiée par le chemin $ARGUMENTS en analysant son contexte, ses dépendances et en orchestrant son exécution complète. **Nouveauté : La tâche est automatiquement marquée comme terminée et déplacée vers `tasks/closed/` après validation du travail.**

## Phase 1: Analyse de la Tâche

### Localisation et Lecture
1. **Naviguer vers la tâche**: Localiser et lire le fichier/dossier de la tâche à $ARGUMENTS
2. **Analyser le contexte**: Examiner la structure, le type de tâche et ses objectifs
3. **Identifier les dépendances**: Détecter les fichiers, configurations et ressources nécessaires
4. **Comprendre les contraintes**: Analyser les prérequis techniques et les limitations

### Validation Préalable
1. **Vérifier la faisabilité**: Confirmer que tous les éléments nécessaires sont disponibles
2. **Analyser les risques**: Identifier les impacts potentiels sur le système
3. **Planifier l'exécution**: Créer une todo list détaillée avec l'outil TodoWrite

## Phase 2: Préparation de l'Environnement

### Configuration
1. **Préparer l'environnement**: Vérifier et configurer les dépendances techniques
2. **Sauvegarder l'état**: Créer un point de sauvegarde si nécessaire
3. **Initialiser les outils**: Préparer les outils et scripts requis pour l'exécution

### Stratégie d'Exécution
1. **Définir l'approche**: Choisir la méthode d'exécution optimale
2. **Estimer la durée**: Évaluer le temps nécessaire à l'accomplissement
3. **Prévoir les alternatives**: Identifier les solutions de fallback

## Phase 3: Exécution Orchestrée

### Exécution Étape par Étape
1. **Suivre la todo list**: Exécuter chaque étape en marquant la progression
2. **Monitorer en temps réel**: Surveiller l'avancement et détecter les problèmes
3. **Adapter si nécessaire**: Ajuster la stratégie selon les obstacles rencontrés
4. **Documenter le processus**: Enregistrer les actions entreprises et leurs résultats

### Gestion des Problèmes
1. **Diagnostiquer les erreurs**: Analyser et résoudre les problèmes rencontrés
2. **Implémenter les corrections**: Appliquer les solutions identifiées
3. **Valider les corrections**: Vérifier que les problèmes sont résolus
4. **Continuer l'exécution**: Reprendre le processus après résolution

## Phase 4: Validation et Finalisation

### Tests et Vérification
1. **Exécuter les tests**: Lancer les tests appropriés selon le type de tâche
2. **Valider les résultats**: Confirmer que les objectifs sont atteints
3. **Vérifier l'intégrité**: S'assurer que l'exécution n'a pas causé de régressions
4. **Tester les edge cases**: Valider le comportement dans les cas limites

### Documentation et Nettoyage
1. **Documenter les résultats**: Créer un rapport d'exécution détaillé
2. **Nettoyer les fichiers temporaires**: Supprimer les artefacts d'exécution
3. **Mettre à jour la documentation**: Actualiser la documentation projet si nécessaire
4. **Archiver les logs**: Sauvegarder les logs d'exécution pour référence future

## Phase 5: Rapport Final et Documentation Automatique

### Synthèse d'Exécution
1. **Résumer l'accomplissement**: Présenter les résultats obtenus
2. **Lister les modifications**: Détailler les changements apportés au système
3. **Identifier les enseignements**: Noter les leçons apprises pendant l'exécution
4. **Recommander les actions suivantes**: Proposer les prochaines étapes si pertinentes

### Métriques et Performance
1. **Temps d'exécution**: Rapporter la durée totale d'accomplissement
2. **Ressources utilisées**: Documenter l'utilisation des ressources système
3. **Taux de succès**: Évaluer le niveau de réussite de la tâche
4. **Points d'amélioration**: Identifier les optimisations possibles pour le futur

### Génération Automatique du Rapport (OBLIGATOIRE)
1. **Créer le rapport détaillé**: Générer automatiquement un rapport dans `tasks/reports/`
   - Format : `[YYYY-MM-DD]_[HH-MM]_[nom-tache]_report.md`
   - Utiliser le template dans `tasks/reports/report_template.md`
   - Inclure TOUTES les sections du template avec données réelles
2. **Documenter les actions**: Liste complète des fichiers créés/modifiés avec détails
3. **Capturer les métriques**: Temps d'exécution, nombre de fichiers, tests exécutés
4. **Archiver pour traçabilité**: Le rapport doit servir de référence complète pour l'audit

## Phase 6: Completion Automatique (Nouveau)

### Validation et Fermeture
1. **Confirmer la réussite**: Après validation complète du travail effectué
2. **Demander confirmation**: "La tâche a été complétée avec succès. Voulez-vous la marquer comme terminée et la déplacer vers tasks/closed/ ? (Oui par défaut)"
3. **Si validation positive ou pas de réponse**:
   - Déplacer automatiquement le fichier de tâche de `tasks/open/` vers `tasks/closed/`
   - Ajouter un timestamp de completion au fichier
   - Mettre à jour l'index des tâches dans `tasks/README.md`
4. **Afficher confirmation**:
   ```
   ✅ Tâche complétée et archivée avec succès
   📁 Déplacée vers tasks/closed/[nom-tache].md
   🎯 Prochaine tâche disponible dans tasks/open/
   ```

### Cas Spéciaux
- **Si la tâche échoue**: Ne pas la déplacer, rester dans open/ avec note d'échec
- **Si validation manuelle requise**: Proposer d'utiliser `/complete-task` manuellement plus tard
- **Si tâche partielle**: Garder dans open/ avec mise à jour du statut

## Utilisation

```bash
/execute-task chemin/vers/ma/tache
/execute-task tasks/open/ma-tache.md
/execute-task tasks/open/refactoring-api.md
/execute-task scripts/deployment/deploy-prod.sh
```

## Adaptabilité

Cette commande s'adapte automatiquement aux différents types de tâches :
- **Scripts**: Exécution directe avec gestion des paramètres
- **Documentation**: Analyse et implémentation des instructions
- **Projets**: Orchestration multi-étapes avec coordination
- **Configurations**: Application et validation des paramètres
- **Tests**: Exécution avec rapport de couverture et résultats

## Workflow Consolidé (Nouveau)

Cette commande intègre maintenant **l'exécution ET la completion** en un seul workflow :
1. **Exécution complète** de la tâche avec validation
2. **Archivage automatique** vers `tasks/closed/` après succès
3. **Traçabilité maintenue** avec historique complet
4. **Gain de temps** : Une seule commande au lieu de deux

**Note**: La commande `/complete-task` reste disponible pour les cas où vous voulez fermer manuellement une tâche sans l'exécuter, ou si vous préférez contrôler manuellement le moment de la fermeture.