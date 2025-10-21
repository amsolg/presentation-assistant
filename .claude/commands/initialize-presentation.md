---
description: "Initialise une nouvelle présentation avec structure complète et validation automatique"
argument-hint: "sujet-presentation audience-cible [mode-test]"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "TodoWrite"]
---

# Initialize Presentation

Initialise une nouvelle présentation en créant la structure complète, exécutant `tools/init_presentation.py` et s'assurant que toute l'information générée est à jour et cohérente.

## Phase 1: Analyse du Contexte

### Parsing des Arguments
1. **Extraire les paramètres** depuis $ARGUMENTS :
   - Format attendu : `"sujet-presentation audience-cible [mode-test]"`
   - Exemple : `"innovation-ai c-level"` ou `"test-presentation technique true"`
   - Mode test optionnel (défaut: false)

2. **Valider les paramètres** :
   - Sujet : format kebab-case recommandé (innovation-ai, workflow-automatise, etc.)
   - Audience : audience valide (c-level, technique, marketing, formation, etc.)
   - Mode test : true/false (défaut: false si non spécifié)

3. **Confirmer avec l'utilisateur** :
   ```
   🎯 Initialisation de présentation
   Sujet    : [sujet]
   Audience : [audience]
   Mode     : [Production/Test]

   Continuer ? (Oui par défaut)
   ```

## Phase 2: Exécution de l'Initialisation

### Script d'Initialisation
1. **Exécuter init_presentation.py** :
   ```bash
   python tools/init_presentation.py [sujet] [audience] [is_test]
   ```

2. **Capturer et analyser la sortie** :
   - Vérifier que l'exécution s'est bien déroulée
   - Identifier le chemin de la structure créée
   - Noter les fichiers générés (presentation_schema.json, README.md)

3. **Gestion des erreurs** :
   - Si le dossier existe déjà : proposer des options (écraser, choisir nouveau nom, annuler)
   - Si erreur de paramètres : corriger et re-exécuter
   - Si erreur système : diagnostiquer et proposer solution

## Phase 3: Validation et Mise à Jour

### Vérification de la Structure
1. **Valider les fichiers créés** :
   - Vérifier existence de `presentation_schema.json`
   - Valider le contenu JSON (syntaxe correcte)
   - Contrôler les métadonnées (nom, sujet, audience, is_test)

2. **Examiner la structure des dossiers** :
   ```
   [presentations|tests]/[sujet]/[audience]/
   ├── presentation_schema.json ✓
   ├── README.md ✓
   ├── output/ ✓
   └── data/ ✓
   ```

3. **Vérifier la cohérence** :
   - Noms de fichiers cohérents avec les paramètres
   - Chemins de sortie correctly configurés
   - Options de build appropriées

### Optimisation du Contenu
1. **Améliorer le README.md** si nécessaire :
   - Ajouter contexte spécifique au sujet
   - Inclure instructions d'utilisation spécialisées
   - Suggérer templates de slides appropriés selon l'audience

2. **Personnaliser presentation_schema.json** :
   - Adapter le nom de présentation selon le contexte
   - Optimiser le chemin de sortie
   - Ajouter commentaires si pertinent

3. **Préparer les templates suggérés** :
   - Analyser le sujet et l'audience
   - Suggérer 3-5 templates de slides appropriés
   - Créer un fichier de suggestions `suggested_slides.md`

## Phase 4: Documentation et Guidance

### Création de la Documentation d'Aide
1. **Générer le guide de démarrage** dans le dossier créé :
   ```markdown
   # Guide de Démarrage - [Sujet] pour [Audience]

   ## 🚀 Prochaines Étapes Recommandées

   ### 1. Ajouter des Slides
   ```bash
   # Ajouter une slide de titre
   python tools/add_slide.py [chemin]/presentation_schema.json 11 ajout

   # Ajouter une table des matières
   python tools/add_slide.py [chemin]/presentation_schema.json 13 ajout
   ```

   ### 2. Templates Suggérés pour votre Audience
   - Slide X : [Nom template] - [Usage]
   - Slide Y : [Nom template] - [Usage]

   ### 3. Générer la Présentation
   ```bash
   python presentation_builder/presentation_builder.py [chemin]/presentation_schema.json
   ```
   ```

2. **Créer suggested_slides.md** avec recommandations spécifiques :
   - Pour C-Level : slides stratégiques, métriques, ROI
   - Pour Technique : détails techniques, architectures, diagrammes
   - Pour Formation : progression pédagogique, exemples
   - Pour Marketing : testimonials, case studies, bénéfices

### Validation Finale
1. **Test complet du workflow** :
   - Ajouter une slide test avec add_slide.py
   - Générer la présentation avec presentation_builder.py
   - Vérifier que le workflow complet fonctionne

2. **Nettoyage si nécessaire** :
   - Supprimer les fichiers de test
   - Réinitialiser presentation_schema.json à l'état initial
   - S'assurer que la structure est propre pour l'utilisateur

## Phase 5: Rapport et Finalisation

### Synthèse pour l'Utilisateur
1. **Présenter le résultat** :
   ```
   ✅ Présentation initialisée avec succès !

   📁 Structure créée dans : [chemin complet]
   📄 Fichiers générés :
   - presentation_schema.json (configuration principale)
   - README.md (instructions d'utilisation)
   - guide_demarrage.md (étapes recommandées)
   - suggested_slides.md (templates suggérés)

   🎯 Optimisé pour : [Audience] sur le sujet [Sujet]
   ```

2. **Fournir les commandes de suite** :
   ```bash
   # Ajouter vos premières slides :
   python tools/add_slide.py [chemin]/presentation_schema.json [template] ajout

   # Générer la présentation :
   python presentation_builder/presentation_builder.py [chemin]/presentation_schema.json
   ```

3. **Suggestions d'amélioration** :
   - Lister 3-5 templates de slides prioritaires selon l'audience
   - Proposer une séquence de construction logique
   - Indiquer les ressources additionnelles (données CSV pour graphiques, etc.)

## Utilisation

```bash
# Présentation production
/initialize-presentation "innovation-ai c-level"

# Présentation de test
/initialize-presentation "test-features technique true"

# Avec espaces dans le contexte
/initialize-presentation "workflow-automatise equipe-architecture"
```

## Adaptabilité par Audience

### C-Level
- Templates suggérés : slides stratégiques, métriques business, ROI
- Structuration : executive summary, impact, recommandations
- Style : synthétique, orienté décision

### Technique
- Templates suggérés : architectures, diagrammes, spécifications
- Structuration : problème, solution technique, implémentation
- Style : détaillé, avec preuves techniques

### Marketing
- Templates suggérés : testimonials, case studies, bénéfices
- Structuration : contexte marché, proposition valeur, call-to-action
- Style : persuasif, orienté bénéfices clients

### Formation
- Templates suggérés : progression pédagogique, exercices, synthèses
- Structuration : théorie, exemples, pratique, évaluation
- Style : pédagogique, avec étapes claires

## Avantages

- **Initialisation complète** : tout est prêt pour commencer
- **Guidance contextuelle** : suggestions adaptées au sujet/audience
- **Validation automatique** : vérification que tout fonctionne
- **Documentation intégrée** : guides et instructions inclus
- **Workflow optimisé** : de l'initialisation à la présentation finale