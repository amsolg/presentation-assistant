# Présentation : Innovation Digitale

## Informations générales
- **Sujet** : innovation-digitale
- **Audience** : c-level
- **Type** : Présentation
- **Créé le** : 2025-10-20 16:03:55

## Structure des fichiers
- `presentation_schema.json` : Configuration principale de la présentation
- `output/` : Présentations générées
- `data/` : Données pour graphiques (CSV)

## Utilisation
Pour générer la présentation :
```bash
python presentation_builder/presentation_builder.py presentations\innovation-digitale\c-level/presentation_schema.json
```

## Notes
- Modifier `presentation_schema.json` pour personnaliser les slides
- Ajouter des fichiers CSV dans `data/` pour les graphiques
- Les présentations générées seront dans `output/`
