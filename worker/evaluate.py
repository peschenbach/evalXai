import json

import torch as t
import torchmetrics as tm
import requests

def evaluateData(preds):
    # Ground truth to compare with
    target = t.tensor([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
    preds_tensor = t.tensor(preds)

    # Compute accuracy for binary classification problem
    compute_accuracy = tm.Accuracy(task="binary")
    accuracy = compute_accuracy(preds_tensor, target)

    return accuracy


predictions_ID = 13
api_url = f"http://backend:8000/api/prediction/{predictions_ID}"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    score = evaluateData(data["prediction"])
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Assuming processed_data is the result of your calculations
post_data = {"score": float(score)}
post_url = "http://backend:8000/api/score/"
response = requests.post(post_url, json=post_data)
