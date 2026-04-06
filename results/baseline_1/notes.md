# Run 1 Notes

Introducing structured validation improved consistency, but also exposed a trade-off between output reliability and schema brittleness. 

## What happened
Baseline hierarchical CrewAI assignment planner executed successfully using structured output validation with Pydantic.

## Interesting observations
- Pydantic validation was successfully introduced into the workflow for research, analysis and assignment guidance tasks.
- The first attempt failed because `topic_area` was too strictly constrained using an Enum, which showed that the model was returning semantically correct labels but not exact matches.
- After relaxing `topic_area` to a string, the workflow completed successfully.
- The hierarchical manager orchestration still functioned, but structured outputs made the pipeline feel more controlled than baseline 0.
- Outputs were still generated to markdown files while also being constrained by schema-based validation.

## Quality observations
- Outputs were noticeably more structured and easier to inspect.
- Research findings were more consistent and reusable because fields were explicitly defined.
- Analysis and assignment guidance were easier to compare because outputs followed a predictable shape.
- The run exposed where validation can improve reliability, but also where over-engineering schema constraints can make the workflow brittle.
- Source quality still needs improvement, as some outputs relied on weaker sources than would be ideal for academic use.

## Improvement ideas
- Tighten prompts further so agents return cleaner schema-aligned outputs first time
- Add retry / fallback handling for validation failures
- Improve source quality filtering so outputs prioritise stronger academic references
- Add evaluator/comparison step to score output quality between baselines
- Compare the same workflow using a stronger model once structure is stable