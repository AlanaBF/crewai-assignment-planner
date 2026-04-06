# Run 1 Notes

Baseline 3 tested whether a local Ollama model could handle the same structured multi-agent workflow used in previous baselines.

## What happened

Baseline hierarchical CrewAI assignment planner executed successfully using Ollama Gemma 4 as the model provider instead of OpenAI.

## Interesting observations
- The workflow was able to run locally after configuring CrewAI to use Ollama.
- Structured outputs still completed across the same multi-agent pipeline, including research analysis, assignment guidance, and final report generation.
- This run showed that the workflow was portable to a local model environment without requiring OpenAI API usage.
- Earlier setup issues exposed some practical engineering overhead when switching providers, including model compatibility and dependency configuration.
- Quality observations
- Outputs were coherent and well structured overall.
- The assignment guidance was surprisingly confident and useful in terms of section planning and common mistakes.
- The analysis retained the four-topic structure well and remained readable throughout.
- The main weakness was source grounding and citation quality. Several references were generic placeholders rather than specific, traceable academic sources, which reduced the reliability of the output for university-level work.
- Compared with the OpenAI baselines, this output felt more generalised and synthetic — strong in shape and flow, but weaker in evidence and academic credibility.

## Improvement ideas
- Strengthen the research stage so local models are less likely to fall back to vague or placeholder references
- Add a validation or evaluator step specifically for source quality and citation completeness
- Compare the same workflow against a stronger hosted model using the same prompts and schema constraints
- Test whether a smaller local model performs similarly or whether Gemma 4 meaningfully outperforms lighter Ollama options
- Add an automated scoring rubric to compare usefulness, structure, and evidence quality across all baselines