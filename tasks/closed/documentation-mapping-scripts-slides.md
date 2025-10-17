# Documentation Mapping Scripts-Slides

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
Les développeurs et utilisateurs avancés n'ont pas de vue d'ensemble claire sur quel script génère quelle slide et où trouver les templates correspondants.

**Impact sur l'utilisateur :**
- Difficile de savoir quel script utiliser pour un type de slide spécifique
- Perte de temps à chercher dans le code pour comprendre les correspondances
- Risque d'utiliser le mauvais script ou template

## 💡 Solution Proposée

**Expérience cible :**
L'utilisateur ouvre un seul document de référence et voit immédiatement :
- Les 9 scripts disponibles avec leur fonction
- Pour chaque script : les numéros de slides supportées
- Le chemin direct vers chaque template analysé

**Bénéfices attendus :**
- Compréhension immédiate du système complet
- Choix rapide du bon script pour chaque besoin
- Navigation facile vers les templates pour personnalisation

## 🛠️ Implémentation

### Ce qui doit changer
- **Nouveau fichier :** `docs/SCRIPTS_SLIDES_MAPPING.md` - Document de référence complet
- **Analyse :** Parcourir les 9 scripts dans `presentation_builder/`
- **Extraction :** Mapper chaque script avec ses slides depuis `CONTENT_TO_TEMPLATE_MAPPING`
- **Liaison :** Lier chaque slide à son template dans `template_analysis_output/`

### Format du document cible
```markdown
# Mapping Scripts → Slides → Templates

## 1. presentation_builder.py
**Rôle :** Orchestrateur principal
**Slides supportées :** N/A (coordination uniquement)

## 2. navigation_builder.py
**Rôle :** Tables des matières et navigation
**Slides supportées :**
- Slide 13 (index 12) - Table des matières
  - Template : `template_analysis_output/slide_13_analysis.md`

## 3. section_header_builder.py
**Rôle :** Pages de section et titres
**Slides supportées :**
- Slides 14-16 (index 13-15) - Sections
  - Templates : `template_analysis_output/slide_14_analysis.md` à `slide_16_analysis.md`

[... continuer pour les 9 scripts ...]
```

### Tests de validation
- [ ] Document liste bien les 9 scripts
- [ ] Chaque script a ses slides correctement mappées
- [ ] Tous les chemins de templates sont valides et accessibles

### Documentation à ajuster
- [ ] `CLAUDE.md` - Ajouter référence au nouveau document de mapping
- [ ] `docs/README.md` - Lister le nouveau guide de référence

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Peut identifier le bon script en < 10 secondes
- [ ] Trouve le template correspondant immédiatement
- [ ] Comprend l'architecture complète du système

**Pour le système :**
- [ ] Mapping complet et à jour
- [ ] Tous les liens fonctionnent
- [ ] Documentation cohérente avec le code

## 🚀 Prochaines Étapes

1. **Analyser** les 9 scripts dans `presentation_builder/`
2. **Extraire** le mapping depuis `presentation_builder.py`
3. **Créer** le document de référence structuré
4. **Valider** tous les chemins et correspondances

---

**Créé :** 2025-01-16
**Priorité :** Élevée
**Estimation :** 30 minutes