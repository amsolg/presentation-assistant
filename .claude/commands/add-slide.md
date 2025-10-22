---
description: "Ajoute ou insère une slide dans une présentation avec personnalisation automatique"
argument-hint: "layout_name position [config_path]"
allowed-tools: ["Read", "Edit", "Bash", "Glob"]
---

# Add Slide

Ajoute ou insère une slide dans un fichier config.json de présentation en utilisant tools/add_slide.py, puis personnalise automatiquement le contenu selon le contexte de la présentation.

## Instructions

Tu dois ajouter une slide à une présentation existante en suivant cette procédure complète :

### Phase 1: Analyse du Contexte
1. **Identifier le fichier de configuration** :
   - Si $ARGUMENTS contient un chemin spécifique vers config.json, l'utiliser
   - Sinon, chercher config.json dans le répertoire courant ou ses sous-dossiers
   - Lire le fichier config.json pour comprendre le contexte de la présentation (sujet, audience, slides existantes)

2. **Analyser la demande d'ajout** :
   - Extraire le layout_name demandé des $ARGUMENTS (ex: "Page titre", "2 statistiques avec ligne bleue")
   - Déterminer la position d'insertion : "fin" ou position numérique spécifique
   - Valider que le layout_name existe dans les templates disponibles

### Phase 2: Mappage Layout vers Slide Number
1. **Rechercher le slide_number correspondant** :
   - Utiliser Glob pour trouver les fichiers dans templates/presentation-project/slide-structure/
   - Lire les fichiers slide_*.json pour trouver celui avec le layout_name demandé
   - Extraire le slide_number (1-57) correspondant au layout souhaité

### Phase 3: Exécution de l'Ajout
1. **Déterminer le mode d'ajout** :
   - Si position = "fin" ou non spécifiée → mode "ajout"
   - Si position numérique → mode "insertion"

2. **Exécuter tools/add_slide.py** :
   ```bash
   # Pour ajout à la fin
   python tools/add_slide.py [config_path] [slide_number] ajout

   # Pour insertion à une position
   python tools/add_slide.py [config_path] [slide_number] insertion [position]
   ```

### Phase 4: Personnalisation Intelligente
1. **Lire le config.json mis à jour** pour identifier la nouvelle slide ajoutée

2. **Personnaliser le contenu selon le contexte** :
   - **Sujet de la présentation** : Adapter les textes au domaine (tech, business, formation)
   - **Audience cible** : Ajuster le vocabulaire et le niveau de détail
   - **Position dans la présentation** : Contextualiser par rapport aux slides précédentes/suivantes
   - **Layout spécifique** : Optimiser selon le type de slide (titre, statistiques, contenu, etc.)

3. **Modifier les shapes de la nouvelle slide** :
   - Remplacer les textes placeholder par du contenu pertinent
   - Ajuster les propriétés visuelles si nécessaire (couleurs, tailles, alignements)
   - Maintenir la conformité aux standards Premier Tech
   - Utiliser Edit ou MultiEdit pour mettre à jour le config.json

### Phase 5: Validation et Rapport
1. **Valider la cohérence** :
   - Vérifier que la slide s'intègre bien dans le flow de la présentation
   - Contrôler le respect des standards Premier Tech (polices, couleurs, marges)
   - S'assurer que les textes sont adaptés à l'audience

2. **Fournir un rapport de synthèse** :
   - Layout ajouté et position finale
   - Personnalisations appliquées
   - Suggestions d'amélioration si pertinentes
   - Prochaines étapes recommandées

## Exemples d'Usage

**Ajouter une slide de titre à la fin :**
```
/add-slide "Page titre" fin
```

**Insérer une slide de statistiques en position 3 :**
```
/add-slide "2 statistiques avec ligne bleue" 3
```

**Ajouter avec chemin spécifique :**
```
/add-slide "3 boîtes bleues pour courts énoncés avec sous-titre" fin presentations/innovation/c-level/config.json
```

## Comportements Intelligents

- **Auto-détection du contexte** : Analyser automatiquement le sujet et l'audience pour personnaliser
- **Cohérence narrative** : Adapter le contenu pour qu'il s'intègre naturellement dans le flow
- **Standards Premier Tech** : Maintenir automatiquement la conformité corporate
- **Optimisation layout** : Tirer parti des spécificités de chaque type de slide
- **Suggestions proactives** : Proposer des améliorations ou compléments pertinents

Cette commande peut être utilisée de manière autonome dans le workflow de création de présentation, permettant d'enrichir dynamiquement le contenu selon les besoins identifiés.