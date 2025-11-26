class Designer:
    def create_plan(self, literature, topic):
        plan = {
            "topic": topic,
            "goal": f"Build a classifier on a synthetic dataset related to: {topic}",
            "model": "RandomForestClassifier",
            "model_params": {
                "n_estimators": 100,
                "max_depth": None
            },
            "metric": "accuracy",

            "dataset": "synthetic",
            "dataset_params": {
                "samples": 800,
                "features": 20,
                "classes": 3
            },

            "steps": [
                "Generate synthetic dataset",
                "Split into train/test",
                "Initialize RandomForest model",
                "Train model",
                "Evaluate accuracy",
                "Save metrics and plot"
            ]
        }
        return plan
