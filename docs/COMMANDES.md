# 📋 Référence Commandes - Scripts Presentation Builder

## 🎯 Architecture des Scripts

### **Règle Fondamentale**
- **Script 01** : SEUL autorisé à créer une nouvelle présentation
- **Scripts 02-10** : Insertion UNIQUEMENT dans présentations existantes via `--insert-into`

### **Workflow Obligatoire**
```bash
# 1. Créer d'abord la base
python presentation_builder/01_slide_title_creator.py "Titre"

# 2. Puis ajouter selon besoins
python presentation_builder/[02-10]_*.py --insert-into "titre.pptx" [PARAMS]
```

---

## 📖 **Scripts Détaillés**

### **Script 01 - Slide Title Creator** *(Création de base)*
```bash
# Usage de base
python presentation_builder/01_slide_title_creator.py "Mon Titre"

# Avec métadonnées complètes
python presentation_builder/01_slide_title_creator.py "Transformation Numérique" \
  --subtitle "Stratégie 2024-2026" \
  --metadata "2024.01.15 – Équipe Innovation" \
  --project "transformation_2024"

# Paramètres disponibles
--subtitle "Sous-titre"          # Contexte additionnel
--metadata "Date – Auteur"       # Métadonnées de présentation
--project "nom_projet"           # Organisation des fichiers
--output "chemin/specifique"     # Chemin de sortie personnalisé
--no-widen                       # Désactiver élargissement auto texte
--validate                       # Validation template seulement

# Note : Utilise automatiquement la slide 11 du template Premier Tech
```

### **Script 02 - Navigation Builder** *(Table des matières)*
```bash
# Navigation simple
python presentation_builder/02_navigation_builder.py \
  --insert-into "presentation.pptx" \
  --sections "Introduction" "Analyse" "Solutions" "Conclusion"

# Navigation avec sous-sections
python presentation_builder/02_navigation_builder.py \
  --insert-into "presentation.pptx" \
  --sections "Context" "Stratégie" "Implémentation" "ROI" "Next Steps"

# Paramètres disponibles
--sections "Sect1" "Sect2" ...   # Liste des sections (max 5 recommandé)
--title "Table des Matières"     # Titre personnalisé (optionnel)
```

### **Script 03 - Section Header Builder** *(Titres de sections)*
```bash
# Styles disponibles
python presentation_builder/03_section_header_builder.py "Introduction" \
  --insert-into "presentation.pptx" --style major      # Slide 15 (bleu)

python presentation_builder/03_section_header_builder.py "Analyse Détaillée" \
  --insert-into "presentation.pptx" --style moderate   # Slide 16 (blanc)

python presentation_builder/03_section_header_builder.py "2. Stratégie" \
  --insert-into "presentation.pptx" --style numbered   # Slide 14 (avec chiffre)

# Paramètres
--style [major|moderate|numbered] # Style de section
```

### **Script 04 - Simple Message Builder** *(Messages impactants)*
```bash
# Message centré simple
python presentation_builder/04_simple_message_builder.py \
  "Innovation continues to drive our success" \
  --insert-into "presentation.pptx" --style centered

# Message avec image
python presentation_builder/04_simple_message_builder.py \
  "Notre mission : Excellence opérationnelle" \
  --insert-into "presentation.pptx" --style illustrated

# Message avec mots-clés
python presentation_builder/04_simple_message_builder.py \
  "Transformation numérique globale" \
  --insert-into "presentation.pptx" --style keyword_simple \
  --keywords "Digital" "Innovation" "Agile"

# Styles disponibles
--style [centered|illustrated|keyword_simple] # Variantes message
--keywords "Mot1" "Mot2" "Mot3"               # Pour style keyword_simple
```

### **Script 05 - Statistics Builder** *(2-4 statistiques)*
```bash
# 2 statistiques avec ligne bleue
python presentation_builder/05_statistics_builder.py \
  "85%" "Satisfaction Client" "92%" "Rétention Équipes" \
  --insert-into "presentation.pptx" --style blue_line

# 2 statistiques avec ligne grise
python presentation_builder/05_statistics_builder.py \
  "125%" "ROI Année 1" "78%" "Adoption Utilisateurs" \
  --insert-into "presentation.pptx" --style grey_line

# 3 statistiques
python presentation_builder/05_statistics_builder.py \
  "85%" "Satisfaction" "92%" "Rétention" "78%" "Adoption" \
  --insert-into "presentation.pptx" --style three_stats

# 4 statistiques
python presentation_builder/05_statistics_builder.py \
  "85%" "Satisfaction" "92%" "Rétention" "78%" "Adoption" "95%" "Qualité" \
  --insert-into "presentation.pptx" --style four_stats

# 4 statistiques avec lignes
python presentation_builder/05_statistics_builder.py \
  "85%" "Satisfaction" "92%" "Rétention" "78%" "Adoption" "95%" "Qualité" \
  --insert-into "presentation.pptx" --style four_stats_lines

# Paramètres
VALUE1 LABEL1 VALUE2 LABEL2 [VALUE3 LABEL3] [VALUE4 LABEL4]  # 2-4 statistiques
--style [blue_line|grey_line|three_stats|four_stats|four_stats_lines]
--title "Titre personnalisé"        # Titre optionnel
--position POSITION                  # Position d'insertion
```

### **Script 06 - Content Boxes Builder** *(3 ou 4 concepts)*
```bash
# 3 boîtes simples
python presentation_builder/06_content_boxes_builder.py \
  --insert-into "presentation.pptx" \
  "Excellence Opérationnelle" "Innovation Continue" "Satisfaction Client"

# Avec sous-titres
python presentation_builder/06_content_boxes_builder.py \
  --insert-into "presentation.pptx" \
  "Pilier 1" "Pilier 2" "Pilier 3" \
  --subtitle1 "Processus optimisés" --subtitle2 "R&D avancée" --subtitle3 "Écoute active"

# 4 boîtes avec concept4
python presentation_builder/06_content_boxes_builder.py \
  --insert-into "presentation.pptx" \
  "Concept1" "Concept2" "Concept3" --concept4 "Concept4"

# Paramètres
CONCEPT1 CONCEPT2 CONCEPT3               # 3 concepts requis (positionnels)
--concept4 "CONCEPT4"                    # 4ème concept (pour styles 4 boîtes)
--subtitle1/2/3/4 "Description"          # Descriptions individuelles (optionnel)
--style [grey_3_detailed|grey_3_simple|blue_3_detailed|blue_3_simple|grey_4_detailed|grey_4_simple|blue_4_detailed|blue_4_simple]
```

### **Script 07 - Detailed Explanation Builder** *(Explications détaillées)*
```bash
# Explication avec 4 points clés
python presentation_builder/07_detailed_explanation_builder.py \
  --insert-into "presentation.pptx" \
  --style "four_points" \
  --title "Architecture Microservices" \
  "Architecture scalable moderne pour applications d'entreprise" \
  --additional "Sécurité renforcée" "Performance optimisée" "Monitoring temps réel"

# Comparaison détaillée avec ligne bleue
python presentation_builder/07_detailed_explanation_builder.py \
  --insert-into "presentation.pptx" \
  --style "dual_detailed_blue" \
  --title "Avant vs Après" \
  --subtitle "Transformation numérique complète" \
  "Architecture legacy" \
  --additional "Architecture cloud-native"

# Paramètres
CONTENU_PRINCIPAL                    # Contenu principal de l'explication
--style [four_points|dual_detailed_blue|dual_detailed_grey|dual_titled_blue|dual_titled_grey|dual_lists_blue|dual_lists_grey]
--title "TITRE"                      # Titre de la slide
--subtitle "SOUS_TITRE"              # Sous-titre (pour styles dual_detailed_*)
--additional "POINT1" "POINT2" ...   # Contenu additionnel selon le style
```

**Styles disponibles:**
- `four_points` : 4 énoncés avec mots-clés (slide 35)
- `dual_detailed_blue` : 2 énoncés avec sous-titres et ligne bleue (slide 39)
- `dual_detailed_grey` : 2 énoncés avec sous-titres et ligne grise (slide 40)
- `dual_titled_blue` : 2 énoncés avec titre et ligne bleue (slide 41)
- `dual_titled_grey` : 2 énoncés avec titre et ligne grise (slide 42)
- `dual_lists_blue` : 2 listes avec sous-titres et ligne bleue (slide 43)
- `dual_lists_grey` : 2 listes avec sous-titres et ligne grise (slide 44)

### **Script 08 - Testimonial Builder** *(Témoignages)*
```bash
# Témoignage simple
python presentation_builder/08_testimonial_builder.py \
  "Cette solution a transformé notre productivité" "Marie Dupont" \
  --insert-into "presentation.pptx"

# Témoignage complet avec attribution
python presentation_builder/08_testimonial_builder.py \
  "L'implémentation s'est déroulée parfaitement" "Jean Martin" \
  --insert-into "presentation.pptx" \
  --position "Directeur IT" --company "TechCorp Inc." \
  --testimonial-title "Retour d'Expérience Client"

# Paramètres
"CITATION" "AUTEUR"               # Témoignage et auteur requis
--position "Poste"                # Fonction de l'auteur
--company "Entreprise"            # Organisation
--testimonial-title "Titre"      # Titre du témoignage
```

### **Script 09 - Charts Builder** *(Graphiques enhanced)*
```bash
# Import depuis CSV simple (2 colonnes: Label, Valeur)
python presentation_builder/09_charts_builder.py "Ventes Q4" \
  --insert-into "presentation.pptx" \
  --csv "data/ventes_q4.csv" --style column_clustered

# CSV multi-séries pour comparaisons
python presentation_builder/09_charts_builder.py "Comparaison Régions" \
  --insert-into "presentation.pptx" \
  --csv "data/regions_comparison.csv" --style line_chart

# Configuration JSON complète
python presentation_builder/09_charts_builder.py \
  --insert-into "presentation.pptx" \
  --json-config "charts/config_budget.json"

# Données directes avec insights
python presentation_builder/09_charts_builder.py "Performance KPI" \
  --insert-into "presentation.pptx" --style pie_chart \
  --data-labels "Atteint" "En cours" "Retard" \
  --data-values "65" "25" "10" \
  --insights "65% des objectifs atteints"

# Export de données depuis graphique existant
python presentation_builder/09_charts_builder.py \
  --export-from "presentation.pptx" \
  --export-csv "exported_data.csv" --slide-index -1

# Création d'exemples
python presentation_builder/09_charts_builder.py \
  --create-sample-csv "exemple.csv" # ou --create-sample-json "config.json"

# Styles disponibles
--style [column_clustered|line_chart|pie_chart|bar_clustered|column_compact|bar_compact]
--csv "fichier.csv"                    # Import CSV simple ou multi-séries
--json-config "config.json"           # Configuration complète JSON
--data-labels "Label1" "Label2"       # Labels directs
--data-values "Val1" "Val2"           # Valeurs directes
--insights "Points clés"              # Insights métier
--series-title "Titre série"          # Titre personnalisé série
--export-from "source.pptx"           # Export données existantes
--export-csv "output.csv"             # Fichier export
--slide-index INDEX                   # Index slide à exporter
--position POSITION                   # Position d'insertion
```

### **Script 10 - Conclusion Builder** *(Fermetures PT)*
```bash
# Conclusion corporate standard
python presentation_builder/10_conclusion_builder.py \
  --insert-into "presentation.pptx" --style "passion_tech"

# Message de fermeture personnalisé
python presentation_builder/10_conclusion_builder.py \
  "Ensemble, construisons l'avenir numérique" \
  --insert-into "presentation.pptx" --style "custom_conclusion" \
  --call-to-action "Démarrons ce projet ensemble"

# Styles disponibles
--style [passion_tech|we_are_pt|custom_conclusion|monogram]  # Variantes de conclusion
--call-to-action "Message"                                   # Pour style custom_conclusion
```

---

## 🔧 **Commandes Utiles**

### **Validation et Aide**
```bash
# Valider un script
python presentation_builder/[SCRIPT].py --validate

# Aide détaillée
python presentation_builder/[SCRIPT].py --help

# Lister les styles (pour scripts avec styles)
python presentation_builder/05_statistics_builder.py --list-styles
python presentation_builder/09_charts_builder.py --list-styles

# Options communes disponibles dans plusieurs scripts
--no-widen                    # Désactiver élargissement auto objets texte
--template "chemin/custom"    # Template personnalisé (optionnel)
--position INDEX             # Position d'insertion spécifique
```

### **Gestion des Fichiers**
```bash
# Les fichiers sont générés automatiquement à partir du titre
# Format : titre_en_snake_case.pptx

# Exemple : "Mon Titre" → "mon_titre.pptx"
```

---

## 📊 **Guide Spécialisé - Script 09 Charts Builder**

### **Formats CSV Supportés**

#### **CSV Simple (2 colonnes: Label, Valeur)**
```csv
Catégorie,Valeur
T1,2500000
T2,3200000
T3,2800000
T4,3700000
```

#### **CSV Multi-séries (comparaisons)**
```csv
Trimestre,Europe,Amérique,Asie
T1,1200000,800000,500000
T2,1500000,1000000,700000
T3,1300000,900000,600000
T4,1800000,1200000,700000
```

### **Configuration JSON**
```json
{
  "title": "Titre du graphique",
  "style": "column_clustered",
  "data": {
    "labels": ["T1", "T2", "T3", "T4"],
    "values": [2500000, 3200000, 2800000, 3700000]
  },
  "insights": "Croissance continue avec pic en T4"
}
```

### **Fichiers d'exemples disponibles**
```bash
# Dans data/charts/ (créés automatiquement)
--create-sample-csv "ventes_exemple.csv"        # CSV simple
--create-sample-json "config_exemple.json"      # Configuration JSON

# Exemples fournis
data/charts/ventes_trimestrielles.csv          # Ventes sur 8 trimestres
data/charts/regions_comparison.csv             # Comparaison multi-régions
data/charts/budget_repartition.csv             # Répartition budgétaire
data/charts/kpi_performance.csv                # Performance KPIs
```

---

## ⚠️ **Erreurs Communes et Solutions**

### **Script 01 - Title Creator**
```bash
# ❌ ERREUR : Essayer d'insérer dans une présentation existante
python 01_slide_title_creator.py "Titre" --insert-into presentation.pptx

# ✅ CORRECT : Script 01 crée TOUJOURS une nouvelle présentation
python 01_slide_title_creator.py "Titre"
```

### **Scripts 02-10 - Insertion**
```bash
# ❌ ERREUR : Oublier --insert-into
python 02_navigation_builder.py --sections "A" "B" "C"

# ✅ CORRECT : Toujours spécifier la présentation cible
python 02_navigation_builder.py --insert-into presentation.pptx --sections "A" "B" "C"
```

### **Script 09 - Charts**
```bash
# ❌ ERREUR : Mauvais format CSV
# Fichier avec entêtes différents ou séparateurs incorrects

# ✅ CORRECT : Vérifier le format avec un exemple
python 09_charts_builder.py --create-sample-csv "test.csv"
```

---

## 🚀 **Workflow Optimisé Typique**

```bash
# 1. Créer la base
python 01_slide_title_creator.py "Transformation Numérique 2024" \
  --subtitle "Stratégie d'Innovation" \
  --metadata "2024.01.15 – Équipe Digital"

# 2. Ajouter navigation
python 02_navigation_builder.py --insert-into transformation_numerique_2024.pptx \
  --sections "Contexte" "Vision" "Roadmap" "Budget" "Next Steps"

# 3. Sections et contenu
python 03_section_header_builder.py "1. Contexte Marché" \
  --insert-into transformation_numerique_2024.pptx --style numbered

python 06_content_boxes_builder.py --insert-into transformation_numerique_2024.pptx \
  "Innovation" "Efficiency" "Growth" \
  --subtitles "R&D 25%" "Process +30%" "Revenue +15%"

# 4. Statistiques et graphiques
python 05_statistics_builder.py \
  "85%" "Adoption Rate" "127M$" "Expected ROI" \
  --insert-into transformation_numerique_2024.pptx --style blue_line

python 09_charts_builder.py "Budget Allocation" \
  --insert-into transformation_numerique_2024.pptx \
  --csv data/budget_2024.csv --style pie_chart \
  --insights "R&D représente 35% du budget total"

# 5. Conclusion
python 10_conclusion_builder.py \
  --insert-into transformation_numerique_2024.pptx --style passion_tech
```