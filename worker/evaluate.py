import torch as t
import torchmetrics as tm
import requests

# GET predictions
# TODO use GET-API from Backend
preds = t.tensor([0, 1, 0, 1, 0, 0, 1, 1, 1, 1])


def evaluateData():
    # Ground truth to compare with
    # target = t.tensor([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    # # Compute accuracy for binary classification problem
    # compute_accuracy = tm.Accuracy(task="binary")
    # accuracy = compute_accuracy(preds, target)

    # print(f"preds: {preds}")
    # print(f"target: {target}")
    # print(f"accuracy: {accuracy}")
    return 0


api_url = "http://backend:8000/api/prediction/1"
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    score = evaluateData()
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

# Assuming processed_data is the result of your calculations
post_data = {"score": score}
post_url = "http://backend:8000/api/score/"
response = requests.post(post_url, json=post_data)

if response.status_code == 201:  # Assuming a successful POST request returns status code 201
    print("Database updated successfully")
else:
    print(f"Failed to update database. Status code: {response.status_code}")