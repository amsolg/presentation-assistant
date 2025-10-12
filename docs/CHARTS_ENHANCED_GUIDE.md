# 📊 Guide du Script Charts Builder Enhanced

## 🚀 Vue d'ensemble

Le script `09_charts_builder.py` est une version améliorée du générateur de graphiques qui offre :

- ✅ **Import automatique depuis CSV/Excel**
- ✅ **Support multi-séries** pour comparaisons complexes
- ✅ **Configuration JSON** pour paramètres avancés
- ✅ **Standards visuels Premier Tech** strictement respectés
- ✅ **Validation et enrichissement** automatique des données
- ✅ **Export de données** de graphiques existants

## 📁 Fichiers d'exemples fournis

### CSV d'exemples dans `data/charts/`
- `ventes_trimestrielles.csv` - Données de ventes sur 8 trimestres
- `regions_comparison.csv` - Comparaison multi-régions (4 séries)
- `budget_repartition.csv` - Répartition budgétaire en pourcentages
- `kpi_performance.csv` - Performance des KPIs

### JSON de configuration dans `data/charts/`
- `config_ventes.json` - Configuration pour graphique de ventes
- `config_budget.json` - Configuration pour graphique en secteurs
- `config_regions.json` - Configuration multi-séries régions

## 🎯 Cas d'usage typiques

### 1️⃣ Import simple depuis CSV

```bash
# Graphique en colonnes depuis CSV
python 09_charts_builder.py "Ventes Trimestrielles" \
  --insert-into ma_presentation.pptx \
  --csv ../data/charts/ventes_trimestrielles.csv \
  --style column_clustered
```

### 2️⃣ Graphique en secteurs avec CSV

```bash
# Répartition budgétaire
python 09_charts_builder.py "Budget 2024" \
  --insert-into ma_presentation.pptx \
  --csv ../data/charts/budget_repartition.csv \
  --style pie_chart \
  --insights "R&D représente 35% du budget total"
```

### 3️⃣ Multi-séries depuis CSV

```bash
# Comparaison régionale multi-séries
python 09_charts_builder.py "Performance Régions" \
  --insert-into ma_presentation.pptx \
  --csv ../data/charts/regions_comparison.csv \
  --style line_chart
```

### 4️⃣ Configuration JSON complète

```bash
# Utilisation d'une configuration JSON
python 09_charts_builder.py \
  --insert-into ma_presentation.pptx \
  --json-config ../data/charts/config_budget.json
```

### 5️⃣ Export de données existantes

```bash
# Exporter les données d'un graphique
python 09_charts_builder.py \
  --export-from ma_presentation.pptx \
  --export-csv exported_data.csv \
  --slide-index -1  # Dernière slide
```

## 📈 Formats de données supportés

### Format CSV Simple (2 colonnes)
```csv
Catégorie,Valeur
T1 2024,2500000
T2 2024,3200000
T3 2024,2800000
T4 2024,3700000
```

### Format CSV Multi-séries
```csv
Trimestre,Europe,Amérique,Asie
T1 2024,1.2,0.8,0.5
T2 2024,1.5,1.0,0.7
T3 2024,1.3,0.9,0.6
T4 2024,1.8,1.2,0.7
```

### Format JSON Complet
```json
{
  "title": "Titre du graphique",
  "style": "column_clustered",
  "data": {
    "labels": ["T1", "T2", "T3", "T4"],
    "values": [2.5, 3.2, 2.8, 3.7],
    "series": {
      "Europe": [1.2, 1.5, 1.3, 1.8],
      "Amérique": [0.8, 1.0, 0.9, 1.2]
    }
  },
  "insights": "Points clés à retenir",
  "formatting": {
    "show_legend": true,
    "show_data_labels": true
  }
}
```

## 🎨 Styles de graphiques disponibles

| Style | Type | Usage recommandé |
|-------|------|------------------|
| `column_clustered` | Colonnes groupées | Comparaisons catégorielles |
| `line_chart` | Ligne | Tendances temporelles |
| `pie_chart` | Secteurs | Répartitions/proportions |
| `bar_clustered` | Barres horizontales | Comparaisons horizontales |
| `column_compact` | Colonnes compactes | Visualisations condensées |
| `bar_compact` | Barres compactes | Comparaisons condensées |

## 🏗️ Standards Premier Tech appliqués

### Dimensions standards (pixels)
- **Graphiques colonnes/barres** : 942 × 488
- **Graphiques secteurs** : 701 × 435
- **Graphiques compacts** : 652 × 435

### Palette de couleurs officielles Premier Tech

#### Couleurs principales
- `#41B6E6` (RVB: 65-182-230) - Bleu Premier Tech (Pantone 298) - Accent primaire
- `#FFFFFF` (RVB: 255-255-255) - Blanc - Texte principal
- `#040E1E` (RVB: 4-14-30) - Bleu Noir PPT - Fond

#### Couleurs d'accent secondaires
- `#8A8D8F` (RVB: 138-141-143) - Gris (Pantone 877) - Accent secondaire
- `#0077C8` (RVB: 0-119-200) - Bleu vif (Pantone 3005) - Graphiques additionnels
- `#54585B` (RVB: 84-88-91) - Gris foncé (Pantone 425) - Graphiques additionnels
- `#BDBDBD` (RVB: 189-189-189) - Gris clair (Pantone 877 - 50%) - Graphiques additionnels

### Application des couleurs dans les graphiques

#### Graphiques multi-séries (colonnes, lignes, barres)
Les graphiques utilisent une rotation de couleurs diversifiées pour distinguer facilement les différentes séries de données :
1. Bleu Premier Tech (#41B6E6)
2. Bleu vif (#0077C8)
3. Gris moyen (#8A8D8F)
4. Gris foncé (#54585B)
5. Gris clair (#BDBDBD)
6. Bleu foncé (#003F7F)

#### Graphiques en secteurs (pie charts)
Utilise la palette étendue complète pour maximiser la distinction visuelle entre les secteurs. Les catégories sont automatiquement regroupées si plus de 8 secteurs sont présents.

### Formatage des étiquettes

#### Pie Charts - Prévention de la coupure de mots
- Les étiquettes sont positionnées à l'extérieur des secteurs pour maximiser l'espace
- Le text wrapping est désactivé pour éviter la coupure de mots en plein milieu
- Format d'affichage : Pourcentage + Nom de catégorie

#### Points clés (insights)
- Texte affiché en **blanc** (#FFFFFF) pour une meilleure visibilité sur fond sombre
- Police de 12pt positionnée sous le graphique

## ✨ Fonctionnalités avancées

### Personnalisation des titres de séries
- Utilisez `--series-title` pour personnaliser le nom de la série de données
- Par défaut, le titre est "Valeurs" pour une série unique
- Pour les CSV multi-séries, les titres sont tirés des en-têtes de colonnes

### Validation automatique des données
- Conversion automatique des pourcentages
- Normalisation pour graphiques en secteurs (100%)
- Limitation du nombre de catégories pour la lisibilité
- Gestion des valeurs manquantes

### Enrichissement des données
- Regroupement automatique des petites valeurs ("Autres")
- Ajustement des formats numériques
- Support des devises (€, $)

### Export et réutilisation
- Export CSV des données de graphiques existants
- Réutilisation dans d'autres présentations
- Analyse des données hors PowerPoint

## 🔧 Dépannage

### Erreur "pandas non installé"
```bash
pip install pandas openpyxl
```

### Erreur de format CSV
- Vérifier l'encodage UTF-8
- S'assurer que le séparateur est une virgule
- Vérifier qu'il n'y a pas de lignes vides

### Graphique non visible
- Vérifier que le style correspond au type de données
- S'assurer que les valeurs sont numériques
- Vérifier la position d'insertion

## 📝 Exemples complets

### Présentation financière complète
```bash
# 1. Créer la présentation de base
python 01_slide_title_creator.py "Résultats Financiers 2024"

# 2. Ajouter graphique de ventes
python 09_charts_builder.py "Évolution des Ventes" \
  --insert-into "Résultats Financiers 2024.pptx" \
  --csv ../data/charts/ventes_trimestrielles.csv \
  --style line_chart \
  --position 1

# 3. Ajouter répartition budget
python 09_charts_builder.py "Allocation Budgétaire" \
  --insert-into "Résultats Financiers 2024.pptx" \
  --csv ../data/charts/budget_repartition.csv \
  --style pie_chart \
  --position 2

# 4. Ajouter comparaison régionale
python 09_charts_builder.py "Performance par Région" \
  --insert-into "Résultats Financiers 2024.pptx" \
  --csv ../data/charts/regions_comparison.csv \
  --style column_clustered \
  --position 3
```

## 🚀 Workflow recommandé

1. **Préparer les données** dans Excel/CSV
2. **Valider le format** avec un éditeur de texte
3. **Tester avec données simples** avant multi-séries
4. **Appliquer configuration JSON** pour finition
5. **Exporter si besoin** pour réutilisation

## 📊 Bonnes pratiques

- **Limiter à 8 catégories** pour graphiques en secteurs
- **Maximum 12 catégories** pour barres/colonnes
- **Minimum 3 points** pour graphiques linéaires
- **Utiliser les insights** pour contexte
- **Respecter la palette** de couleurs Premier Tech

## 🆘 Support

Pour toute question ou problème :
1. Vérifier ce guide
2. Consulter les exemples fournis
3. Utiliser `--validate` pour tester le template
4. Utiliser `--list-styles` pour voir les options