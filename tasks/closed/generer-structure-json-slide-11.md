# Générer Structure JSON Détaillée pour Slide 11

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
Il n'existe pas de représentation structurée et documentée des shapes dans les slides du template Premier Tech. Les développeurs doivent deviner où placer le contenu et quelles sont les contraintes de chaque élément visuel.

**Impact sur l'utilisateur :**
- Perte de temps à explorer manuellement le template pour comprendre la structure
- Risque d'utiliser incorrectement les placeholders
- Difficulté à maintenir la cohérence visuelle Premier Tech
- Impossible de valider automatiquement si le contenu respecte les contraintes du template

## 💡 Solution Proposée

**Expérience cible :**
L'utilisateur devrait pouvoir consulter un fichier JSON qui documente précisément chaque élément de la slide 11 (et éventuellement des autres slides), avec ses propriétés exactes et une description claire de son usage prévu.

**Bénéfices attendus :**
- Documentation claire et accessible de la structure des slides
- Développement plus rapide des builders de slides
- Validation automatique possible du contenu vs template
- Préservation garantie de l'identité visuelle Premier Tech

## 🛠️ Implémentation

### Ce qui doit changer
- **Nouveau dossier :** `templates/presentation-project/slide-structure/`
- **Nouveau fichier :** `slide_11_structure.json` avec description complète
- **Nouveau script :** `tools/extract_slide_structure.py` - Script réutilisable pour extraire la structure de n'importe quelle slide

### Structure JSON attendue
```json
{
  "slide_number": 11,
  "slide_name": "Title Slide",
  "shapes": [
    {
      "name": "Title Placeholder",
      "position": {"left": X, "top": Y},
      "dimensions": {"width": W, "height": H},
      "text_content": "Contenu actuel visible",
      "font_size": 44,
      "description": "Titre principal de la présentation - Max 60 caractères recommandé"
    }
  ]
}
```

### Tests de validation
- [ ] Script génère correctement le JSON pour slide 11
- [ ] Script fonctionne pour n'importe quelle slide (paramétrable)
- [ ] Descriptions manuelles ajoutées et pertinentes
- [ ] Structure JSON validable avec schema

### Documentation à ajuster
- [ ] `docs/TEMPLATE_STRUCTURE_GUIDE.md` - Nouveau guide sur la structure des templates
- [ ] `CLAUDE.md` - Ajouter référence au nouveau dossier slide-structure

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Peut consulter la structure exacte de la slide 11 en JSON
- [ ] Comprend immédiatement quel contenu mettre dans chaque shape
- [ ] Peut utiliser le script pour analyser d'autres slides

**Pour le système :**
- [ ] JSON généré automatiquement à partir du template existant
- [ ] Script réutilisable pour les 57 slides du template
- [ ] Format JSON cohérent et extensible

## 🚀 Prochaines Étapes

1. **Analyser** le fichier `template_analysis_output/slide_11.json` existant
2. **Développer** le script d'extraction de structure
3. **Générer** le fichier JSON pour slide 11
4. **Enrichir** avec les descriptions manuelles de chaque shape
5. **Tester** le script sur d'autres slides pour valider la réutilisabilité

---

**Créé :** 2025-10-16
**Priorité :** Élevée
**Estimation :** 2-3 heures