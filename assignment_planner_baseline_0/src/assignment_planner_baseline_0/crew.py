from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool

@CrewBase
class AssignmentPlannerBaseline0():
    """AssignmentPlannerBaseline0 crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def degree_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['degree_researcher'],
            verbose=True, tools=[SerperDevTool()]
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @agent
    def senior_advanced_software_engineer_teacher(self) -> Agent:
        return Agent(
            config=self.agents_config['senior_advanced_software_engineer_teacher'],
            verbose=True
        )

    @task
    def find_relevant_research(self) -> Task:
        return Task(
            config=self.tasks_config['find_relevant_research'],
        )

    @task
    def analyze_research(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_research'],
            output_file='output/analysis.md'
        )

    @task
    def assignment_guidance(self) -> Task:
        return Task(
            config=self.tasks_config['assignment_guidance'],
            output_file='output/assignment_guidance.md'
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AssignmentPlannerBaseline0 crew"""
        manager = Agent(
            config=self.agents_config['manager'],
            allow_delegation=True
        )
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            # process=Process.sequential,
            verbose=True,
            manager_agent=manager,
            process=Process.hierarchical,
        )
