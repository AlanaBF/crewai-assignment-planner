# Run 1 Notes

Baseline 2 improved prompt discipline and output control, showing that stronger task instructions can make the workflow more predictable without materially increasing cost.

## What happened

Baseline hierarchical CrewAI assignment planner executed successfully with stronger prompt engineering layered on top of the structured validation introduced in baseline 1.

## Interesting observations

- Task prompts were tightened to better align agent outputs with the expected Pydantic structure.
- The research task was explicitly constrained to use fixed topic_area labels and avoid extra markdown or commentary.
- Source quality guidance was strengthened by instructing the research agent to prioritise academic papers, university materials, official cloud documentation, and standards-based sources.
- The workflow completed successfully without the schema failure seen in baseline 1.
- The hierarchical manager orchestration remained in place, but the stronger prompt constraints appeared to reduce some of the noisier output behaviour seen in earlier runs.

## Quality observations

- Outputs were more controlled and more schema-aligned than baseline 1.
- The structure of the analysis and assignment guidance remained easy to inspect and compare.
- Prompt refinements appeared to improve consistency without requiring changes to the core workflow design.
- The run still showed some source quality weaknesses in the generated outputs, with a few references remaining weaker than ideal for academic use. For example, the analysis still included sources such as ResearchGate mirrors and weaker web-style references rather than consistently stronger academic or official material
- Assignment guidance was clear and usable, but still leaned slightly generic in places rather than fully reflecting higher-education marking expectations

## Improvement ideas

- Strengthen source filtering further so the research agent excludes weak sources more aggressively
- Add a source-quality evaluator step before downstream tasks use the findings
- Introduce a comparison or scoring layer to assess output quality between baselines
- Test whether a stronger reasoning model improves academic depth and source selection
- Compare hierarchical orchestration against sequential execution now that output structure is more stable