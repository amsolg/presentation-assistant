# Guide de Gestion Dynamique de Taille de Texte - Presentation Assistant

## Vue d'Ensemble

Ce guide détaille l'approche standardisée pour la gestion dynamique de la taille de police dans tous les scripts de `presentation_builder`, basée sur l'implémentation du `testimonial_builder.py` et analysée dans l'ensemble du codebase.

## Architecture et Principes Fondamentaux

### 1. Principe Central : Mapping Inverse Déterministe

L'approche repose sur une relation **inverse et déterministe** entre la longueur du contenu et la taille de police :

```
Plus le texte est long → Plus la police doit être petite
Même longueur = même taille, toujours
```

### 2. Choix Architecturaux Critiques

- **Paramètre de mesure** : `len(text)` (caractères, pas mots)
- **Retour standardisé** : `int` (points de police PowerPoint)
- **Méthode** : Intervalles discrets plutôt que formules continues
- **Structure** : `if/elif` en cascade pour lisibilité et maintenabilité

## Table de Mapping Universelle

### 3.1 Intervalles Standards

```python
def _calculate_optimal_font_size(self, shape, text_content: str, available_height=None) -> int:
    """
    Calcule la taille de police optimale selon la longueur du texte.

    Args:
        shape: Shape PowerPoint contenant le texte
        text_content: Contenu textuel à mesurer
        available_height: Hauteur disponible (optionnel)

    Returns:
        int: Taille de police optimale en points
    """
    try:
        text_length = len(text_content)

        # === INTERVALLES UNIVERSELS ===
        # Textes courts (0-500 chars) - Dégressivité forte
        if text_length < 100:       # [0, 99]
            optimal_size = 40
        elif text_length <= 200:    # [100, 200]
            optimal_size = 32
        elif text_length <= 300:    # [201, 300]
            optimal_size = 24
        elif text_length <= 500:    # [301, 500]
            optimal_size = 20

        # Textes moyens (500-2000 chars) - Dégressivité modérée
        elif text_length <= 700:    # [501, 700]
            optimal_size = 16
        elif text_length <= 1000:   # [701, 1000]
            optimal_size = 14
        elif text_length <= 1300:   # [1001, 1300]
            optimal_size = 12

        # Textes longs (1300+ chars) - Dégressivité fine
        elif text_length <= 1700:   # [1301, 1700]
            optimal_size = 11
        elif text_length <= 2100:   # [1701, 2100]
            optimal_size = 10
        elif text_length <= 2500:   # [2101, 2500]
            optimal_size = 9
        elif text_length <= 3300:   # [2501, 3300]
            optimal_size = 8
        elif text_length <= 4000:   # [3301, 4000]
            optimal_size = 7
        else:                       # [4001+]
            optimal_size = 7        # Taille minimale
            print(f"[WARNING] Texte extrêmement long ({text_length} caractères)")

        print(f"[FONT] Texte {text_length} caractères -> Police {optimal_size}pt (intervalle basé)")
        return optimal_size

    except Exception as e:
        print(f"[WARNING] Erreur calcul taille police: {e}")
        return 12  # Fallback sécurisé
```

### 3.2 Rationale Mathématique

| Longueur | Police | Réduction | Usage Typique |
|----------|---------|-----------|---------------|
| 0-99     | 40pt    | -         | Titres courts, mots-clés |
| 100-200  | 32pt    | -20%      | Citations courtes, énoncés |
| 201-300  | 24pt    | -25%      | Paragraphes courts |
| 301-500  | 20pt    | -17%      | Explications moyennes |
| 501-700  | 16pt    | -20%      | Contenus détaillés |
| 701-1000 | 14pt    | -12%      | Textes longs |
| 1000+    | ≤12pt   | Fine      | Documents, listes |

## Implémentation par Type de Contenu

### 4.1 Citations et Témoignages (testimonial_builder)

**Contexte** : Textes variables de 50 à 4000+ caractères
**Implémentation** : Table complète avec gestion des cas limites

```python
def _calculate_optimal_font_size(self, shape, quote_text: str, available_height) -> int:
    # Implémentation complète selon table universelle
    # + Gestion warning pour textes > 4000 caractères
    # + Logging détaillé pour diagnostic
```

### 4.2 Messages Simples (simple_message_builder)

**Contexte** : Messages courts à moyens (10-500 caractères)
**Adaptation recommandée** : Intervalles simplifiés

```python
def _calculate_optimal_font_size(self, shape, message_text: str) -> int:
    text_length = len(message_text)

    # Version simplifiée pour messages courts
    if text_length < 50:
        return 36      # Messages très courts
    elif text_length <= 100:
        return 28      # Messages courts
    elif text_length <= 200:
        return 24      # Messages moyens
    elif text_length <= 500:
        return 20      # Messages longs
    else:
        return 16      # Messages très longs
```

### 4.3 Statistiques et Données (statistics_builder)

**Contexte** : Valeurs numériques et labels courts
**Adaptation recommandée** : Intervalles spécialisés

```python
def _calculate_optimal_font_size_for_stats(self, text_content: str, content_type: str) -> int:
    text_length = len(text_content)

    if content_type == "value":
        # Valeurs numériques - tailles plus grandes
        if text_length <= 5:        # "100%", "1.2M"
            return 32
        elif text_length <= 10:     # "€1,250,000"
            return 28
        else:
            return 24

    elif content_type == "label":
        # Labels descriptifs - tailles moyennes
        if text_length <= 20:       # "Satisfaction Client"
            return 18
        elif text_length <= 40:     # "Années d'Expérience Moyenne"
            return 16
        else:
            return 14
```

### 4.4 Boîtes de Contenu (content_boxes_builder)

**Contexte** : Titres et contenus structurés
**Statut actuel** : Pas d'implémentation dynamique
**Recommandation** : Adapter selon le type de shape

```python
def _calculate_optimal_font_size_for_content_box(self, text_content: str, box_role: str) -> int:
    text_length = len(text_content)

    if box_role == "title":
        # Titres de boîtes - privilégier la lisibilité
        if text_length <= 30:
            return 20
        elif text_length <= 50:
            return 18
        else:
            return 16

    elif box_role == "content":
        # Contenus de boîtes - table universelle adaptée
        if text_length <= 100:
            return 16
        elif text_length <= 200:
            return 14
        elif text_length <= 400:
            return 12
        else:
            return 11
```

### 4.5 Explications Détaillées (detailed_explanation_builder)

**Contexte** : Textes longs et structurés
**Adaptation recommandée** : Focus sur les textes moyens-longs

```python
def _calculate_optimal_font_size_for_explanation(self, text_content: str) -> int:
    text_length = len(text_content)

    # Focus sur la plage 100-1000 caractères pour explications
    if text_length <= 150:
        return 18      # Explications courtes
    elif text_length <= 300:
        return 16      # Explications moyennes
    elif text_length <= 600:
        return 14      # Explications détaillées
    elif text_length <= 1000:
        return 12      # Explications complètes
    else:
        return 11      # Explications très longues
```

## Application Standardisée

### 5.1 Fonction d'Application Universelle

```python
def _apply_font_size_to_shape(self, shape, font_size: int):
    """
    Applique une taille de police à tous les paragraphes d'un shape.
    Méthode universelle pour tous les builders.

    Args:
        shape: Shape PowerPoint à modifier
        font_size: Taille de police en points
    """
    try:
        from pptx.util import Pt

        if not hasattr(shape, 'text_frame') or not shape.text_frame:
            return

        # Appliquer la taille à TOUS les paragraphes et runs
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(font_size)

        print(f"[FONT] Taille {font_size}pt appliquée à {len(shape.text_frame.paragraphs)} paragraphe(s)")

    except Exception as e:
        print(f"[WARNING] Erreur application taille police: {e}")
```

### 5.2 Intégration dans le Workflow

```python
# ORDRE D'OPÉRATIONS CRITIQUE
def _customize_slide_content(self, slide, content_data):
    # 1. Assigner le texte d'abord
    shape.text_frame.text = content_data['text']

    # 2. Configurer word_wrap
    shape.text_frame.word_wrap = content_data.get('word_wrap', True)

    # 3. Calculer et appliquer la taille dynamique
    optimal_font_size = self._calculate_optimal_font_size(shape, content_data['text'])
    self._apply_font_size_to_shape(shape, optimal_font_size)

    # 4. Ajustements géométriques finaux
    if content_data.get('widen_for_long_text') and len(content_data['text']) > 100:
        shape.width = Inches(12)
```

## Patterns d'Adaptation Spécialisée

### 6.1 Classe Générique Réutilisable

```python
class DynamicFontSizer:
    """
    Classe générique pour gestion dynamique de taille de police.
    Réutilisable dans tous les builders.
    """

    def __init__(self, size_intervals: List[Tuple[int, int]]):
        """
        Args:
            size_intervals: [(max_length, font_size), ...]
            Exemple: [(100, 40), (200, 32), (500, 20)]
        """
        self.intervals = sorted(size_intervals)

    def calculate_size(self, text_length: int) -> int:
        """Calcule la taille selon les intervalles définis"""
        for max_length, font_size in self.intervals:
            if text_length <= max_length:
                return font_size
        return self.intervals[-1][1]  # Dernier élément si dépassement

    def apply_to_shape(self, shape, text_content: str):
        """Applique la taille calculée au shape"""
        optimal_size = self.calculate_size(len(text_content))
        self._apply_font_size_to_shape(shape, optimal_size)
```

### 6.2 Usage Spécialisé par Builder

```python
# Dans content_boxes_builder.py
title_sizer = DynamicFontSizer([
    (30, 20),    # Titres courts
    (50, 18),    # Titres moyens
    (100, 16)    # Titres longs
])

content_sizer = DynamicFontSizer([
    (100, 16),   # Contenus courts
    (200, 14),   # Contenus moyens
    (400, 12),   # Contenus longs
    (800, 11)    # Contenus très longs
])

# Dans statistics_builder.py
value_sizer = DynamicFontSizer([
    (5, 32),     # Chiffres simples
    (10, 28),    # Valeurs moyennes
    (20, 24)     # Valeurs complexes
])

label_sizer = DynamicFontSizer([
    (20, 18),    # Labels courts
    (40, 16),    # Labels moyens
    (60, 14)     # Labels longs
])
```

## Gestion des Cas Limites

### 7.1 Validation et Sécurité

```python
def _calculate_optimal_font_size_safe(self, shape, text_content: str, min_size: int = 7, max_size: int = 40) -> int:
    """
    Version sécurisée avec validation des limites.

    Args:
        shape: Shape PowerPoint
        text_content: Contenu textuel
        min_size: Taille minimale autorisée
        max_size: Taille maximale autorisée

    Returns:
        int: Taille de police validée
    """
    try:
        # Validation des entrées
        if not text_content:
            return 12  # Fallback pour texte vide

        if len(text_content) > 10000:
            print(f"[WARNING] Texte exceptionnellement long ({len(text_content)} caractères)")
            return min_size

        # Calcul normal
        calculated_size = self._calculate_optimal_font_size(shape, text_content)

        # Application des limites
        final_size = max(min_size, min(max_size, calculated_size))

        if final_size != calculated_size:
            print(f"[ADJUST] Taille ajustée de {calculated_size}pt à {final_size}pt (limites: {min_size}-{max_size})")

        return final_size

    except Exception as e:
        print(f"[ERROR] Erreur calcul sécurisé: {e}")
        return 12  # Fallback ultime
```

### 7.2 Gestion de l'Espacement

```python
def _validate_text_spacing(self, slide, shapes_to_check: List[int]):
    """
    Valide l'espacement entre les éléments textuels après redimensionnement.

    Args:
        slide: Slide PowerPoint
        shapes_to_check: Indices des shapes à vérifier
    """
    try:
        shapes_list = list(slide.shapes)

        for i in range(len(shapes_to_check) - 1):
            current_idx = shapes_to_check[i]
            next_idx = shapes_to_check[i + 1]

            if current_idx < len(shapes_list) and next_idx < len(shapes_list):
                current_shape = shapes_list[current_idx]
                next_shape = shapes_list[next_idx]

                # Calculer l'espacement
                current_bottom = current_shape.top + current_shape.height
                next_top = next_shape.top
                spacing = next_top - current_bottom

                # Convertir en pouces
                spacing_inches = spacing / 914400  # 914400 EMU = 1 inch

                if spacing_inches < 0.1:  # Minimum 0.1 inch
                    print(f"[WARNING] Espacement insuffisant entre shapes {current_idx} et {next_idx}: {spacing_inches:.3f}\"")
                    print(f"[RECOMMENDATION] Considérer réduire davantage la taille de police")
                else:
                    print(f"[SUCCESS] Espacement suffisant: {spacing_inches:.3f}\"")

    except Exception as e:
        print(f"[WARNING] Erreur validation espacement: {e}")
```

## État d'Implémentation dans le Codebase

### Analyse des Scripts Existants

| Script | Gestion Dynamique | Statut | Recommandation |
|--------|------------------|---------|----------------|
| `testimonial_builder.py` | ✅ Complet | Production | Référence pour les autres |
| `simple_message_builder.py` | ❌ Aucune | À implémenter | Version simplifiée |
| `statistics_builder.py` | ❌ Aucune | À implémenter | Spécialisée valeurs/labels |
| `content_boxes_builder.py` | ❌ Aucune | À implémenter | Différencier titre/contenu |
| `detailed_explanation_builder.py` | ❌ Aucune | À implémenter | Focus textes moyens-longs |
| `charts_builder.py` | ❌ Aucune | À implémenter | Titres et insights seulement |

### Pattern d'Implémentation Recommandé

```python
# 1. Ajouter la fonction de calcul spécialisée
def _calculate_optimal_font_size(self, shape, text_content: str) -> int:
    # Implémentation selon le type de builder

# 2. Ajouter la fonction d'application universelle
def _apply_font_size_to_shape(self, shape, font_size: int):
    # Implémentation universelle

# 3. Intégrer dans les méthodes de personnalisation existantes
def _customize_slide_content(self, slide, content_data):
    # Ordre : texte → word_wrap → taille dynamique → ajustements
```

## Alternatives Évaluées et Rejetées

### 9.1 Formule Mathématique Continue

```python
# REJETÉE : Formule logarithmique
import math
optimal_size = max(7, int(50 - 10 * math.log10(text_length + 1)))

# Problèmes :
# - Résultats imprévisibles
# - Difficile à ajuster
# - Pas de contrôle précis des seuils
```

### 9.2 Lookup Table

```python
# REJETÉE : Dictionnaire de lookup
SIZE_MAPPING = {
    (0, 99): 40,
    (100, 200): 32,
    # ...
}

# Problèmes :
# - Plus complexe à lire
# - Gestion des ranges compliquée
# - Pas plus performant
```

### 9.3 Calcul par Surface

```python
# REJETÉE : Basé sur la surface disponible
def calculate_size_by_area(text_length, available_area):
    chars_per_square_inch = estimate_density(font_family)
    # ...

# Problèmes :
# - Trop complexe
# - Variables inconnues
# - Résultats inconsistants
```

## Avantages de l'Approche Retenue

✅ **Prédictibilité** : Même input → même output, toujours
✅ **Simplicité** : Logique claire, pas de calculs complexes
✅ **Maintenabilité** : Facile de modifier un seuil spécifique
✅ **Testabilité** : Chaque intervalle peut être testé individuellement
✅ **Performance** : O(1) constant, pas de calculs lourds
✅ **Robustesse** : Gestion d'erreur simple avec fallback
✅ **Flexibilité** : Intervalles ajustables selon le contexte

## Validation et Tests

### 10.1 Test Exhaustif des Intervalles

```python
def test_font_sizing_intervals():
    """Test complet de tous les intervalles définis"""
    test_cases = [
        # Limites inférieures
        {"length": 99, "expected": 40},
        {"length": 100, "expected": 32},

        # Limites supérieures
        {"length": 200, "expected": 32},
        {"length": 201, "expected": 24},

        # Milieux d'intervalles
        {"length": 150, "expected": 32},
        {"length": 350, "expected": 20},

        # Cas limites
        {"length": 0, "expected": 40},
        {"length": 5000, "expected": 7}
    ]

    for case in test_cases:
        result = calculate_optimal_font_size(None, "x" * case["length"])
        assert result == case["expected"], f"Échec pour {case['length']} chars: attendu {case['expected']}, reçu {result}"
```

### 10.2 Génération de Contenu Contrôlé

```python
def generate_text_of_exact_length(target_length: int) -> str:
    """
    Générateur pour tester des longueurs précises.
    Critique pour validation des seuils exacts.
    """
    base = "Premier Tech offre des solutions innovantes. "
    repeated = (base * (target_length // len(base) + 1))[:target_length]
    return repeated
```

## Conclusion

Cette approche de gestion dynamique de taille de texte transforme un problème variable (longueur de texte imprévisible) en solution déterministe (mapping fixe longueur → taille), tout en restant simple à comprendre, tester et maintenir.

L'implémentation dans `testimonial_builder.py` sert de référence pour l'adoption progressive dans tous les autres builders, avec des adaptations spécialisées selon le type de contenu géré par chaque script.