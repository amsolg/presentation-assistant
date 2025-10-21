---
description: "Adapte l'information de recherche documentaire pour une audience spécifique de présentation"
argument-hint: "chemin/vers/audience (ex: tests/ia-generative-integration/technique) chemin/vers/guide-audience (ex: docs/audience/technique.md)"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "SlashCommand"]
---

# Adapt Content For Audience

Génère un rapport d'information adapté pour une audience spécifique de présentation en combinant intelligemment les données de recherche documentaire avec le guide d'audience correspondant. Cette commande produit un contenu personnalisé optimisé pour maximiser l'engagement et l'efficacité de la présentation.

## Phase 1: Validation et Préparation

### Parsing des Arguments
1. **Extraire les chemins** depuis $ARGUMENTS :
   - Format attendu : `"chemin/vers/audience chemin/vers/guide-audience"`
   - Exemple : `"tests/ia-generative-integration/technique docs/audience/technique.md"`
   - Premier argument : Dossier de présentation audience-spécifique
   - Deuxième argument : Chemin vers le guide d'audience créé par `/research-audience`

2. **Validation des prérequis** :
   - Vérifier l'existence du dossier de présentation
   - Localiser le dossier `data/` parent pour les résultats de recherche
   - Vérifier l'existence du guide d'audience spécifié
   - Identifier les documents de recherche disponibles

3. **Génération automatique si manquant** :
   - **Si dossier data vide ou inexistant** :
     ```bash
     /research-presentation-data "[chemin-vers-audience]"
     ```
   - **Si guide d'audience manquant** :
     ```bash
     /research-audience "[nom-audience-extrait]"
     ```

4. **Confirmation de la mission** :
   ```
   🎯 Adaptation de contenu pour présentation
   Audience      : [nom-audience]
   Dossier       : [chemin-complet]
   Guide audience: [chemin-guide]

   Démarrage de l'adaptation contextuelle...
   ```

## Phase 2: Analyse des Sources

### Chargement du Guide d'Audience
1. **Lire le guide d'audience complet** :
   - Extraire les caractéristiques clés de l'audience
   - Identifier les besoins informationnels prioritaires
   - Noter le format de présentation optimal
   - Comprendre la stratégie de communication recommandée

2. **Analyser les préférences** :
   - Niveau de détail technique requis
   - Durée d'attention optimale
   - Types de visuels préférés
   - Ton et style de communication

### Chargement des Données de Recherche
1. **Scanner le dossier data parent** :
   ```bash
   find [chemin-parent]/data/ -type f -name "*.md" -o -name "*.json" -o -name "*.csv"
   ```
   - Identifier tous les rapports de recherche disponibles
   - Prioriser les documents les plus récents
   - Analyser la complétude des informations

2. **Lire les documents de recherche** :
   - Rapport principal de recherche documentaire
   - Données et statistiques collectées
   - Études de cas et exemples
   - Sources et références

## Phase 3: Adaptation Intelligente du Contenu

### Filtrage par Pertinence Audience
1. **Sélection des informations prioritaires** :
   - Croiser les besoins informationnels de l'audience avec les données disponibles
   - Filtrer selon le niveau d'expertise (technique/business/général)
   - Adapter la profondeur d'analyse selon les préférences

2. **Hiérarchisation du contenu** :
   - Messages clés adaptés à l'audience
   - Informations de support contextuel
   - Détails techniques selon le niveau requis
   - Exemples et cas d'usage pertinents

### Adaptation du Niveau de Détail
1. **Pour audience C-Level** :
   - Focus sur impact business et ROI
   - Synthèse des enjeux stratégiques
   - Recommandations exécutives
   - Métriques de performance clés

2. **Pour audience Technique** :
   - Détails d'implémentation et spécifications
   - Comparaisons techniques et benchmarks
   - Aspects architecturaux et sécurité
   - Considérations de performance

3. **Pour audience Formation** :
   - Concepts expliqués progressivement
   - Exemples pratiques et démonstrations
   - Guides étape par étape
   - Ressources d'apprentissage complémentaires

### Restructuration Narrative
1. **Adapter la séquence logique** :
   - Organiser selon la progression optimale pour l'audience
   - Créer des transitions fluides
   - Intégrer les éléments d'engagement recommandés

2. **Optimiser pour la durée d'attention** :
   - Découper en segments adaptés
   - Placer les points clés aux moments optimaux
   - Intégrer les points d'interaction suggérés

## Phase 4: Génération du Rapport Adapté

### Structure du Rapport Personnalisé
```markdown
# Rapport Adapté : [Sujet] pour [Audience Spécifique]

## Synthèse Exécutive Personnalisée

### Pour Cette Audience
- **Pourquoi c'est important** : [Pertinence spécifique]
- **Impact attendu** : [Bénéfices adaptés]
- **Actions recommandées** : [Prochaines étapes appropriées]

### Messages Clés Adaptés
1. [Message principal adapté au niveau et intérêts]
2. [Message de support avec preuves pertinentes]
3. [Message d'action avec call-to-action approprié]

## Contenu Principal Personnalisé

### Contexte et Enjeux
- [Définitions adaptées au niveau d'expertise]
- [Contexte d'application spécifique à l'audience]
- [Enjeux prioritaires pour ce profil]

### Information Clé par Section

#### [Section 1 - Adaptée]
- **Pour cette audience** : [Pourquoi c'est pertinent]
- **Niveau de détail** : [Adapté aux préférences]
- **Points d'emphasis** : [Éléments à souligner]
- **Données de support** : [Statistiques et exemples appropriés]

#### [Section 2 - Adaptée]
- [Même structure adaptée]

### Études de Cas Sélectionnées
- [Cas d'usage pertinents pour l'audience]
- [Exemples avec niveau de détail approprié]
- [Témoignages et retours d'expérience ciblés]

## Recommandations de Présentation

### Structure Suggérée
1. **Ouverture** : [Type d'accroche adapté]
2. **Développement** : [Séquence optimisée pour l'audience]
3. **Conclusion** : [Call-to-action approprié]

### Éléments Visuels Recommandés
- [Types de graphiques adaptés]
- [Données à visualiser selon les préférences]
- [Niveau de complexité graphique optimal]

### Timing et Rythme
- **Durée recommandée** : [Selon guide d'audience]
- **Points de pause** : [Moments d'interaction optimaux]
- **Répartition du temps** : [Par section selon attention]

## Adaptation Linguistique

### Vocabulaire et Ton
- **Registre** : [Adapté au profil audience]
- **Termes techniques** : [Niveau d'expertise approprié]
- **Style narratif** : [Selon préférences communication]

### Messages à Éviter
- [Pièges spécifiques à cette audience]
- [Sujets potentiellement problématiques]
- [Erreurs de communication typiques]

## Données de Support Priorisées

### Statistiques Clés
- [Chiffres les plus impactants pour l'audience]
- [Métriques prioritaires selon le profil]
- [Comparaisons et benchmarks pertinents]

### Références et Sources
- [Sources adaptées à la crédibilité requise]
- [Types de validation importants pour l'audience]
- [Références d'autorité reconnues par le profil]

## Plan d'Action Personnalisé

### Pour l'Audience
- [Actions spécifiques recommandées]
- [Prochaines étapes adaptées au rôle]
- [Ressources complémentaires appropriées]

### Pour la Présentation
- [Ajustements recommandés au format]
- [Éléments d'interaction à intégrer]
- [Métriques de succès spécifiques]

## Annexes Adaptées

### Glossaire Ciblé
- [Termes importants avec définitions adaptées]

### Ressources Complémentaires
- [Documents de référence pertinents]
- [Liens et lectures recommandées]

---

*Rapport généré automatiquement par adaptation intelligente*
*Basé sur : [sources-recherche] + [guide-audience]*
*Optimisé pour : [caractéristiques-audience]*
```

## Phase 5: Validation et Optimisation

### Contrôle Qualité
1. **Cohérence avec le guide d'audience** :
   - Vérifier respect des recommandations de communication
   - Confirmer adaptation du niveau de détail
   - Valider l'usage du vocabulaire approprié

2. **Complétude de l'adaptation** :
   - Tous les éléments de recherche pertinents sont inclus
   - Le contenu est réorganisé de manière optimale
   - Les recommandations spécifiques sont intégrées

3. **Pertinence du contenu** :
   - Information adaptée aux besoins informationnels
   - Exemples et cas d'usage appropriés
   - Niveau de complexité optimal

### Optimisation Finale
1. **Fluidité narrative** :
   - Transitions logiques et naturelles
   - Progression adaptée à l'audience
   - Rythme optimal selon les préférences

2. **Actionabilité** :
   - Recommandations concrètes et spécifiques
   - Plan d'action clair et réalisable
   - Métriques de succès définies

## Phase 6: Production et Livraison

### Génération du Fichier
1. **Nom et emplacement** :
   - Nom : `content-brief-adapted-[date].md`
   - Emplacement : `[chemin-audience]/content-brief-adapted-[date].md`

2. **Mise à jour du contexte** :
   - Créer ou mettre à jour `content-brief.md` principal
   - Documenter les sources et méthode d'adaptation utilisées
   - Logger dans `documentation/research_log.md` si existant

### Rapport de Mission
```
✅ Adaptation de contenu complétée avec succès !

📁 Fichier généré : [chemin-complet]
🎯 Audience optimisée : [profil-audience]
📊 Sources adaptées :
- Recherche documentaire : [fichiers-utilisés]
- Guide d'audience : [guide-référence]
- Adaptation intelligente : [méthodes-appliquées]

📋 Adaptations réalisées :
- Niveau de détail ajusté selon expertise
- Vocabulaire adapté au profil
- Structure optimisée pour attention
- Messages clés personnalisés
- Exemples filtrés par pertinence

🎯 Optimisé pour :
- Durée d'attention : [estimation]
- Niveau technique : [adapté]
- Style communication : [personnalisé]
- Format présentation : [recommandations-intégrées]

📈 Qualité d'adaptation : [Élevée/Très élevée]
🔄 Dernière mise à jour : [date]

💡 Utilisation recommandée :
- Base de travail pour création de slides
- Référence pour adaptation du contenu
- Guide pour structuration de la présentation
- Support pour préparation de la narration
```

## Utilisation

```bash
# Adaptation avec chemins complets
/adapt-content-for-audience "tests/ia-generative-integration/technique" "docs/audience/technique.md"

# Adaptation pour présentation C-Level
/adapt-content-for-audience "presentations/innovation-digitale/c-level" "docs/audience/c-level.md"

# Adaptation pour individu spécifique
/adapt-content-for-audience "presentations/hygiene-mains/andre-malenfant" "docs/audience/individuals/andre-m-malenfant-mala3.md"
```

## Avantages

- **Adaptation intelligente** : Combine recherche documentaire et profil d'audience
- **Génération automatique** : Crée les prérequis manquants automatiquement
- **Personnalisation avancée** : Niveau de détail et style adaptés précisément
- **Optimisation engagement** : Basé sur les préférences et attention de l'audience
- **Intégration workflow** : S'intègre parfaitement dans le processus de création
- **Qualité professionnelle** : Rapport de niveau consulting adapté pour Premier Tech
- **Réutilisabilité** : Base solide pour création de multiples présentations
- **Traçabilité complète** : Documentation des sources et méthodes d'adaptation