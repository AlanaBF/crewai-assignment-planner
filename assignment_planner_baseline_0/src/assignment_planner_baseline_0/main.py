#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from assignment_planner_baseline_0.crew import AssignmentPlannerBaseline0

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
        AssignmentPlannerBaseline0().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run()