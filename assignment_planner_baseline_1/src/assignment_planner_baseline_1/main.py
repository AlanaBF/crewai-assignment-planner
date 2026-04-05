#!/usr/bin/env python
import warnings
from datetime import datetime
from assignment_planner_baseline_1.crew import AssignmentPlannerBaseline1

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
        AssignmentPlannerBaseline1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()