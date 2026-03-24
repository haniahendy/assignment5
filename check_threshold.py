import mlflow

with open("model_info.txt", "r") as f:
    run_id = f.read().strip().replace("RUN_ID=", "")

client = mlflow.tracking.MlflowClient()
run = client.get_run(run_id)

accuracy = run.data.metrics.get("accuracy", 0)

print("Accuracy:", accuracy)

if accuracy < 0.85:
    raise Exception("Model accuracy below threshold ")
else:
    print("Model passed threshold ")
