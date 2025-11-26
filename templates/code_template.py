"""
Auto-generated experiment template.
This file is NOT executed directly.
The CoderExecutor agent generates a dynamic experiment.py based on the Designer plan.
This template exists only as a reference/example.
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def run_experiment():
    # Example static dataset
    X, y = make_classification(
        n_samples=500,
        n_features=20,
        n_classes=2,
        random_state=42
    )

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Example model
    clf = RandomForestClassifier(n_estimators=20, random_state=42)
    clf.fit(X_train, y_train)

    # Accuracy output (for demo only)
    acc = clf.score(X_test, y_test)
    print("Accuracy:", acc)
