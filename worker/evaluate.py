import torch as t
import torchmetrics as tm

# GET predictions
# TODO use GET-API from Backend
preds = t.tensor([0, 1, 0, 1, 0, 0, 1, 1, 1, 1])

# Ground truth to compare with
target = t.tensor([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

# Compute accuracy for binary classification problem
compute_accuracy = tm.Accuracy(task="binary")
accuracy = compute_accuracy(preds, target)

print(f"preds: {preds}")
print(f"target: {target}")
print(f"accuracy: {accuracy}")
