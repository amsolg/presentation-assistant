---
description: "Recherche et documente un guide spécifique pour une audience de présentation"
argument-hint: "nom-audience [type: individual|group]"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "WebSearch", "WebFetch"]
---

# Research Audience

Recherche une audience spécifique et génère un guide complet sur le type d'information pertinent et le format de présentation optimal pour maximiser l'intérêt et la durée d'attention.

## Phase 1: Analyse et Classification de l'Audience

### Parsing des Arguments
1. **Extraire les paramètres** depuis $ARGUMENTS :
   - Format attendu : `"nom-audience [type]"`
   - Exemples : `"c-level"`, `"john-doe individual"`, `"equipe-architecture group"`
   - Type optionnel : `individual`, `group` (défaut: audience générale)

2. **Déterminer le type d'audience** :
   - **Audience générale** : Persona type (c-level, technique, marketing, formation)
   - **Individu** : Personne spécifique (nom ou acronyme)
   - **Groupe** : Équipe ou département spécifique

3. **Confirmer la recherche** :
   ```
   🎯 Recherche d'audience pour présentation
   Audience : [nom]
   Type     : [general/individual/group]

   Démarrage de la recherche...
   ```

## Phase 2: Recherche Documentaire Stratégique

### Source Principale : Stratégie de Diffusion
1. **Analyser docs\strategie-diffusion-connaissances.md** :
   - Extraire les personas correspondants
   - Identifier les caractéristiques clés
   - Noter les besoins informationnels spécifiques
   - Comprendre l'état d'esprit et approche de communication

2. **Mapping avec les 4 Personas de Référence** :
   - **Leader Stratégique** : C-suite, VP, Directeurs
   - **Manager Tactique** : Chefs de projet, directeurs de programme
   - **Spécialiste Technique** : Développeurs, ingénieurs, architectes
   - **Utilisateur Métier** : Ventes, marketing, RH, finance

### Recherche Individuelle (Si type = individual)
1. **Localiser la fiche individuelle** :
   - Chemin : `C:\Users\max_o\OneDrive - Premier Tech\PTOS\Organizational Structure\Team Members`
   - **Utiliser la commande `find`** pour localiser le fichier de l'individu :
     ```bash
     find "C:\Users\max_o\OneDrive - Premier Tech\PTOS\Organizational Structure\Team Members" -name "*nom-individu*" -type f
     ```
   - Rechercher par nom complet, prénom, nom de famille, ou acronyme
   - Lire la fiche individuelle complète

2. **Analyser les relations managériales** :
   - **Utiliser `grep` pour identifier si l'individu est gestionnaire** :
     ```bash
     grep -r "nom-individu" "C:\Users\max_o\OneDrive - Premier Tech\PTOS\Organizational Structure\Team Members"
     ```
   - Cette recherche révèle si le nom apparaît dans les fiches d'autres équipiers
   - Identifier les relations hiérarchiques et les équipes gérées

3. **Navigation en graphe de connaissances** :
   - **Si la fiche manque de description, navigation obligatoire** :
     - Suivre les références et liens dans la fiche (format `[[Nom - Acronyme]]`)
     - Explorer les projets mentionnés
     - Analyser les connexions organisationnelles
     - Reconstituer le profil via les relations
   - **Recherche étendue pour documents référencés** :
     - Les documents référencés peuvent se trouver dans d'autres dossiers
     - **Utiliser recherche depuis le dossier parent** :
       ```bash
       find "C:\Users\max_o\OneDrive - Premier Tech\PTOS\Organizational Structure" -name "*terme-recherche*" -type f
       ```
     - Exploration des dossiers connexes :
       - `Applications/` : Applications et outils utilisés par l'individu
       - `Projects/` : Projets spécifiques (Digital Projects, Non-Digital)
       - `Teams/` : Descriptions d'équipes détaillées
       - `Companies/` : Information sur les entités corporatives (PTSA, PTG, etc.)
       - `Technical Capabilities/` : Compétences techniques organisationnelles
       - `Business Capabilities/` : Capacités métier
   - Identifier les connexions et relations
   - Mapper le réseau d'expertise
   - Comprendre le contexte organisationnel
   - Analyser les projets et responsabilités

4. **Construction du profil personnalisé** :
   - Expertise technique spécifique
   - Style de communication préféré
   - Projets actuels et passés
   - Position dans l'organigramme
   - Réseaux internes et externes

### Recherche Groupe (Si type = group)
1. **Identifier les membres du groupe** :
   - Lister tous les individus du groupe
   - Analyser la composition de l'équipe
   - Identifier les rôles et hiérarchies

2. **Recherche individuelle pour chaque membre** :
   - Appliquer le processus individuel pour chaque personne
   - Créer un profil pour chaque membre dans `docs\audience\individuals`

3. **Analyse collective du groupe** :
   - Identifier les patterns communs
   - Reconnaître les diversités d'expertise
   - Déterminer les dynamiques de groupe

### Recherche Web Complémentaire
Si la documentation interne est insuffisante :

1. **Recherche par persona général** :
   - Meilleures pratiques de communication pour le type d'audience
   - Formats de présentation optimaux
   - Durée d'attention typique
   - Préférences de contenu

2. **Recherche spécialisée par domaine** :
   - Si technique : rechercher formats techniques populaires
   - Si business : rechercher styles exécutifs efficaces
   - Si formation : rechercher méthodes pédagogiques

## Phase 3: Construction du Guide d'Audience

### Structure du Guide Standard
```markdown
# Guide d'Audience : [Nom de l'Audience]

## Profil de l'Audience

### Caractéristiques Clés
- **Rôle/Position** : [Description]
- **Niveau d'expertise** : [Technique/Business/Mixte]
- **Temps disponible** : [Estimation]
- **Objectifs principaux** : [Liste]

### Question Principale
"[Question que se pose cette audience]"

## Besoins Informationnels

### Informations Prioritaires
- [Liste des types d'information essentiels]
- [Niveau de détail requis]
- [Contexte nécessaire]

### Informations Secondaires
- [Éléments de support]
- [Contexte additionnel]

## Format de Présentation Optimal

### Structure Recommandée
1. **Ouverture** : [Type d'accroche]
2. **Développement** : [Organisation du contenu]
3. **Conclusion** : [Type de call-to-action]

### Durée et Rythme
- **Durée totale recommandée** : [Minutes]
- **Nombre de slides optimal** : [Estimation]
- **Rythme de narration** : [Descriptif]

### Style Visuel
- **Complexité graphique** : [Simple/Moyen/Complexe]
- **Types de visuels préférés** : [Liste]
- **Couleurs et branding** : [Directives]

## Stratégie de Communication

### Ton et Style
- **Registre de langue** : [Formel/Semi-formel/Accessible]
- **Niveau technique** : [Vulgarisation/Technique/Expert]
- **Approche narrative** : [Descriptif]

### Messages Clés à Privilégier
- [Types de messages qui résonnent]
- [Angles d'approche efficaces]
- [Preuves et validations importantes]

### Pièges à Éviter
- [Ce qui peut perdre l'attention]
- [Erreurs de communication typiques]
- [Sujets à traiter avec précaution]

## Recommandations Spécifiques

### Templates de Slides Suggérés
- [Liste des templates Premier Tech appropriés]
- [Séquence recommandée]

### Éléments d'Engagement
- [Techniques pour maintenir l'attention]
- [Points d'interaction recommandés]

### Métriques de Succès
- [Comment mesurer l'efficacité]
- [Indicateurs d'engagement]

## Exemples et Cas d'Usage

### Sujets Adaptés
- [Types de présentations appropriés]
- [Exemples de sujets qui fonctionnent bien]

### Adaptations par Contexte
- [Variations selon le contexte de présentation]
- [Ajustements pour différents formats]
```

## Phase 4: Production et Organisation

### Placement des Fichiers

#### Pour Audiences Générales
- **Chemin** : `docs\audience\[nom-audience].md`
- **Nom fichier** : Basé sur le type d'audience (c-level.md, technique.md, etc.)

#### Pour Individus
- **Chemin** : `docs\audience\individuals\[nom-individu].md`
- **Nom fichier** : Basé sur le nom de la personne

#### Pour Groupes
- **Chemin principal** : `docs\audience\groups\[nom-groupe].md`
- **Fichiers individuels** : `docs\audience\individuals\[nom-membre].md` pour chaque membre

### Création des Dossiers
1. **Vérifier et créer la structure** :
   ```bash
   mkdir -p docs/audience/individuals
   mkdir -p docs/audience/groups
   ```

2. **Générer le guide principal** selon le type d'audience

3. **Si groupe** : Créer les guides individuels pour chaque membre

## Phase 5: Validation et Enrichissement

### Validation du Contenu
1. **Cohérence avec la stratégie de diffusion** :
   - Vérifier alignement avec les personas de référence
   - Confirmer que les recommandations suivent les meilleures pratiques

2. **Complétude du guide** :
   - Tous les sections sont remplies
   - Recommandations spécifiques et actionnables
   - Exemples concrets fournis

3. **Réutilisabilité** :
   - Guide indépendant de toute présentation spécifique
   - Applicable à différents sujets
   - Mise à jour facile

### Enrichissement par Recherche Web
Si les informations internes sont insuffisantes :

1. **Rechercher les meilleures pratiques** pour le type d'audience
2. **Identifier les tendances** de communication récentes
3. **Intégrer des références** et sources externes pertinentes

## Phase 6: Rapport et Recommandations

### Synthèse pour l'Utilisateur
```
✅ Guide d'audience généré avec succès !

📁 Fichier créé : [chemin complet]
🎯 Type d'audience : [type]
📊 Basé sur : [sources utilisées]

🔍 Recherche effectuée :
- Stratégie de diffusion : ✓
- Base de connaissances PT : [✓/N/A]
- Navigation graphe connaissances : [✓/N/A]
- Recherche web complémentaire : [✓/N/A]

📋 Guide inclut :
- Profil détaillé de l'audience
- Besoins informationnels spécifiques
- Format de présentation optimal
- Stratégie de communication adaptée
- Templates de slides suggérés

🗂️ Documents connexes explorés (si applicable) :
- Applications utilisées : [nombre]
- Projets associés : [nombre]
- Connexions organisationnelles : [description]
```

### Suggestions d'Utilisation
1. **Pour créer une présentation** :
   - Consulter le guide avant de démarrer
   - Adapter le contenu selon les recommandations
   - Utiliser les templates suggérés

2. **Pour optimiser une présentation existante** :
   - Comparer avec les recommandations du guide
   - Ajuster le format et le style
   - Vérifier la durée et le rythme

## Utilisation

```bash
# Audience générale
/research-audience "c-level"

# Individu spécifique
/research-audience "john-doe individual"

# Groupe d'équipe
/research-audience "equipe-architecture group"
```

## Avantages

- **Recherche exhaustive** : Combine sources internes et externes
- **Guides réutilisables** : Applicables à de multiples présentations
- **Personnalisation avancée** : Adaptation fine selon le profil d'audience
- **Navigation en graphe** : Utilise la base de connaissances Premier Tech
- **Stratégie validée** : Basé sur la méthodologie de diffusion documentée
- **Organisation claire** : Structure hiérarchique des guides d'audience