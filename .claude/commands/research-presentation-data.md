---
description: "Effectue une recherche documentaire approfondie pour alimenter une présentation PowerPoint"
argument-hint: "chemin/vers/sujet/audience (ex: tests/ia-generative-integration/technique)"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "WebSearch", "WebFetch", "Task"]
---

# Research Presentation Data

Effectue une recherche documentaire complète pour collecter et organiser les informations nécessaires à la création d'une présentation PowerPoint. La recherche s'adapte automatiquement selon la disponibilité des sources : dossier data local, contexte de conversation, et recherche web ciblée.

## Phase 1: Analyse du Contexte et Initialisation

### Parsing des Arguments
1. **Extraire le chemin de présentation** depuis $ARGUMENTS :
   - Format attendu : `"chemin/vers/sujet/audience"`
   - Exemples : `"tests/ia-generative-integration/technique"`, `"presentations/innovation-digitale/c-level"`
   - Identifier automatiquement : sujet, audience, et type (test/présentation)

2. **Valider la structure du projet** :
   - Vérifier l'existence du dossier de présentation
   - Localiser ou créer le dossier `data/`
   - Analyser la structure existante
   - Identifier les fichiers de configuration (config.json, audience.md, etc.)

3. **Confirmer la mission de recherche** :
   ```
   🔍 Recherche documentaire pour présentation
   Sujet     : [nom-sujet]
   Audience  : [nom-audience]
   Type      : [test/présentation]
   Dossier   : [chemin-complet]

   Démarrage de la recherche documentaire...
   ```

## Phase 2: Analyse des Sources Existantes

### Exploration du Dossier Data Local
1. **Scanner le contenu existant** :
   ```bash
   ls -la [chemin]/data/
   find [chemin]/data/ -type f -name "*.md" -o -name "*.json" -o -name "*.csv" -o -name "*.txt"
   ```
   - Inventorier tous les fichiers présents
   - Analyser les types de documents (rapports, données, notes)
   - Identifier les lacunes informationnelles

2. **Analyser la qualité des données existantes** :
   - Lire chaque fichier présent dans le dossier data
   - Évaluer la pertinence pour la présentation
   - Identifier les informations manquantes ou obsolètes
   - Noter les sources et dates des informations

3. **Évaluation de complétude** :
   - Déterminer si les données existantes sont suffisantes
   - Identifier les gaps informationnels spécifiques
   - Prioriser les besoins de recherche complémentaire

### Exploration du Contexte Projet
1. **Analyser les fichiers de configuration** :
   - Lire `audience.md` (profil d'audience détaillé)
   - Examiner `content-brief.md` (documentation adaptée)
   - Consulter `README.md` du sujet (contexte global)
   - Analyser `config.json` (configuration technique)

2. **Explorer la documentation existante** :
   - Parcourir le dossier `documentation/` si présent
   - Lire `context.md` et `research_log.md`
   - Examiner les sources dans `documentation/sources/`

## Phase 3: Recherche Contextuelle dans la Conversation

### Analyse de l'Historique de Conversation
1. **Extraire les informations pertinentes** :
   - Identifier les discussions précédentes sur le sujet
   - Capturer les définitions et explications fournies
   - Noter les références et liens mentionnés
   - Compiler les exemples et cas d'usage discutés

2. **Synthétiser le contexte conversationnel** :
   - Organiser les informations par thème
   - Identifier les angles d'approche privilégiés
   - Noter les préférences exprimées pour l'audience
   - Capturer les objectifs spécifiques mentionnés

## Phase 4: Recherche Web Ciblée

### Stratégie de Recherche Adaptée à l'Audience
1. **Adapter la recherche selon le profil d'audience** :
   - **C-Level** : Stratégie, ROI, impact business, études de cas, tendances marché
   - **Technique** : Spécifications, architectures, comparaisons, benchmarks, documentation technique
   - **Formation** : Concepts de base, tutoriels, guides pratiques, exemples step-by-step
   - **Marketing** : Case studies, adoption rates, success stories, témoignages clients

2. **Recherche par thématiques prioritaires** :
   - Définitions et concepts clés du sujet
   - État de l'art et meilleures pratiques actuelles
   - Études de cas et exemples concrets
   - Statistiques et données quantitatives récentes
   - Tendances et perspectives d'évolution

3. **Sources et références fiables** :
   - Documentation officielle et whitepapers
   - Études d'analystes reconnus (Gartner, Forrester, etc.)
   - Articles académiques et publications spécialisées
   - Témoignages clients et retours d'expérience
   - Données statistiques d'organismes officiels

### Recherche Web Systématique
```bash
# Recherche principale sur le sujet
WebSearch: "[sujet] best practices 2024"
WebSearch: "[sujet] implementation guide [audience-type]"
WebSearch: "[sujet] case studies success stories"
WebSearch: "[sujet] statistics market trends 2024"

# Recherche spécialisée par audience
# Si C-Level:
WebSearch: "[sujet] business value ROI executive"
WebSearch: "[sujet] strategic implementation enterprise"

# Si Technique:
WebSearch: "[sujet] technical architecture implementation"
WebSearch: "[sujet] developer guide specifications"

# Si Formation:
WebSearch: "[sujet] beginner guide tutorial"
WebSearch: "[sujet] learning path step by step"
```

## Phase 5: Synthèse et Organisation des Données

### Structure du Rapport de Recherche
```markdown
# Rapport de Recherche : [Sujet] pour [Audience]

## Résumé Exécutif
- **Objectif de recherche** : [Description]
- **Sources consultées** : [Liste]
- **Principales découvertes** : [Points clés]
- **Recommandations** : [Actions suggérées]

## Contexte et Définitions

### Définition du Sujet
- [Définition claire et concise]
- [Contexte d'application]
- [Périmètre et limites]

### Enjeux pour l'Audience
- [Pourquoi c'est important pour cette audience]
- [Impact et bénéfices attendus]
- [Défis et obstacles typiques]

## État de l'Art

### Meilleures Pratiques Actuelles
- [Liste des pratiques recommandées]
- [Standards de l'industrie]
- [Méthodologies éprouvées]

### Tendances et Évolutions
- [Tendances émergentes]
- [Évolutions technologiques]
- [Perspectives d'avenir]

## Données et Statistiques

### Chiffres Clés
- [Statistiques d'adoption]
- [Données de marché]
- [Métriques de performance]

### Benchmarks et Comparaisons
- [Comparaisons de solutions]
- [Benchmarks de performance]
- [Analyses concurrentielles]

## Études de Cas et Exemples

### Cas de Succès
- [Exemples d'implémentations réussies]
- [Témoignages clients]
- [Retours d'expérience positifs]

### Leçons Apprises
- [Erreurs communes à éviter]
- [Facteurs critiques de succès]
- [Recommandations pratiques]

## Sources et Références

### Sources Internes
- [Documents internes consultés]
- [Conversations et contexte projet]

### Sources Externes
- [Articles et publications]
- [Sites web et documentation]
- [Études et rapports]

## Recommandations pour la Présentation

### Messages Clés
- [3-5 messages principaux à transmettre]
- [Arguments de persuasion]
- [Preuves et validations]

### Structure Suggérée
- [Organisation optimale du contenu]
- [Séquence logique des arguments]
- [Points d'emphasis recommandés]

### Éléments Visuels Proposés
- [Types de graphiques utiles]
- [Données à visualiser]
- [Exemples à illustrer]

## Annexes

### Glossaire
- [Définitions des termes techniques]

### Références Complètes
- [Liste exhaustive des sources]

### Données Brutes
- [Tableaux de données]
- [Statistiques détaillées]
```

## Phase 6: Production et Validation

### Création du Rapport
1. **Générer le rapport principal** :
   - Nom : `research_report_[date].md`
   - Emplacement : `[chemin]/data/research_report_[date].md`

2. **Organiser les fichiers de support** :
   - Créer sous-dossiers si nécessaire (sources, images, data)
   - Sauvegarder les références web importantes
   - Organiser les données brutes collectées

3. **Mise à jour du log de recherche** :
   - Ajouter l'entrée dans `documentation/research_log.md` si existant
   - Documenter les sources consultées et méthodes utilisées

### Validation du Contenu
1. **Vérification de la complétude** :
   - Toutes les sections sont remplies avec contenu substantiel
   - Les sources sont citées et vérifiables
   - Les données sont récentes et pertinentes

2. **Adaptation à l'audience** :
   - Le niveau de détail correspond au profil d'audience
   - Le vocabulaire est approprié
   - Les exemples sont pertinents

3. **Qualité et fiabilité** :
   - Sources diverses et crédibles
   - Informations cross-validées quand possible
   - Biais identifiés et mentionnés

## Phase 7: Livrables et Recommandations

### Rapport de Mission
```
✅ Recherche documentaire complétée avec succès !

📁 Fichier créé : [chemin-complet]/data/research_report_[date].md
📊 Sources consultées :
- Dossier data local : [✓/Vide/N/A]
- Contexte conversation : [✓/N/A]
- Recherche web : [nombre] sources
- Documentation projet : [✓/N/A]

📋 Contenu du rapport :
- Contexte et définitions
- État de l'art et meilleures pratiques
- Données et statistiques récentes
- Études de cas et exemples concrets
- Recommandations pour la présentation

🎯 Optimisé pour audience : [type-audience]
📈 Qualité des données : [Élevée/Moyenne/Basique]
🔄 Dernière mise à jour : [date]

💡 Suggestions d'utilisation :
- Consulter en priorité la section "Messages Clés"
- Utiliser les études de cas pour les exemples
- S'appuyer sur les statistiques pour les arguments
- Suivre la structure suggérée pour la présentation
```

### Actions de Suivi Recommandées
1. **Pour la création de contenu** :
   - Utiliser les messages clés comme base narrative
   - Intégrer les statistiques dans les slides de données
   - Adapter les exemples au format de présentation

2. **Pour l'optimisation continue** :
   - Mettre à jour le rapport si nouvelles informations
   - Compléter avec feedback après présentation
   - Enrichir pour futures présentations similaires

## Utilisation

```bash
# Recherche pour un projet de test
/research-presentation-data "tests/ia-generative-integration/technique"

# Recherche pour une présentation executive
/research-presentation-data "presentations/innovation-digitale/c-level"

# Recherche avec chemin relatif
/research-presentation-data "presentations/hygiene-mains/formation"
```

## Avantages

- **Recherche exhaustive** : Combine toutes sources disponibles (local, conversation, web)
- **Adaptation contextuelle** : Contenu optimisé selon audience et sujet
- **Organisation structurée** : Rapport réutilisable et maintenable
- **Sources fiables** : Priorisation des sources crédibles et récentes
- **Intégration workflow** : S'intègre parfaitement dans le processus de création
- **Traçabilité complète** : Documentation des sources et méthodes utilisées
- **Qualité professionnelle** : Rapport de niveau consulting pour alimenter présentations Premier Tech