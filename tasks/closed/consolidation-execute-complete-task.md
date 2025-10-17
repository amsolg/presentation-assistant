# Consolidation Execute-Task et Complete-Task

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
L'utilisateur doit exécuter deux commandes séparées pour traiter complètement une tâche : `/execute-task` pour l'implémenter, puis `/complete-task` pour la marquer comme terminée et la déplacer vers `closed/`.

**Impact sur l'utilisateur :**
- Double effort pour chaque tâche (2 commandes au lieu d'une)
- Risque d'oublier de fermer les tâches terminées
- Accumulation de tâches dans `open/` même si elles sont complétées
- Workflow interrompu et moins fluide

## 💡 Solution Proposée

**Expérience cible :**
L'utilisateur exécute simplement `/execute-task nom-tache.md` et le système :
1. Analyse et implémente la tâche
2. Valide automatiquement le travail effectué
3. Demande confirmation si tout est OK
4. Déplace automatiquement la tâche vers `closed/` après validation

**Bénéfices attendus :**
- Workflow simplifié : une seule commande pour tout le cycle
- Pas de tâches oubliées dans `open/`
- Meilleure traçabilité avec validation automatique
- Gain de temps significatif sur chaque tâche

## 🛠️ Implémentation

### Ce qui doit changer
- **`.claude/commands/execute-task.md`** : Ajouter la logique de completion après validation
- **`.claude/commands/complete-task.md`** : Garder pour usage manuel si besoin, mais moins fréquent

### Tests de validation
- [ ] Execute-task termine et déplace automatiquement une tâche simple
- [ ] Execute-task demande confirmation avant de fermer
- [ ] Complete-task reste disponible pour fermeture manuelle
- [ ] Les tâches fermées gardent leur historique dans `closed/`

### Documentation à ajuster
- [ ] `CLAUDE.md` - Section workflow des tâches
- [ ] `tasks/README.md` - Mise à jour du workflow

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Peut exécuter et fermer une tâche en une seule commande
- [ ] Reçoit une confirmation claire de la completion
- [ ] Ne retrouve plus de tâches terminées dans `open/`

**Pour le système :**
- [ ] Validation automatique fonctionne
- [ ] Déplacement vers `closed/` sans perte de données
- [ ] Compatibilité avec l'ancien workflow maintenue

## 🚀 Prochaines Étapes

1. **Analyser** les commandes execute-task et complete-task actuelles
2. **Implémenter** la logique de validation et completion dans execute-task
3. **Tester** sur plusieurs types de tâches
4. **Scanner** les tâches ouvertes pour identifier celles à fermer

---

**Créé :** 2025-01-16
**Priorité :** Élevée
**Estimation :** 30-45 minutes