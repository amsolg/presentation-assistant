# Templates de Slides Suggérés - IA Générative (Audience Technique)

## 🎯 Priorité 1 - Slides Essentielles

### 1. **Slide 13 - Table des Matières**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 13 ajout
```
- **Usage** : Structure claire du contenu technique
- **Contenu suggéré** : Architecture, Implémentation, Performance, Sécurité, Déploiement

### 2. **Slide 14 - Section Architecture**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 14 ajout
```
- **Usage** : Titre de section principale
- **Contenu suggéré** : "Architecture et Composants Techniques"

### 3. **Slide 31 - Détails d'Implémentation (4 boîtes)**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 31 ajout
```
- **Usage** : Détails techniques approfondis
- **Contenu suggéré** : APIs, Base de données, Authentification, Monitoring

### 4. **Slide 6 - Diagramme d'Architecture**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 6 ajout
```
- **Usage** : Visualisation de l'architecture système
- **Contenu suggéré** : Flux de données, composants, intégrations

## 🔧 Priorité 2 - Slides Techniques Spécialisées

### 5. **Slide 27 - Comparaisons Techniques (3 boîtes)**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 27 ajout
```
- **Usage** : Comparaison de solutions techniques
- **Contenu suggéré** : Solutions cloud vs on-premise, frameworks, outils

### 6. **Slide 22 - Métriques Performance (2 stats)**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 22 ajout
```
- **Usage** : KPIs techniques essentiels
- **Contenu suggéré** : Latence moyenne, Throughput

### 7. **Slide 24 - Statistiques Détaillées (4 stats)**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 24 ajout
```
- **Usage** : Métriques complètes du système
- **Contenu suggéré** : CPU, Mémoire, Réseau, Disponibilité

### 8. **Slide 36 - Documentation Technique (avec image)**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 36 ajout
```
- **Usage** : Énoncé technique avec diagramme
- **Contenu suggéré** : Processus d'intégration, workflow

## 📊 Priorité 3 - Slides avec Données

### 9. **Slide 46 - Graphiques Performance**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 46 ajout
```
- **Usage** : Visualisation des métriques
- **Données requises** : Créer `data/performance_metrics.csv`

### 10. **Slide 47 - Graphiques Évolution**
```bash
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 47 ajout
```
- **Usage** : Tendances et évolution dans le temps
- **Données requises** : Créer `data/evolution_stats.csv`

## 🎨 Séquence de Construction Recommandée

### Phase 1 : Structure (5 min)
1. Table des matières (slide 13)
2. Sections principales (slides 14-16)

### Phase 2 : Contenu Principal (10 min)
3. Architecture détaillée (slide 31)
4. Diagrammes techniques (slide 6)
5. Comparaisons (slide 27)

### Phase 3 : Métriques (5 min)
6. Performance (slide 22)
7. Statistiques complètes (slide 24)

### Phase 4 : Données Avancées (10 min)
8. Graphiques avec CSV (slides 46-47)
9. Documentation visuelle (slide 36)

## 📋 Templates par Type de Contenu

### **Architecture et Design**
- Slides 6-10 : Graphiques et diagrammes
- Slide 36-37 : Énoncés avec images
- Slide 31-35 : Détails techniques structurés

### **Performance et Métriques**
- Slides 22-26 : Statistiques et KPIs
- Slides 46-51 : Graphiques de données

### **Comparaisons et Alternatives**
- Slides 27-30 : Contenu structuré en 3 boîtes
- Slides 39-44 : Listes et comparaisons duales

### **Documentation et Processus**
- Slides 17-21 : Messages simples et mots-clés
- Slide 45 : Citations et témoignages techniques

## 🚀 Commande Complète pour Démarrage Rapide
```bash
# Créer une présentation technique complète en une fois
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 13 ajout
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 14 ajout
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 31 ajout
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 6 ajout
python tools/add_slide.py tests/ia-generative-integration/technique/presentation_schema.json 22 ajout

# Puis générer
python presentation_builder/presentation_builder.py tests/ia-generative-integration/technique/presentation_schema.json
```