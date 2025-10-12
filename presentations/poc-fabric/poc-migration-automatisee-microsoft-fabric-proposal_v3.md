# PoC: Réduire ETO v2 de 8-11h à 2h par jour avec Microsoft Fabric

## Validation de Performance sur un Workflow Critique

## Quoi ?

### Objectif du PoC
Valider que **Microsoft Fabric peut réduire de 90% le temps d'exécution d'ETO v2**, passant de 8-11 heures actuelles à moins de 2 heures par exécution, en modernisant l'architecture de données et les processus ETL.

### Périmètre Technique
- **Migration du workflow ETO v2** vers Microsoft Fabric (jobs RDL00001 et RDL00002)
- **Remplacement de SSIS** par Dataflow Gen2 et Fabric Pipelines
- **Optimisation de l'architecture** avec OneLake et Fabric Data Warehouse
- **Validation des performances** sur données réelles de production

### Livrables Attendus
- Environnement Fabric configuré avec workflow ETO v2 migré
- Comparatif de performance documenté (temps d'exécution, ressources)
- Plan d'implémentation pour mise en production
- Recommandations pour migration d'autres workflows critiques

## Pourquoi ?

### Impact Business Critique
- **Libération de ressources**: 6-9h de capacité infrastructure récupérées par jour
- **Amélioration de la réactivité**: Jobs plus rapides = données business plus fraîches
- **Réduction des coûts d'opportunité**: Moins de blocages sur infrastructure partagée
- **Préparation à l'évolution**: Foundation moderne pour croissance des besoins data

### Risques du Status Quo
- **Performance dégradante**: ETO v2 devient de plus en plus lent
- **Impact croissant**: 4 exécutions par jour multiplient les retards
- **Vieillissement technique**: Architecture SSIS difficile à maintenir et optimiser
- **Limitation de croissance**: Infrastructure actuelle ne peut pas absorber plus de charge

### Opportunité Stratégique
- **Modernisation progressive**: Commencer par le workflow le plus critique
- **Validation technologique**: Prouver la viabilité de Fabric dans notre contexte
- **Foundation future**: Base pour migration d'autres processus critiques
- **Amélioration continue**: Opportunité d'optimiser les processus existants

## Pourquoi Maintenant ?

### Urgence et Contexte Favorable
- **Problème qui s'aggrave**: ETO v2 performance continue de se dégrader
- **Coût d'opportunité**: Chaque jour de retard = 8-11h de ressources infrastructure monopolisées
- **Impact croissant**: Les jobs s'exécutent 4 fois par jour, amplifiant les retards
- **Technologie mature**: Microsoft Fabric stable, moment optimal pour validation
- **Impact mesurable**: Gains quantifiables sur cas concret (90% d'amélioration potentielle)
- **Fenêtre d'opportunité**: Période favorable pour tests sans impact production

### Alternative au Status Quo
**Sans action**: ETO v2 continue de monopoliser 8-11h quotidiennes d'infrastructure, impactant la réactivité business
**Avec PoC**: Validation d'une solution moderne qui libérerait 6-9h de capacité par jour

## Périmètre du PoC

### Inclusions
- **PowerBI de Fabric**: Création et consommation de rapports depuis PowerBI Online
- **Fabric Mirroring**: Réplication temps réel des données sources
- **Dataflow Gen2**: Pipelines de transformation de données modernes
- **OneLake**: Stockage unifié des données
- **Fabric Data Warehouse**: Entrepôt de données analytique cloud-native

### Exclusions
- **Mise en opération**: Le PoC ne couvrira pas le déploiement en production
- **Microsoft Purview**: La gouvernance des données sera traitée dans une phase ultérieure
- **Migration complète**: Seul le workflow ETO v2 sera traité

---

### Métadonnées du Document
- **Titre**: PoC Validation Microsoft Fabric - Cas ETO v2
- **Version**: 2.0
- **Date**: 2025-08-27
- **Auteur**: Maxime Ouellet (OUEM7)
- **Destinataires**: Emmanuel Dugas-Gallant (DUGE)
- **Classification**: Confidentiel - Usage interne Premier Tech

---

## 1. Le Problème : ETO v2 en Perte de Vitesse

### 1.1 Situation Actuelle
**ETO v2** est un workflow critique composé de deux jobs avec des dégradations de performance majeures:

**RDL00001_EnterpriseDataETO_V2_FULL**:
- **Exécution**: À 23h00 chaque jour
- **Durée actuelle**: ~4 heures de traitement

**RDL00001_EnterpriseDataETO_V2_PARTITIONS**:
- **Exécution**: 4h00, 11h00, 14h00 (3x/jour)
- **Durée actuelle**: 1h45 à 2h30 par exécution

**Impact total**: 8-11 heures quotidiennes de ressources infrastructure monopolisées
**Impact business**: Retards dans la prise de décision opérationnelle, données non disponibles pendant le traitement
**Équipes affectées**: 
- Infrastructure (LEVJ4 et équipe)
- Utilisateurs finaux PTG
- Tous les consommateurs de rapports BI (incluant PTSA et autres groupes)
- **Impact indirect**: Les ressources libérées pourront être réinvesties au bénéfice de tous les projets BI

### 1.2 Objectif de Performance
- **Cible FULL**: Réduire de 4h à moins de 30 minutes (~90% d'amélioration)
- **Cible PARTITIONS**: Réduire de 1h45-2h30 à moins de 15 minutes (~85% d'amélioration)
- **Impact total**: Passer de 8-11h quotidiennes à moins de 2h
- **Libération ressources**: 6-9 heures de capacité infrastructure récupérées par jour

### 1.3 Gains Business Attendus
- **Performance accrue**: Disponibilité des données énormément accéléré pour la prise de décision
- **Fiabilité améliorée**: Architecture moderne réduisant les risques de défaillance
- **Agilité business**: Capacité à traiter plus fréquemment les données pour répondre aux besoins métiers
- **ROI Infrastructure**: Réallocation des ressources libérées vers d'autres projets critiques

---

## 2. La Solution Proposée : PoC Microsoft Fabric

### 2.1 Approche PoC - Modernisation Complète (Non Migration)

**Important**: Il ne s'agit pas d'une simple migration mais d'une **modernisation complète** du processus:

1. **Analyse du processus actuel**: Scanner et comprendre la logique métier d'ETO v2
2. **Réarchitecture moderne**: Concevoir une nouvelle architecture optimisée pour Fabric
   - Exploitation native des capacités cloud (parallélisation, mise en cache)
   - Utilisation optimale de OneLake et du Data Warehouse
   - Pipeline Dataflow Gen2 conçu pour la performance
3. **Implémentation nouvelle**: Développer le processus modernisé (non une copie)
4. **Validation fonctionnelle**: Assurer l'équivalence des résultats avec une meilleure performance
5. **Documentation**: Méthodologie reproductible pour autres workflows

### 2.1.1 Stratégie d'Extraction JDE pour la PoC

**Approche Recommandée - Extraction Incrémentale avec Dataflow Gen2**:
- **Technique**: Extraction incrémentale basée sur timestamps/watermarks
- **Outil**: Dataflow Gen2 natif dans Fabric
- **Avantages PoC**:
  - Pas de dépendance externe coûteuse
  - Contrôle total sur la logique d'extraction
  - Optimisation des ressources JDE
  - Rapidité de mise en œuvre

**Approches Non Retenues pour la PoC**:
- **CDC coûteux** (ex: Qlik, Fivetran): Budget et complexité incompatibles avec PoC
- **Développement CDC custom**: Risque élevé et temps de développement prohibitif
- **Mirroring direct**: Dépendance technologique non justifiée pour validation concept

**Justification Technique**:
- La PoC vise à valider les gains de performance, pas l'architecture finale
- L'extraction incrémentale permet de tester la modernisation du pipeline
- Les techniques classiques restent optimales pour un environnement contrôlé

### 2.2 Pourquoi ETO v2 comme Cas Test
- **Représentatif**: 2 jobs typiques (FULL + PARTITIONS) avec patterns différents
- **Mesurable**: Performance actuelle bien documentée (4h + 3x2h quotidien)
- **Impact critique**: 8-11h quotidiennes de ressources monopolisées
- **Expertise disponible**: Jean-Guy Lévesque connaît intimement ces jobs
- **Gain potentiel majeur**: 6-9 heures d'infrastructure libérées par jour

### 2.3 Impact Élargi sur l'Écosystème BI
- **Effet domino**: La dégradation d'ETO v2 impacte TOUS les projets BI qui dépendent de la disponibilité des ressources pour le rafraîchissement de leurs propres données
- **Bénéfice généralisé**: L'amélioration d'ETO v2 profitera à l'ensemble de l'écosystème BI

---

## 3. Plan d'Exécution (4 Semaines)

### 3.1 Timeline Détaillée

| **Semaine** | **Activités**                      | **Livrables**                     | **Validation**                  |
| ----------- | ---------------------------------- | --------------------------------- | ------------------------------- |
| **S1**      | Scanner IA du workflow ETO v2      | Catalogue complet des composants  | Métadonnées extraites à 90%+    |
| **S2**      | Génération automatique Fabric      | Workflow ETO v2 migré dans Fabric | Migration fonctionnelle validée |
| **S3**      | Tests de performance et validation | Résultats comparatifs             | Performance < 30 minutes        |
| **S4**      | Documentation et recommandations   | Rapport final PoC                 | Décision go/no-go               |

### 3.0 Semaine S0 - Préparation (Prérequis)

| **Activité** | **Responsable** | **Validation** |
|-------------|-----------------|----------------|
| Valider l'approche d'extraction incrémentale JDE | OUEM7 + Équipe ERP | Stratégie Dataflow Gen2 confirmée |
| Obtenir accès JDE pour données requises | Équipe ERP | Accès de lecture confirmé |
| Identifier les tables et champs ETO v2 | Équipe Data | Mapping source-cible documenté |
| Provisionner environnement Fabric test | DUGE | Environnement prêt |
### 3.2 Équipe Projet
- **Maxime Ouellet (OUEM7)**: Responsable technique, exécution
- **Jean-Guy Lévesque (LEVJ4)**: Expert infrastructure, validation technique ETO v2
- **Représentant équipe Data**: Support sur le fonctionnement actuel du processus ETO
- **Emmanuel Dugas-Gallant (DUGE)**: Supervision environnement Fabric
- **Yvan Chouinard**: Gestion de projet PoC
- **Décision finale**: Management IT (selon processus d'approbation standard)

### 3.3 Ressources Requises
- **Budget**: <1000$ (environnement Fabric temporaire)
- **Accès**: DevOps, bases de données dev ETO v2
- **Durée**: 4 semaines à temps partiel

---

## 4. Critères de Réussite

### 4.1 Critères Techniques (Go/No-Go)
- ✅ **Migration réussie**: Les 2 jobs ETO v2 (ou une version unifiée) fonctionnent dans Fabric
- ✅ **Performance FULL**: < 30 minutes (vs 4h actuellement)
- ✅ **Performance PARTITIONS**: < 15 minutes (vs 1h45-2h30 actuellement)
- ✅ **Équivalence fonctionnelle**: Mêmes résultats que version actuelle
- ✅ **Catalogue automatisé**: 90%+ des composants identifiés automatiquement

### 4.2 Critères Business
- ✅ **Reproductibilité**: Méthodologie applicable à d'autres workflows
- ✅ **Complexité manageable**: Effort de déploiement élargi estimable
- ✅ **Valeur démontrée**: Gains quantifiés et validés par Jean-Guy
- ✅ **Intégration PowerBI Online**: Les rapports existants seront convertis à PowerBI Online qui lira directement depuis les données stockées dans Fabric (OneLake et Data Warehouse)

### 4.3 Métriques de Validation

| **Métrique** | **Actuel** | **Cible PoC** | **Méthode** |
|--------------|------------|---------------|-------------|
| Job FULL | 4 heures | < 30 minutes | Chronométrage |
| Job PARTITIONS | 1h45-2h30 | < 15 minutes | Chronométrage |
| Impact total quotidien | 8-11 heures | < 2 heures | Calcul total |
| Extraction métadonnées | Manuelle | 90% automatisée | Audit catalogue |
| Équivalence fonctionnelle | N/A | 100% | Tests de régression |

---

## 5. Décision et Prochaines Étapes

### 5.1 Scénarios Post-PoC

| **Résultat PoC** | **Action Recommandée** | **Timeline** |
|------------------|----------------------|--------------|
| **Succès complet** | Phase pilote élargie (3-5 workflows) | 4-6 semaines |
| **Succès partiel** | Itération ciblée sur défis identifiés | 2-4 semaines |
| **Échec technique** | Réévaluation stratégique | Immédiate |

### 5.2 Validation des Parties Prenantes

| **Rôle** | **Critère de Validation** | **Décision** |
|----------|---------------------------|--------------|
| **Jean-Guy (LEVJ4)** | Performance < 30 minutes | Validation technique infrastructure |
| **Équipe Data** | Intégrité des données maintenue | Validation fonctionnelle |
| **Emmanuel (DUGE)** | Alignement architecture | Faisabilité déploiement |
| **Yvan Chouinard** | Gestion projet réussie | Validation processus |
| **Management IT** | Valeur business démontrée | Go/No-Go final |

### 5.3 Détail du Budget (<1000$)
- **Frais d'exploitation Fabric**: Capacité F2 ou F4 pour 4 semaines (~800-1000$)
- **Stockage OneLake**: Inclus dans la capacité
- **Transfert de données**: Inclus dans la capacité
- **Aucun coût de licence**: Utilisation des licences existantes

### 5.4 Analyse de Risques Détaillée

| **Risque** | **Impact** | **Probabilité** | **Mitigation** |
|------------|------------|-----------------|----------------|
| Manque d'accès JDE | Bloquant | Moyenne | Validation en S0 avec équipe ERP |
| Absence Jean-Guy (vacances) | Moyenne | Faible | Documentation existante + équipe backup |
| Collaboration limitée équipes | Moyenne | Faible | Engagement préalable des parties prenantes |
| Délais approbations | Bloquant | Moyenne | Processus d'approbation clarifié en S0 |

### 5.5 Engagement Minimal, Impact Maximal
- **Apprentissage**: Validation concrète avant décisions majeures
- **Impact potentiel**: Base pour modernisation complète si validé

---

**Décision Attendue**: Approbation pour démarrage PoC 4 semaines

**Document confidentiel - Propriété de Premier Tech**  
*Version 2.0 - 2025-08-27*