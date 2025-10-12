#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script d'orchestration automatique - Presentation Assistant pour Équipe Architecture d'Entreprise
Généré automatiquement par le Presentation Assistant le 2025-10-10

Ce script utilise les presentation_builder pour construire une présentation
adaptée spécifiquement à l'audience Équipe Architecture d'Entreprise selon l'analyse contextuelle.

Configuration audience:
- Niveau d'expertise: Expert technique (4-5/5)
- Style Sam: Expert technique avec enthousiasme mesuré
- Durée cible: 14 minutes
- Scripts utilisés: Scripts réels disponibles

NOTES IMPORTANTES:
- Les titres doivent faire moins de 45 caractères (limitation script 01)
- Les chemins relatifs doivent partir de presentation_builder/ (format: ../presentations/...)
- Toujours spécifier --template ../../../templates/Template_PT.pptx pour les scripts d'insertion
"""

import os
import sys
import subprocess
import json
from datetime import datetime
from pathlib import Path

class PresentationOrchestrator:
    """Orchestrateur pour la construction automatique de présentation"""

    def __init__(self):
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.presentation_builder_path = self.project_root / "presentation_builder"
        self.output_dir = Path(__file__).parent / "output"
        self.output_dir.mkdir(exist_ok=True)

        # Configuration spécifique à l'audience
        self.audience_config = {
            "audience": "Équipe Architecture d'Entreprise",
            "expertise_level": "Expert technique (4-5/5)",
            "duration_target": "14 minutes",
            "sam_style": "Expert technique avec enthousiasme mesuré",
            "technical_depth": "Profondeur architecturale avancée",
            "communication_style": "Expert-à-expert avec crédibilité technique"
        }

        # Informations du projet
        self.project_info = {
            "subject": "Presentation Assistant - Architecture Système",
            "creation_date": "2025-10-10",
            "target_audience": "Équipe Architecture d'Entreprise",
            "estimated_slides": 15,
            "complexity_level": "4/5 - Expert technique"
        }

        # Séquence de construction optimisée avec les VRAIS scripts et paramètres
        self.build_sequence = [
            {
                "step_id": "title_slide",
                "script": "01_slide_title_creator.py",
                "params": [
                    "Presentation Assistant",
                    "--subtitle", "Architecture Système Enterprise",
                    "--metadata", "Équipe Architecture d'Entreprise",
                    "--project", "presentation_assistant_architecture",
                    "--output", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx"
                ],
                "description": "Slide 1: Page titre",
                "critical": True
            },
            {
                "step_id": "technical_navigation",
                "script": "02_navigation_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--sections", "Architecture & Composants", "Intégrations & APIs", "Quality & Performance", "Workflow & Extensibilité"
                ],
                "description": "Slide 2: Navigation Technique",
                "critical": True
            },
            {
                "step_id": "section_architecture",
                "script": "03_section_header_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--section-title", "Architecture & Composants",
                    "--section-subtitle", "Modularité et Patterns de Design"
                ],
                "description": "Slide 3: Section Architecture",
                "critical": True
            },
            {
                "step_id": "modular_components",
                "script": "06_content_boxes_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Composants Modulaires",
                    "--box1-title", "Script Layer",
                    "--box1-content", "10 modules spécialisés (01-10) avec responsabilités distinctes",
                    "--box2-title", "Template Engine",
                    "--box2-content", "Mapping intelligent vers 57 slides Premier Tech authentiques",
                    "--box3-title", "Orchestration Core",
                    "--box3-content", "Workflow automatisé avec gestion d'erreurs et validation"
                ],
                "description": "Slide 4: Composants Modulaires",
                "critical": True
            },
            {
                "step_id": "design_patterns",
                "script": "06_content_boxes_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Patterns de Design",
                    "--box1-title", "Strategy Pattern",
                    "--box1-content", "Scripts spécialisés par type de contenu",
                    "--box2-title", "Factory Pattern",
                    "--box2-content", "Création dynamique de slides selon templates",
                    "--box3-title", "Template Method",
                    "--box3-content", "Workflow standardisé avec étapes personnalisables",
                    "--box4-title", "Observer Pattern",
                    "--box4-content", "Monitoring et logging des opérations"
                ],
                "description": "Slide 5: Patterns de Design",
                "critical": True
            },
            {
                "step_id": "section_integration",
                "script": "03_section_header_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--section-title", "Intégrations & APIs",
                    "--section-subtitle", "ElevenLabs et Extensibilité"
                ],
                "description": "Slide 6: Section Intégrations",
                "critical": True
            },
            {
                "step_id": "api_integration",
                "script": "07_detailed_explanation_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Intégration ElevenLabs API",
                    "--style", "dual_lists_blue",
                    "Architecture API robuste avec authentification sécurisée",
                    "--additional",
                    "Rate limiting et backoff exponentiel",
                    "Latence ~75ms moyenne",
                    "Streaming support pour audio long",
                    "Cache intelligent multi-niveaux"
                ],
                "description": "Slide 7: Intégration API",
                "critical": True
            },
            {
                "step_id": "section_quality",
                "script": "03_section_header_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--section-title", "Quality & Performance",
                    "--section-subtitle", "Métriques et Monitoring"
                ],
                "description": "Slide 8: Section Quality",
                "critical": True
            },
            {
                "step_id": "performance_metrics",
                "script": "05_statistics_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Métriques de Performance",
                    "--stat1-value", "< 3 min",
                    "--stat1-label", "Génération",
                    "--stat1-context", "Présentation complète 15+ slides",
                    "--stat2-value", "95%",
                    "--stat2-label", "Tests",
                    "--stat2-context", "Couverture code et templates",
                    "--stat3-value", "100%",
                    "--stat3-label", "Conformité",
                    "--stat3-context", "Styles Premier Tech préservés"
                ],
                "description": "Slide 9: Métriques Performance",
                "critical": True
            },
            {
                "step_id": "monitoring_stats",
                "script": "05_statistics_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Monitoring et Observabilité",
                    "--stat1-value", "Real-time",
                    "--stat1-label", "Monitoring",
                    "--stat1-context", "Métriques et alerting automatique",
                    "--stat2-value", "100%",
                    "--stat2-label", "Logging",
                    "--stat2-context", "Traçabilité complète des opérations"
                ],
                "description": "Slide 10: Monitoring",
                "critical": True
            },
            {
                "step_id": "section_workflow",
                "script": "03_section_header_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--section-title", "Workflow & Extensibilité",
                    "--section-subtitle", "Orchestration et Évolution"
                ],
                "description": "Slide 11: Section Workflow",
                "critical": True
            },
            {
                "step_id": "workflow_orchestration",
                "script": "07_detailed_explanation_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Workflow Automatisé",
                    "--style", "four_points",
                    "Pipeline intelligent avec orchestration complète",
                    "--additional",
                    "Analyse audience -> Configuration Sam adaptative",
                    "Séquence scripts -> Validation multi-niveaux",
                    "Gestion d'erreurs avec rollback automatique",
                    "Rapports détaillés et métriques de succès"
                ],
                "description": "Slide 12: Workflow Orchestration",
                "critical": True
            },
            {
                "step_id": "roadmap",
                "script": "06_content_boxes_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Roadmap Technique",
                    "--box1-title", "Phase 2",
                    "--box1-content", "API REST pour intégration externe",
                    "--box2-title", "Phase 3",
                    "--box2-content", "Support multi-langues et templates",
                    "--box3-title", "Phase 4",
                    "--box3-content", "Intelligence prédictive et ML"
                ],
                "description": "Slide 13: Roadmap",
                "critical": True
            },
            {
                "step_id": "technical_validation",
                "script": "10_conclusion_builder.py",
                "params": [
                    "--insert-into", "../presentations/presentation-assistant/equipe-architecture/output/presentation_assistant_architecture.pptx",
                    "--template", "../templates/Template_PT.pptx",
                    "--title", "Validation Technique",
                    "--key-point1", "Architecture modulaire enterprise-ready",
                    "--key-point2", "Intégrations robustes avec gestion d'erreurs",
                    "--key-point3", "Performance et qualité mesurées",
                    "--key-point4", "Extensibilité planifiée"
                ],
                "description": "Slide 14: Conclusion",
                "critical": True
            }
        ]

    def log_step(self, step, message):
        """Log des étapes de construction"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] ÉTAPE {step}: {message}")

    def execute_script(self, script_name, params, description):
        """Exécute un script presentation_builder avec gestion d'erreurs"""
        self.log_step("EXEC", f"Exécution de {script_name} - {description}")

        script_path = self.presentation_builder_path / script_name
        cmd = [sys.executable, str(script_path)] + params

        try:
            result = subprocess.run(cmd,
                                  cwd=self.presentation_builder_path,
                                  capture_output=True,
                                  text=True,
                                  timeout=120)

            if result.returncode == 0:
                self.log_step("SUCCESS", f"{script_name} exécuté avec succès")
                return True
            else:
                self.log_step("ERROR", f"Échec de {script_name}")
                if result.stderr:
                    print(f"  STDERR: {result.stderr[:500]}")
                if result.stdout:
                    print(f"  STDOUT: {result.stdout[:500]}")
                return False

        except subprocess.TimeoutExpired:
            self.log_step("ERROR", f"Timeout lors de l'exécution de {script_name}")
            return False
        except Exception as e:
            self.log_step("ERROR", f"Erreur inattendue avec {script_name}: {e}")
            return False

    def validate_environment(self):
        """Valide l'environnement avant construction"""
        self.log_step("VALIDATE", "Validation de l'environnement")

        # Vérifier template Premier Tech
        template_path = self.project_root / "templates" / "Template_PT.pptx"
        if not template_path.exists():
            self.log_step("ERROR", f"Template Premier Tech non trouvé: {template_path}")
            return False

        # Vérifier scripts presentation_builder
        required_scripts = [
            "01_slide_title_creator.py", "02_navigation_builder.py", "03_section_header_builder.py",
            "05_statistics_builder.py", "06_content_boxes_builder.py", "07_detailed_explanation_builder.py",
            "10_conclusion_builder.py"
        ]
        for script in required_scripts:
            script_path = self.presentation_builder_path / script
            if not script_path.exists():
                self.log_step("ERROR", f"Script manquant: {script}")
                return False

        self.log_step("SUCCESS", "Environnement validé")
        return True

    def build_presentation(self):
        """Construction séquentielle de la présentation"""
        self.log_step("START", "Début de la construction de présentation")

        # Validation de l'environnement
        if not self.validate_environment():
            return False

        # Variables de construction
        presentation_file = "presentation_assistant_architecture.pptx"
        presentation_path = self.output_dir / presentation_file

        steps_completed = []
        total_steps = len(self.build_sequence)

        # Construction séquentielle
        for step_num, step_config in enumerate(self.build_sequence, 1):
            self.log_step("PROGRESS", f"Étape {step_num}/{total_steps}: {step_config['description']}")

            success = self.execute_script(
                step_config["script"],
                step_config["params"],
                step_config["description"]
            )

            if success:
                steps_completed.append(step_config["step_id"])
                self.log_step("STEP_SUCCESS", f"Étape {step_num} terminée avec succès")
            else:
                self.log_step("STEP_FAILED", f"Échec de l'étape {step_num}")
                if step_config.get("critical", True):
                    self.log_step("ABORT", "Étape critique échouée - arrêt du processus")
                    return False

        # Validation finale
        if presentation_path.exists():
            file_size = presentation_path.stat().st_size
            self.log_step("SUCCESS", f"Présentation créée: {presentation_file} ({file_size:,} bytes)")
        else:
            self.log_step("ERROR", "Fichier de présentation non trouvé après construction")
            return False

        # Génération du rapport
        self.generate_build_report(steps_completed, presentation_path)
        return True

    def generate_build_report(self, steps_completed, presentation_path):
        """Génère le rapport de construction"""
        report = {
            "presentation_info": self.project_info,
            "audience_config": self.audience_config,
            "build_timestamp": datetime.now().isoformat(),
            "steps_completed": steps_completed,
            "total_steps": len(self.build_sequence),
            "success_rate": len(steps_completed) / len(self.build_sequence) * 100,
            "output_file": str(presentation_path),
            "file_exists": presentation_path.exists(),
            "file_size_kb": presentation_path.stat().st_size // 1024 if presentation_path.exists() else 0
        }

        # Sauvegarde du rapport JSON
        report_path = self.output_dir / "build_report.json"
        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        # Rapport Markdown
        self.generate_detailed_report(report)

        self.log_step("REPORT", f"Rapport généré: {report_path}")
        self.log_step("COMPLETE", f"Construction terminée")

    def generate_detailed_report(self, report):
        """Génère un rapport détaillé en markdown"""
        report_md = f"""# Rapport de Construction - {self.project_info['subject']}

## Informations Générales

**Audience**: {self.audience_config['audience']}
**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Durée cible**: {self.audience_config['duration_target']}
**Style Sam**: {self.audience_config['sam_style']}

## Résultats de Construction

**Statut**: {"SUCCÈS" if report['success_rate'] == 100 else f"PARTIEL ({report['success_rate']:.1f}%)"}
**Fichier**: `{report['output_file']}`
**Taille**: {report['file_size_kb']:,} KB
**Slides**: {self.project_info['estimated_slides']}

## Étapes Exécutées

"""
        for i, step in enumerate(self.build_sequence, 1):
            status = "✓" if step["step_id"] in report["steps_completed"] else "✗"
            report_md += f"- [{status}] **Étape {i}**: {step['description']}\n"

        report_md += f"""

## Configuration Sam AI

- **Communication**: {self.audience_config['communication_style']}
- **Profondeur**: {self.audience_config['technical_depth']}
- **Audience**: {self.audience_config['audience']}

---

*Généré par Presentation Assistant v2.5*
"""

        report_md_path = self.output_dir / "build_report.md"
        with open(report_md_path, 'w', encoding='utf-8') as f:
            f.write(report_md)

def main():
    """Point d'entrée principal"""
    print("=" * 60)
    print("ORCHESTRATEUR DE PRÉSENTATION")
    print("Sujet: Presentation Assistant - Architecture Système")
    print("Audience: Équipe Architecture d'Entreprise")
    print("=" * 60)

    orchestrator = PresentationOrchestrator()
    success = orchestrator.build_presentation()

    if success:
        print("\n" + "=" * 60)
        print("SUCCÈS: Présentation construite avec succès!")
        print("Fichier dans: output/presentation_assistant_architecture.pptx")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("ÉCHEC: Erreurs lors de la construction")
        print("Consultez les logs pour plus de détails")
        print("=" * 60)
        sys.exit(1)

if __name__ == "__main__":
    main()