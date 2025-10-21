# Présentation : Ia Generative Integration

## Informations générales
- **Sujet** : ia-generative-integration
- **Audience** : technique
- **Type** : Test
- **Créé le** : 2025-10-21 10:25:13

## Structure des fichiers
- `presentation_schema.json` : Configuration principale de la présentation
- `output/` : Présentations générées
- `data/` : Données pour graphiques (CSV)

## Utilisation
Pour générer la présentation :
```bash
python presentation_builder/presentation_builder.py tests\ia-generative-integration\technique/presentation_schema.json
```

## Notes
- Modifier `presentation_schema.json` pour personnaliser les slides
- Ajouter des fichiers CSV dans `data/` pour les graphiques
- Les présentations générées seront dans `output/`
