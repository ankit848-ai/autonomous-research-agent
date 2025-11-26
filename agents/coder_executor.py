import subprocess
import os
import json
from textwrap import dedent

class CoderExecutor:

    def generate_code(self, plan, session_id):
        """Generate experiment.py dynamically based on the plan."""
        
        code_path = f"artifacts/{session_id}/experiment.py"

        samples = plan["dataset_params"]["samples"]
        features = plan["dataset_params"]["features"]
        classes = plan["dataset_params"]["classes"]

        n_estimators = plan["model_params"]["n_estimators"]

        code = f"""
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Generate synthetic dataset
X, y = make_classification(
    n_samples={samples},
    n_features={features},
    n_classes={classes},
    random_state=42
)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
clf = RandomForestClassifier(n_estimators={n_estimators}, random_state=42)
clf.fit(X_train, y_train)

# Evaluate
acc = clf.score(X_test, y_test)
print("Accuracy:", acc)
"""

        with open(code_path, "w") as f:
            f.write(dedent(code))

        return {"file": code_path}

    def execute_code(self, code_info, session_id):
        """Run experiment.py and capture output."""
        
        path = code_info["file"]

        run = subprocess.run(
            ["python", path],
            capture_output=True,
            text=True
        )

        result = {
            "output": run.stdout,
            "errors": run.stderr,
            "returncode": run.returncode,
        }

        # Save logs
        log_path = f"artifacts/{session_id}/run_logs.txt"
        with open(log_path, "w") as f:
            f.write("STDOUT:\n" + run.stdout + "\n\n")
            f.write("STDERR:\n" + run.stderr + "\n\n")

        return result
