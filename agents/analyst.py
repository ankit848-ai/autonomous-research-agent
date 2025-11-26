import os
import json
import matplotlib.pyplot as plt
import re

class Analyst:

    def process(self, result, session_id):
        """Extract accuracy, save metrics + plot, return structured output."""

        stdout = result["output"]  # FIXED

        # ---- Extract accuracy ----
        match = re.search(r"Accuracy:\s*([0-9\.]+)", stdout)
        if match:
            acc = float(match.group(1))
        else:
            acc = 0.0

        # ---- Ensure artifacts folder exists ----
        folder = f"artifacts/{session_id}"
        os.makedirs(folder, exist_ok=True)

        # ---- Save accuracy plot ----
        plot_path = f"{folder}/accuracy.png"
        plt.figure(figsize=(6, 4))
        plt.bar(["Accuracy"], [acc])
        plt.title("Model Accuracy")
        plt.ylabel("Score")
        plt.savefig(plot_path)
        plt.close()

        # ---- Save metrics ----
        metrics_path = f"{folder}/metrics.json"
        with open(metrics_path, "w") as f:
            json.dump({"accuracy": acc}, f, indent=4)

        # ---- Return combined structured output ----
        return {
            "accuracy": acc,
            "plot_path": plot_path,
            "metrics_path": metrics_path
        }
