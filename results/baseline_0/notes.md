# Run 1 Notes

## What happened
Baseline hierarchical CrewAI assignment planner executed successfully.

## Interesting observations
- Manager agent attempted delegation.
- There was an early coworker/delegation naming mismatch warning before continuing.
- Research agent used Serper multiple times with targeted academic-style queries.
- Outputs were generated successfully despite some slightly messy orchestration behaviour.

## Quality observations
- Outputs were useful and coherent.
- Research was reasonably well structured.
- Assignment guidance looked practical.
- Report generation worked, though source quality and citation validation would need stronger checking in future iterations.

## Improvement ideas
- Add cleaner output saving
- Add structured validation with Pydantic
- Investigate hierarchical vs sequential behaviour more critically
- Add evaluator/comparison step