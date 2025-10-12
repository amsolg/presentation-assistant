# ⚡ Démarrage Rapide - Presentation Assistant

## 🎯 Que voulez-vous créer ?

### 🚀 **Workflow Automatisé** (Recommandé - Production Complète)

Demandez simplement à Claude Code :
```
"Je veux une présentation sur [sujet] pour [audience]"
```

**Résultat automatique :**
- Structure projet dans `presentations/[sujet]/`
- Recherche web automatique et documentation
- Script Python d'orchestration personnalisé
- Configuration Sam AI adaptée à l'audience
- Présentation finale avec narration intégrée

### 📄 **Construction Manuelle** (Scripts individuels)

```bash
# 1. Créer la base (OBLIGATOIRE en premier)
python presentation_builder/01_slide_title_creator.py "Mon Titre de Présentation"

# 2. Ajouter navigation (recommandé si >5 slides)
python presentation_builder/02_navigation_builder.py \
  --insert-into "mon_titre_de_presentation.pptx" \
  --sections "Introduction" "Analyse" "Solutions" "Conclusion"

# 3. Ajouter contenu selon vos besoins (voir tableau ci-dessous)
```

### 📊 **Sélection Rapide par Besoin**

| **Vous voulez ajouter...** | **Script à utiliser** | **Exemple de commande** |
|---------------------------|----------------------|------------------------|
| 🏷️ **Nouvelle section** | `03_section_header_builder.py` | `python ... "Introduction" --insert-into "fichier.pptx" --style major` |
| 💬 **Message important** | `04_simple_message_builder.py` | `python ... "Message impactant" --insert-into "fichier.pptx" --style centered` |
| 📈 **2 statistiques** | `05_statistics_builder.py` | `python ... "85%" "Revenue" "92%" "Satisfaction" --insert-into "fichier.pptx"` |
| 📝 **3 ou 4 concepts** | `06_content_boxes_builder.py` | `python ... --insert-into "fichier.pptx" "Concept 1" "Concept 2" "Concept 3"` |
| 📖 **Explications détaillées** | `07_detailed_explanation_builder.py` | `python ... --insert-into "fichier.pptx" --style "four_points" --title "Architecture"` |
| 💬 **Témoignage client** | `08_testimonial_builder.py` | `python ... "Citation excellente" "Jean Dupont" --insert-into "fichier.pptx" --position "Directeur"` |
| 📈 **Graphiques/Charts** | `09_charts_builder.py` | `python ... --insert-into "fichier.pptx" --data-file "data/ventes.csv" --chart-type "column_clustered"` |
| 🎯 **Conclusion PT** | `10_conclusion_builder.py` | `python ... --insert-into "fichier.pptx" --style "passion_tech"` |

### 🤖 **Sam AI - Configuration Automatique**

**Sam** s'adapte automatiquement selon l'audience :
- **C-Level** : Style stratégique, vocabulaire business
- **Technique** : Style précis, vocabulaire expert
- **Formation** : Style pédagogique, vocabulaire accessible

```bash
# Configuration ElevenLabs requise
export ELEVENLABS_API_KEY="your_key"
```

---

## 🚀 **Exemple Complet - Présentation "Transformation Numérique"**

```bash
# 1. Créer la base
python presentation_builder/01_slide_title_creator.py "Transformation Numérique 2024" \
  --subtitle "Stratégie et Roadmap" \
  --metadata "2024.10.07 – Direction IT"

# 2. Navigation
python presentation_builder/02_navigation_builder.py \
  --insert-into "transformation_numerique_2024.pptx" \
  --sections "Context" "Stratégie" "Plan d'Action" "ROI"

# 3. Section "Context"
python presentation_builder/03_section_header_builder.py "Context" \
  --insert-into "transformation_numerique_2024.pptx" --style major

# 4. Message d'accroche
python presentation_builder/04_simple_message_builder.py \
  "Le numérique transforme nos opérations quotidiennes" \
  --insert-into "transformation_numerique_2024.pptx" --style centered

# 5. KPI actuels (2 statistiques)
python presentation_builder/05_statistics_builder.py \
  "78%" "Satisfaction Équipes" "120%" "Productivité" \
  --insert-into "transformation_numerique_2024.pptx"

# 6. Section "Stratégie"
python presentation_builder/03_section_header_builder.py "Stratégie" \
  --insert-into "transformation_numerique_2024.pptx" --style major

# 7. Les 4 concepts clés
python presentation_builder/06_content_boxes_builder.py \
  --insert-into "transformation_numerique_2024.pptx" \
  "Cloud First" "Data Driven" "DevOps Culture" "Security by Design"

# 8. Témoignage
python presentation_builder/08_testimonial_builder.py \
  "Cette approche nous a permis de doubler notre vélocité" "Marie Tremblay" \
  --insert-into "transformation_numerique_2024.pptx" \
  --position "Chef de Projet" --company "Équipe DevOps"

# 9. Conclusion
python presentation_builder/10_conclusion_builder.py \
  --insert-into "transformation_numerique_2024.pptx" --style "passion_tech"
```

---

## ⚠️ **Règles Importantes**

1. **TOUJOURS commencer par le Script 01** (création de base)
2. **Utiliser `--insert-into "fichier.pptx"`** pour tous les autres scripts (02-10)
3. **Le nom du fichier** est généré automatiquement à partir du titre
4. **Sauvegarde automatique** avant chaque modification
5. **Templates Premier Tech** : 57 slides authentiques (préservation styles)
6. **Workflow moderne** : Préférer le workflow automatisé par sujet

---

## 📖 **Besoin de plus de détails ?**

### Documentation Complète
- [COMMANDES.md](COMMANDES.md) : Paramètres détaillés des scripts
- [CHARTS_ENHANCED_GUIDE.md](CHARTS_ENHANCED_GUIDE.md) : Guide graphiques avec CSV
- [../CLAUDE.md](../CLAUDE.md) : Architecture complète et workflow automatisé
- [../templates/presentation-project/](../templates/presentation-project/) : Templates de projet

### Projets d'Exemple
- [../presentations/](../presentations/) : Exemples par sujet et audience

---

## 🔧 **Setup et Commandes Utiles**

```bash
# Installation
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_key"

# Lister les options disponibles
python presentation_builder/[SCRIPT_NAME].py --help

# Exemples de données pour graphiques
ls data/charts/  # CSV d'exemples fournis

# Structure d'un projet automatisé
ls presentations/[sujet]/[audience]/
```

## 🎯 **Évolution du Workflow**

**Traditionnel** : Construction slide par slide
**Moderne** : Workflow automatisé par sujet avec :
- Documentation automatique via recherche web
- Scripts Python d'orchestration personnalisés
- Configuration Sam AI adaptative
- Structure réutilisable multi-audiences
- Qualité Premier Tech garantie