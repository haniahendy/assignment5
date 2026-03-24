import mlflow
import random

mlflow.set_experiment("assignment5")

with mlflow.start_run() as run:
    accuracy = random.uniform(0.7, 0.95)

    mlflow.log_metric("accuracy", accuracy)

    print("Accuracy:", accuracy)

    with open("run_id.txt", "w") as f:
        f.write(run.info.run_id)
