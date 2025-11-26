import argparse
import sys
from agents.orchestrator import Orchestrator

def run_pipeline(topic="sample experiment", mode="demo"):
    orch = Orchestrator()
    outputs = orch.run(topic, mode=mode)

    print("\n🎉 Pipeline Executed Successfully!")
    print("--------------------------------------------------")
    print(f"📄 Paper:  {outputs['paper']}")
    print(f"📊 Slides: {outputs['slides']}")
    print("--------------------------------------------------")
    return outputs


if __name__ == "__main__":

    # If running in notebook or without args → fallback mode
    if len(sys.argv) == 1:
        print("No command-line arguments detected. Running default example...\n")
        run_pipeline("sample research topic")
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", type=str, required=True)
    parser.add_argument("--mode", type=str, default="demo")

    args = parser.parse_args()

    run_pipeline(args.topic, mode=args.mode)
