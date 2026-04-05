# Sequential process:

```mermaid
flowchart TD
    A["User input<br/>Topic: fundamental computer networking concepts in relation to cloud computing"] --> B["Task 1: find_relevant_research<br/>Agent: degree_researcher<br/>Output: research findings"]
    B --> C["Task 2: analyze_research<br/>Agent: reporting_analyst<br/>Uses context from research<br/>Output: analysis.md"]
    C --> D["Task 3: assignment_guidance<br/>Agent: senior_advanced_software_engineer_teacher<br/>Uses context from analysis<br/>Output: assignment_guidance.md"]
    C --> E["Task 4: reporting_task<br/>Agent: reporting_analyst<br/>Uses context from analysis<br/>Output: report.md"]
    D --> F["Saved outputs"]
    E --> F
```

In a sequential workflow, each task runs in a fixed order. This makes the process easier to follow and debug, and it is probably the clearest starting point when learning how tasks and context fit together.