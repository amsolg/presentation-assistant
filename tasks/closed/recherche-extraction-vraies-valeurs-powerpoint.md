# Recherche - Extraction des Vraies Valeurs de Formatage PowerPoint

## 🎯 Problème à Résoudre

**Ce qui ne fonctionne pas actuellement :**
Le script `src/slide_extractor.py` utilise des valeurs par défaut "improvisées" pour le formatage du texte (font_name, font_size, color) au lieu d'extraire les vraies valeurs depuis le fichier PowerPoint. Cela crée une incertitude sur la fidélité de l'extraction.

**Impact sur l'utilisateur :**
- Incertitude sur les vraies valeurs de formatage des templates
- Risque de reproduire incorrectement les styles Premier Tech
- Impossibilité de valider que les valeurs extraites sont exactes
- Documentation potentiellement incorrecte des templates

## 💡 Solution Proposée

**Expérience cible :**
Le script devrait extraire les VRAIES valeurs de formatage depuis le fichier PowerPoint, sans improvisation. Si l'extraction est impossible pour certaines valeurs, cela doit être clairement indiqué avec la raison technique.

## 🛠️ Recherche à Effectuer

### Questions Clés à Résoudre

1. **Pourquoi python-pptx retourne null pour les propriétés de formatage ?**
   - Est-ce un problème de placeholders vs shapes normales ?
   - Les valeurs sont-elles héritées du master/layout ?
   - Y a-t-il une différence entre le formatage direct et hérité ?

2. **Comment accéder aux valeurs héritées des masters/layouts ?**
   - Via slide_layout et slide_master ?
   - Via placeholder_format ?
   - Via le XML directement ?

3. **Alternatives à python-pptx pour l'extraction ?**
   - Accès direct au XML du fichier .pptx
   - Autres bibliothèques Python (python-docx, openpyxl patterns)
   - Outils Microsoft Office COM sur Windows

### Recherches Web à Effectuer

1. "python-pptx extract inherited font properties from placeholder"
2. "python-pptx get master slide formatting"
3. "extract real font size from powerpoint placeholder python"
4. "python-pptx text_frame font returns None"
5. "powerpoint xml structure font formatting placeholders"
6. "python extract styles from pptx slide master"

### Code à Tester

```python
# Test 1: Accès via slide_layout
from pptx import Presentation

prs = Presentation('template.pptx')
slide = prs.slides[0]
layout = slide.slide_layout
master = layout.slide_master

# Explorer les placeholders du layout
for placeholder in layout.placeholders:
    print(f"Placeholder: {placeholder.name}")
    if placeholder.text_frame:
        # Essayer d'obtenir le formatage du layout
        pass

# Test 2: Accès direct au XML
import zipfile
import xml.etree.ElementTree as ET

with zipfile.ZipFile('template.pptx', 'r') as pptx:
    # Lire le XML de la slide
    slide_xml = pptx.read('ppt/slides/slide1.xml')
    # Parser et chercher les styles
    pass
```

## ✅ Critères de Succès

**Pour l'utilisateur :**
- [ ] Extraction des VRAIES valeurs de formatage quand disponibles
- [ ] Indication claire quand une valeur ne peut pas être extraite
- [ ] Documentation de la source de chaque valeur (direct, hérité, défaut système)
- [ ] Rapport technique expliquant les limitations

**Pour le système :**
- [ ] Pas de valeurs improvisées sans indication
- [ ] Code robuste qui gère les cas d'héritage
- [ ] Documentation des limitations techniques
- [ ] Tests prouvant l'exactitude des extractions

## 🚀 Plan d'Action

1. **Recherche Web** sur l'extraction des propriétés héritées
2. **Analyse du XML** direct des fichiers .pptx
3. **Test des différentes approches** avec python-pptx
4. **Documentation des découvertes** et limitations
5. **Implémentation** de la meilleure solution
6. **Rapport final** avec recommandations

---

**Créé :** 2025-10-17
**Priorité :** Élevée
**Estimation :** 2-3 heures