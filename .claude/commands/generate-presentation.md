---
description: "Génère la présentation PowerPoint finale avec validation automatique de conformité"
argument-hint: "chemin/vers/config.json [options]"
allowed-tools: ["Read", "Bash", "Glob", "Grep"]
---

# Generate Presentation

Génère la présentation PowerPoint finale en utilisant `tools/presentation_builder.py` à partir du fichier config.json, puis exécute automatiquement `tools/validation_checker.py` sur chaque slide pour s'assurer de la conformité aux standards Premier Tech. Cette commande représente l'étape finale du workflow de création de présentation.

## Instructions

Tu dois générer la présentation finale et valider automatiquement chaque slide pour garantir la qualité et la conformité.

### Phase 1: Préparation et Validation des Prérequis

1. **Localiser le fichier de configuration** :
   - Si $ARGUMENTS contient un chemin spécifique vers config.json, l'utiliser
   - Sinon, chercher config.json dans le répertoire courant ou ses sous-dossiers
   - Privilégier les fichiers les plus récents si plusieurs sont trouvés

2. **Valider la configuration** :
   - Lire et parser le fichier config.json
   - Vérifier la syntaxe JSON valide
   - Contrôler la présence des champs obligatoires :
     - `presentation_name`
     - `subject`
     - `audience`
     - `slides` (array non vide)
     - `output_path`

3. **Analyser le contexte de génération** :
   - **Nombre de slides** : Compter les slides dans la configuration
   - **Layouts utilisés** : Identifier les layout_name spécifiés
   - **Chemin de sortie** : Normaliser le output_path selon la configuration
   - **Mode** : Détecter si c'est un test ou une présentation production

### Phase 2: Génération de la Présentation

1. **Exécuter presentation_builder.py** :
   ```bash
   python tools/presentation_builder.py [chemin-config.json]
   ```

2. **Surveiller l'exécution** :
   - Capturer la sortie complète du script
   - Vérifier que la génération s'est terminée sans erreur
   - Identifier le fichier PowerPoint généré
   - Noter le temps de génération et les performances

3. **Contrôler le résultat** :
   - Vérifier l'existence du fichier .pptx généré
   - Contrôler la taille du fichier (doit être > 0)
   - Valider l'accessibilité du fichier

### Phase 3: Validation Automatique Complète

1. **Préparer la validation** :
   - Extraire le chemin d'audience depuis la configuration
   - Compter le nombre total de slides générées
   - Préparer la liste des slides à valider (1 à N)

2. **Exécuter validation_checker.py pour chaque slide** :
   ```bash
   # Pour chaque slide de 1 à N
   python tools/validation_checker.py "[chemin-audience]" [slide_number]
   ```

3. **Collecter les résultats de validation** :
   - Capturer la sortie de validation pour chaque slide
   - Identifier les écarts de conformité détectés
   - Compiler les statistiques de validation
   - Détecter les slides avec des problèmes

### Phase 4: Analyse des Résultats de Validation

1. **Traiter les résultats par slide** :
   - **Slide conforme** : Aucun écart détecté, standards respectés
   - **Slide avec avertissements** : Écarts mineurs, fonctionnalité préservée
   - **Slide non conforme** : Écarts critiques, standards violés

2. **Générer les statistiques globales** :
   - Nombre total de slides validées
   - Pourcentage de conformité globale
   - Nombre d'écarts par catégorie (critique, majeur, mineur)
   - Score de qualité Premier Tech

3. **Identifier les problèmes récurrents** :
   - Patterns d'écarts communs
   - Layouts problématiques
   - Types de non-conformité fréquents

### Phase 5: Rapport de Génération et Qualité

Produire un rapport complet avec cette structure :

```
🎊 Présentation Générée avec Succès !

📁 Fichier généré : [chemin-complet.pptx]
🎯 Présentation : [nom-presentation]
👥 Audience : [audience-cible]
📊 Slides : [nombre] slides générées

⚡ Performance de Génération
- Temps de génération : [X.X]s
- Vitesse moyenne : [X.X]s par slide
- Taille du fichier : [X.X] MB

✅ Validation Automatique Complète

📋 Résultats par Slide :
Slide 1 ([layout-name]) : ✅ Conforme
Slide 2 ([layout-name]) : ⚠️  Avertissement mineur
Slide 3 ([layout-name]) : ❌ Non conforme - [détails]
[...pour chaque slide]

📊 Statistiques de Conformité :
- Slides conformes : [X]/[Total] ([XX]%)
- Avertissements : [X] slides
- Non conformités : [X] slides
- Score qualité PT : [XX]/100

🎯 Standards Premier Tech :
✅ Polices conformes : [XX]% des shapes
✅ Couleurs conformes : [XX]% des shapes
✅ Marges conformes : [XX]% des shapes
✅ Alignements conformes : [XX]% des shapes

⚠️  Problèmes Détectés :
[Si des problèmes existent]
- Slide [X] : [Description du problème]
- Slide [Y] : [Description du problème]

💡 Recommandations :
[Si des améliorations sont suggérées]
- [Action recommandée 1]
- [Action recommandée 2]

🎊 Présentation prête pour diffusion !
Qualité : [Excellente/Bonne/À améliorer]
Conformité Premier Tech : [XX]%

📈 Prochaines étapes suggérées :
- Test de narration avec ElevenLabs
- Révision finale du contenu
- Préparation de la diffusion
```

### Phase 6: Actions Post-Génération

1. **Si validation parfaite (100% conforme)** :
   - Confirmer que la présentation est prête pour diffusion
   - Suggérer le test de narration avec ElevenLabs
   - Proposer la finalisation du workflow

2. **Si avertissements mineurs** :
   - Lister les améliorations optionnelles
   - Confirmer que la présentation est utilisable
   - Documenter les points d'attention

3. **Si problèmes critiques** :
   - Identifier les slides nécessitant correction
   - Proposer les commandes pour corriger (/add-slide, édition config)
   - Recommander une nouvelle génération après correction

### Phase 7: Documentation et Archivage

1. **Mettre à jour les fichiers de documentation** :
   - Ajouter un entry dans README.md du projet si existant
   - Logger la génération dans un fichier de suivi
   - Documenter les performances et la qualité

2. **Archiver les résultats de validation** :
   - Sauvegarder le rapport de validation
   - Conserver les logs de génération
   - Maintenir l'historique des versions

## Comportements Intelligents

### Détection Automatique de Problèmes
- **Analyse des patterns** : Identifier les erreurs récurrentes
- **Suggestions proactives** : Proposer des corrections spécifiques
- **Optimisations** : Recommander des améliorations de performance

### Adaptation Contextuelle
- **Mode test vs production** : Ajuster les critères de validation
- **Type d'audience** : Personnaliser les recommandations
- **Complexité de présentation** : Adapter les seuils de qualité

### Intégration Workflow
- **Feedback automatique** : Informer sur la qualité avant diffusion
- **Préparation ElevenLabs** : Optimiser pour la synthèse vocale
- **Standards Premier Tech** : Garantir la conformité corporate

## Exemples d'Usage

```bash
# Génération avec config spécifique
/generate-presentation "presentations/innovation/c-level/config.json"

# Génération depuis répertoire courant
/generate-presentation

# Génération avec validation détaillée
/generate-presentation "tests/demo/technique/config.json"
```

## Critères de Validation Premier Tech

### Standards Automatiquement Vérifiés
- **Polices** : Premier Tech Text, Premier Tech Title, Premier Tech Title Bold
- **Couleurs** : #FFFFFF, #41B6E6, #BDBDBD, palette corporate
- **Tailles** : 18.0 à 66.0 points selon le contexte
- **Marges** : 3.6, 5.67, 7.2, 8.5 points selon layout
- **Alignements** : LEFT, CENTER, RIGHT selon guidelines

### Métriques de Qualité
- **Conformité > 95%** : Excellente qualité, prêt pour diffusion
- **Conformité 85-95%** : Bonne qualité, vérifications mineures
- **Conformité < 85%** : Améliorations nécessaires avant diffusion

Cette commande peut être utilisée de manière autonome et représente l'aboutissement du workflow de création de présentation avec garantie de qualité Premier Tech.