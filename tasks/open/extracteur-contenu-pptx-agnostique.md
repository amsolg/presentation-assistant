# Extracteur de Contenu PowerPoint Agnostique

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
L'extracteur actuel récupère du contenu "fantôme" provenant des templates (texte par défaut comme "Cliquez pour ajouter un titre") dans les fichiers JSON générés, polluant les données avec des informations non pertinentes.

**Impact sur l'utilisateur :**
- Les JSON générés contiennent des données parasites qui nécessitent un nettoyage manuel
- Impossible de distinguer automatiquement le vrai contenu des placeholders vides
- Risque d'inclure du texte template dans les présentations finales

## 💡 Solution Proposée

**Expérience cible :**
L'utilisateur lance l'extraction sur une slide et obtient un JSON contenant UNIQUEMENT le contenu qu'il a explicitement ajouté, sans aucun texte par défaut ou placeholder hérité du template.

**Bénéfices attendus :**
- JSON propres sans données parasites
- Extraction 100% fiable du contenu réel
- Compatibilité avec tous les templates PowerPoint

## 🛠️ Implémentation

### Ce qui doit changer
- **tools/slide_extractor.py :** Nouveau script avec logique de comparaison différentielle
- **Architecture :** Implémenter la hiérarchie masque → layout → slide
- **Algorithme :** Utiliser l'attribut `idx` pour matcher les placeholders entre slide et layout

### Tests de validation
- [ ] Extraction slide 11 ne contient plus "Cliquez pour ajouter du texte"
- [ ] Seul le contenu ajouté par l'utilisateur est extrait
- [ ] Fonctionne avec différents templates PT

### Documentation à ajuster
- [ ] `docs/SLIDE_EXTRACTION_GUIDE.md` - Créer guide technique
- [ ] `CLAUDE.md` - Ajouter référence au nouvel extracteur

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Extraction en 1 commande sans post-traitement
- [ ] JSON ne contient que le contenu réellement ajouté
- [ ] Compatible avec tous les templates Premier Tech

**Pour le système :**
- [ ] Tests unitaires validés sur slides 11, 13 et autres
- [ ] Performance < 1s par slide
- [ ] Code documenté et maintenable

## 🚀 Prochaines Étapes

1. **Analyser** les fichiers JSON problématiques (slide_11.json, slide_13.json)
2. **Implémenter** la logique de comparaison idx-based
3. **Tester** sur l'ensemble des 57 slides du template
4. **Documenter** l'architecture d'extraction

---

**Créé :** 2025-01-17
**Priorité :** Élevée
**Estimation :** 2-3 heures