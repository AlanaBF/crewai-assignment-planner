# CrewAI Assignment Planner

This repository documents my learning and experimentation with CrewAI as part of Ed Donner’s AI Engineer Agentic Track.

The goal is to build and iteratively improve a multi-agent assignment planner that:
- researches a topic
- analyses concepts
- generates assignment guidance
- produces a structured report

## Approach

Rather than building a single version, this project is structured as a series of iterations:

- assignment_planner_0_baseline → initial working version
- assignment_planner_1_saved_outputs → add output tracking
- assignment_planner_2_pydantic → improve structure and validation
- assignment_planner_3_evaluator → compare outputs
- assignment_planner_4_model_testing → compare models

Each version isolates a specific improvement to better understand its impact.

## Diagrams

See `/docs/diagrams` for:
- sequential workflow
- hierarchical workflow

## Why this project

The aim is to move from simple prompting to designing structured AI workflows with:
- clear responsibilities
- defined outputs
- iterative improvement
- measurable comparisons