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
   - Noter les fichiers générés (config.json, README.md)

3. **Gestion des erreurs** :
   - Si le dossier existe déjà : proposer des options (écraser, choisir nouveau nom, annuler)
   - Si erreur de paramètres : corriger et re-exécuter
   - Si erreur système : diagnostiquer et proposer solution

## Phase 3: Validation et Mise à Jour

### Vérification de la Structure
1. **Valider les fichiers créés** :
   - Vérifier existence de `config.json`
   - Valider le contenu JSON (syntaxe correcte)
   - Contrôler les métadonnées (nom, sujet, audience, is_test)

2. **Examiner la structure des dossiers** :
   ```
   [presentations|tests]/[sujet]/[audience]/
   ├── config.json ✓
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

2. **Personnaliser config.json** :
   - Adapter le nom de présentation selon le contexte
   - Optimiser le chemin de sortie
   - Ajouter commentaires si pertinent

3. **Préparer les templates suggérés** :
   - Analyser le sujet et l'audience
   - Suggérer 3-5 templates de slides appropriés
   - Créer un fichier de suggestions `suggested_slides.md`

## Phase 4: Orchestration Intelligente des Commandes

### 🤖 **Exécution Autonome des Commandes Suivantes**

Claude peut automatiquement enchaîner les commandes suivantes selon les besoins identifiés :

1. **Évaluation automatique** :
   - **Si audience nouvelle ou inconnue** → Exécuter automatiquement `/research-audience`
   - **Si sujet complexe nécessitant recherche** → Exécuter automatiquement `/research-presentation-data`
   - **Si données disponibles** → Exécuter automatiquement `/adapt-content-for-audience`
   - **Si contenu adapté disponible** → Proposer `/create-presentation-plan`

2. **Workflow complet recommandé** :
   ```bash
   # Ordre d'exécution optimal (automatique par Claude)
   /initialize-presentation "sujet audience"       # ← Commande initiale
   /research-audience "audience"                   # ← Si nécessaire
   /research-presentation-data "sujet/audience"    # ← Si nécessaire
   /adapt-content-for-audience "..." "..."         # ← Adaptation intelligente
   /create-presentation-plan "sujet/audience"      # ← Plan stratégique
   /add-slide "layout" position                    # ← Ajout de slides (répétable)
   /generate-presentation "config.json"            # ← Génération finale avec validation
   ```

3. **Intelligence d'orchestration** :
   - **Détection automatique** : Claude identifie les besoins sans instruction explicite
   - **Exécution séquentielle** : Respect de l'ordre optimal pour la qualité
   - **Adaptation contextuelle** : Ajustement selon le type de présentation
   - **Usage autonome** : Chaque commande peut être utilisée indépendamment

## Phase 5: Documentation et Guidance

### Création de la Documentation d'Aide
1. **Générer le guide de démarrage** dans le dossier créé :
   ```markdown
   # Guide de Démarrage - [Sujet] pour [Audience]

   ## 🚀 Workflow Recommandé

   L'initialisation a créé la structure de base. Claude peut maintenant automatiquement :

   1. **Analyser l'audience** (si nouvelle) - `/research-audience`
   2. **Rechercher le contenu** (si nécessaire) - `/research-presentation-data`
   3. **Adapter le contenu** pour l'audience - `/adapt-content-for-audience`
   4. **Créer un plan stratégique** - `/create-presentation-plan`
   5. **Ajouter des slides** personnalisées - `/add-slide`
   6. **Générer la présentation** finale - `/generate-presentation`

   ## 🤖 Usage Autonome

   Chaque commande peut être utilisée indépendamment selon les besoins :
   - Modification d'audience → `/research-audience`
   - Nouveau contenu → `/research-presentation-data`
   - Réadaptation → `/adapt-content-for-audience`
   - Nouveau plan → `/create-presentation-plan`
   - Ajout de slides → `/add-slide`
   - Génération finale → `/generate-presentation`

   ### 1. Prochaines Étapes Recommandées
   ```bash
   # Ajouter une slide de titre
   python tools/add_slide.py [chemin]/config.json 11 ajout

   # Ajouter une table des matières
   python tools/add_slide.py [chemin]/config.json 13 ajout
   ```

   ### 2. Templates Suggérés pour votre Audience
   - Slide X : [Nom template] - [Usage]
   - Slide Y : [Nom template] - [Usage]

   ### 3. Générer la Présentation
   ```bash
   python presentation_builder/presentation_builder.py [chemin]/config.json
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
   - Réinitialiser config.json à l'état initial
   - S'assurer que la structure est propre pour l'utilisateur

## Phase 5: Rapport et Finalisation

### Synthèse pour l'Utilisateur
1. **Présenter le résultat** :
   ```
   ✅ Présentation initialisée avec succès !

   📁 Structure créée dans : [chemin complet]
   📄 Fichiers générés :
   - config.json (configuration principale)
   - README.md (instructions d'utilisation)
   - guide_demarrage.md (étapes recommandées)
   - suggested_slides.md (templates suggérés)

   🎯 Optimisé pour : [Audience] sur le sujet [Sujet]
   ```

2. **Fournir les commandes de suite** :
   ```bash
   # Ajouter vos premières slides :
   python tools/add_slide.py [chemin]/config.json [template] ajout

   # Générer la présentation :
   python presentation_builder/presentation_builder.py [chemin]/config.json
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