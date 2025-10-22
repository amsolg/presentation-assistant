---
description: "Génère un plan stratégique de présentation basé sur l'adaptation de contenu pour l'audience"
argument-hint: "chemin/vers/audience [output_path]"
allowed-tools: ["Read", "Write", "Edit", "Glob", "Grep"]
---

# Create Presentation Plan

Génère un plan stratégique et structurel de haut niveau pour une présentation, en utilisant les résultats de l'adaptation de contenu pour audience spécifique. Cette commande doit être exécutée après `/adapt-content-for-audience` et produit un plan directeur qui oriente la création du contenu des slides.

## Instructions

Tu dois créer un plan de présentation stratégique en analysant le contenu adapté et en structurant la présentation de manière optimale pour l'audience cible.

### Phase 1: Collecte et Analyse des Sources

1. **Localiser le contenu adapté** :
   - Si $ARGUMENTS contient un chemin spécifique, l'utiliser comme base
   - Chercher le fichier `content-brief-adapted-*.md` le plus récent dans le répertoire spécifié
   - Alternative : chercher `content-brief.md` s'il existe
   - Lire également le `config.json` pour comprendre le contexte de présentation existant

2. **Analyser le contexte de présentation** :
   - **Sujet principal** : Extraire le thème central de la présentation
   - **Audience cible** : Identifier le profil, niveau d'expertise, préférences
   - **Objectifs** : Comprendre les buts de communication et actions attendues
   - **Contraintes** : Noter les limites de temps, format, complexité

3. **Extraire les éléments clés du contenu adapté** :
   - Messages clés hiérarchisés par importance
   - Données et statistiques prioritaires
   - Exemples et cas d'usage pertinents
   - Recommandations d'action spécifiques
   - Structure narrative optimale

### Phase 2: Conception Stratégique de la Présentation

1. **Définir l'arc narratif** :
   - **Ouverture** : Type d'accroche adapté à l'audience
   - **Développement** : Progression logique des arguments
   - **Climax** : Point d'impact maximum
   - **Conclusion** : Call-to-action et prochaines étapes

2. **Structurer par sections logiques** :
   - Découper le contenu en blocs cohérents
   - Définir les transitions entre sections
   - Équilibrer la charge informationnelle
   - Optimiser le timing selon l'attention de l'audience

3. **Mapper les layouts Premier Tech** :
   - Identifier les types de slides optimaux pour chaque section
   - Sélectionner les layouts les plus appropriés du catalogue des 57 slides
   - Prévoir la répartition des contenus visuels vs textuels
   - Planifier les moments d'interaction ou de pause

### Phase 3: Planification Détaillée par Slide

1. **Définir la séquence de slides** :
   - **Slide d'ouverture** : Titre, accroche, agenda
   - **Slides de contexte** : Problématique, enjeux, définitions
   - **Slides de développement** : Arguments, preuves, exemples
   - **Slides de synthèse** : Récapitulatif, recommandations
   - **Slide de conclusion** : Actions, next steps, contact

2. **Pour chaque slide, spécifier** :
   - **Layout recommandé** : Nom du layout Premier Tech optimal
   - **Objectif de communication** : But spécifique de cette slide
   - **Contenu principal** : Messages et informations clés
   - **Éléments visuels** : Type de données à visualiser
   - **Durée estimée** : Temps de narration prévu

3. **Optimiser pour l'audience** :
   - Adapter le niveau de détail selon l'expertise
   - Intégrer les préférences de communication identifiées
   - Respecter la durée d'attention optimale
   - Placer les éléments d'engagement aux moments stratégiques

### Phase 4: Production du Plan Stratégique

Générer un plan complet avec cette structure :

```markdown
# Plan de Présentation : [Titre] pour [Audience]

## Vue d'Ensemble Stratégique

### Objectifs de Communication
- **Objectif principal** : [But primaire de la présentation]
- **Objectifs secondaires** : [Buts de support]
- **Indicateurs de succès** : [Métriques de réussite]

### Profil d'Audience
- **Type** : [Profil et niveau d'expertise]
- **Besoins informationnels** : [Attentes prioritaires]
- **Préférences communication** : [Style et format optimal]
- **Durée d'attention** : [Timing optimal]

### Messages Clés Hiérarchisés
1. **Message principal** : [Argument central]
2. **Messages de support** : [Arguments secondaires]
3. **Call-to-action** : [Action attendue]

## Architecture de Présentation

### Arc Narratif
- **Ouverture** (X min) : [Type d'accroche et objectif]
- **Développement** (X min) : [Progression des arguments]
- **Conclusion** (X min) : [Synthèse et actions]
- **Durée totale** : [Estimation précise]

### Structure par Sections

#### Section 1: [Titre Section]
- **Objectif** : [But de cette section]
- **Durée** : [Temps alloué]
- **Messages clés** : [Points à faire passer]
- **Slides prévues** : [Nombre estimé]

#### Section 2: [Titre Section]
- [Même structure]

### Répartition Temporelle
- Introduction : X% (X min)
- Développement : X% (X min)
- Conclusion : X% (X min)
- Questions : X% (X min)

## Plan Détaillé par Slide

### Slide 1: [Titre]
- **Layout recommandé** : "Page titre"
- **Objectif** : Capter l'attention et présenter le sujet
- **Contenu principal** :
  - Titre de présentation percutant
  - Sous-titre contextuel
  - Date et métadonnées
- **Durée narration** : ~15s
- **Notes de personnalisation** : [Adaptations spécifiques à l'audience]

### Slide 2: [Titre]
- **Layout recommandé** : [Layout optimal]
- **Objectif** : [But spécifique]
- **Contenu principal** :
  - [Éléments principaux]
  - [Données à inclure]
- **Durée narration** : ~15s
- **Notes de personnalisation** : [Adaptations]

[Continuer pour toutes les slides prévues]

## Optimisations par Audience

### Adaptations Linguistiques
- **Vocabulaire** : [Niveau technique approprié]
- **Ton** : [Style de communication]
- **Exemples** : [Types de références pertinentes]

### Éléments Visuels Stratégiques
- **Types de graphiques** : [Formats optimaux pour l'audience]
- **Niveau de complexité** : [Adaptation selon l'expertise]
- **Données prioritaires** : [Métriques les plus impactantes]

### Points d'Interaction
- **Moments de pause** : [Timing optimal selon attention]
- **Questions d'engagement** : [Types d'interaction appropriés]
- **Transitions participatives** : [Méthodes pour maintenir l'attention]

## Ressources et Données Clés

### Statistiques Prioritaires
- [Chiffres les plus impactants pour cette audience]
- [Métriques de performance pertinentes]
- [Comparaisons et benchmarks appropriés]

### Exemples et Cas d'Usage
- [Études de cas sélectionnées pour l'audience]
- [Témoignages et retours d'expérience pertinents]
- [Démonstrations ou preuves adaptées]

### Sources et Références
- [Autorités reconnues par l'audience]
- [Types de validation importantes]
- [Crédibilité des sources selon le profil]

## Recommandations de Mise en Œuvre

### Préparation de la Narration
- **Style de présentation** : [Adapté au profil audience]
- **Rythme recommandé** : [Vitesse et pauses optimales]
- **Éléments d'emphasis** : [Points à souligner particulièrement]

### Configuration Technique
- **Format de diffusion** : [Modalités optimales]
- **Supports visuels** : [Éléments complémentaires nécessaires]
- **Interactivité** : [Niveau d'engagement recommandé]

### Gestion du Timing
- **Points de contrôle** : [Moments de vérification du timing]
- **Ajustements possibles** : [Éléments modulables]
- **Plan de backup** : [Solutions si contraintes temporelles]

## Métriques de Succès

### Indicateurs de Réception
- [Comment mesurer l'engagement de l'audience]
- [Signaux de compréhension à observer]
- [Critères de réussite de la communication]

### Objectifs Mesurables
- [Résultats attendus concrets]
- [Actions post-présentation souhaitées]
- [Indicateurs de performance spécifiques]

---

*Plan généré automatiquement à partir de l'adaptation de contenu*
*Basé sur : [sources-contenu-adapté]*
*Optimisé pour : [profil-audience-spécifique]*
*Date de génération : [date-actuelle]*
```

### Phase 5: Validation et Optimisation

1. **Contrôle de cohérence** :
   - Vérifier l'alignement avec les objectifs de communication
   - Valider la pertinence pour l'audience spécifique
   - Confirmer la faisabilité temporelle

2. **Optimisation stratégique** :
   - Équilibrer les sections selon l'importance
   - Ajuster le niveau de détail selon l'expertise
   - Optimiser les transitions et le flow narratif

3. **Intégration avec le workflow** :
   - Préparer les recommandations pour la création des slides
   - Identifier les layouts Premier Tech optimaux
   - Prévoir les besoins en personnalisation de contenu

### Phase 6: Production et Livraison

1. **Génération du fichier plan** :
   - Nom : `presentation-plan-[date].md`
   - Emplacement : `[chemin-audience]/presentation-plan-[date].md`
   - Mise à jour du README.md du projet si existant

2. **Rapport de génération** :
   ```
   ✅ Plan de présentation généré avec succès !

   📁 Fichier : [chemin-complet]
   🎯 Audience : [profil-audience]
   📊 Basé sur : [sources-adaptation]

   📋 Plan structuré :
   - Slides prévues : [nombre]
   - Durée estimée : [timing]
   - Sections définies : [nombre]
   - Layouts identifiés : [types]

   🎯 Optimisé pour :
   - Niveau d'expertise de l'audience
   - Préférences de communication
   - Contraintes temporelles
   - Objectifs de performance

   💡 Prêt pour :
   - Création du config.json détaillé
   - Personnalisation des slides
   - Génération de la présentation
   ```

## Utilisation

```bash
# Génération avec chemin spécifique
/create-presentation-plan "presentations/innovation-digitale/c-level"

# Génération avec output personnalisé
/create-presentation-plan "tests/ia-generative/technique" "presentations/plan-final.md"
```

Cette commande peut être utilisée de manière autonome après `/adapt-content-for-audience` et fournit la base stratégique pour la création optimisée de la présentation finale.