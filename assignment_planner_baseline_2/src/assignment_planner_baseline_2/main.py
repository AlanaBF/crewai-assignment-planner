#!/usr/bin/env python
import warnings
from datetime import datetime
from assignment_planner_baseline_2.crew import AssignmentPlannerBaseline2

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'fundamental computer networking concepts in relation to cloud computing',
        'current_year': str(datetime.now().year)
    }

    try:
        AssignmentPlannerBaseline2().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()