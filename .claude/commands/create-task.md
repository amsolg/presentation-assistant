#---
description: "Crée une tâche roadmap focalisée sur l'expérience utilisateur pour Presentation Assistant"
argument-hint: "description-de-la-tache"
allowed-tools: ["Write", "Read", "Bash"]
---

# Create Roadmap Task

Crée une tâche roadmap simple et actionnable pour améliorer l'expérience utilisateur du système Presentation Assistant.

## Instructions

Génère un document de tâche en priorisant **l'expérience utilisateur** et la **simplicité d'exécution**. Voici la demande de l'utilisateur :

"$ARGUMENTS"

### 1. Créer la Structure

Si elle n'existe pas, créer :
```
tasks/
├── open/           # Tâches en cours
│   └── [nom-tache].md
└── closed/         # Tâches terminées
    └── [nom-tache].md
```

### 2. Générer la Tâche

Créer `tasks/open/[nom-tache].md` avec cette structure simplifiée :

```markdown
# [Titre de la Tâche]

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
[Description simple du problème du point de vue utilisateur]

**Impact sur l'utilisateur :**
[Pourquoi c'est frustrant/inefficace pour l'utilisateur]

## 💡 Solution Proposée

**Expérience cible :**
[Comment l'utilisateur devrait pouvoir faire cette tâche - décrit comme un scénario d'usage]

**Bénéfices attendus :**
- [Bénéfice utilisateur 1]
- [Bénéfice utilisateur 2]
- [Bénéfice utilisateur 3]

## 🛠️ Implémentation

### Ce qui doit changer
- **Fichier A :** [modification simple]
- **Fichier B :** [modification simple]

### Tests de validation
- [ ] Scénario utilisateur 1 fonctionne
- [ ] Scénario utilisateur 2 fonctionne
- [ ] Performance acceptable (< Xs)

### Documentation à ajuster
- [ ] `docs/[guide].md` - [section à mettre à jour]
- [ ] `CLAUDE.md` - [si changement workflow]

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Peut accomplir [tâche] en moins de [temps]
- [ ] Ne rencontre plus [problème spécifique]
- [ ] Interface/workflow plus intuitif

**Pour le système :**
- [ ] Tests unitaires passent
- [ ] Pas de régression performance
- [ ] Documentation cohérente

## 🚀 Prochaines Étapes

1. **Analyser** le code existant concerné
2. **Implémenter** la solution minimale viable
3. **Tester** les scénarios utilisateur
4. **Documenter** les changements

---

**Créé :** [Date]
**Priorité :** [Élevée/Moyenne/Faible]
**Estimation :** [Temps approximatif]
```

### 3. Mettre à Jour l'Index

Ajouter la nouvelle tâche au `tasks/README.md` avec :
- Nom de la tâche
- Priorité
- Status
- Lien vers le fichier dans open/

## Principe Directeur

**Focus sur l'expérience utilisateur :**
- Chaque tâche doit améliorer concrètement l'usage du système
- Solutions simples et directement testables
- Documentation orientée workflow utilisateur
- Moins de bureaucratie, plus d'action

La tâche créée doit être **immédiatement compréhensible** et **rapidement implémentable**.