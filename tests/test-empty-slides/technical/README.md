# Présentation : Test Empty Slides

## Informations générales
- **Sujet** : test-empty-slides
- **Audience** : technical
- **Type** : Test
- **Créé le** : 2025-10-20 21:13:05

## Structure des fichiers
- `presentation_schema.json` : Configuration principale de la présentation
- `output/` : Présentations générées
- `data/` : Données pour graphiques (CSV)

## Utilisation
Pour générer la présentation :
```bash
python presentation_builder/presentation_builder.py tests\test-empty-slides\technical/presentation_schema.json
```

## Notes
- Modifier `presentation_schema.json` pour personnaliser les slides
- Ajouter des fichiers CSV dans `data/` pour les graphiques
- Les présentations générées seront dans `output/`
