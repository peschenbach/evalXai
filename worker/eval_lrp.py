import torch
from captum.attr import GradientShap, Lime, LRP
import pickle as pkl
from torch import load
from emd import *

# load the generated tetris data
data_file = "linear_1d1p_0.18_uncorrelated"
data_path = "/data/" + data_file + ".pkl"
with open(data_path, 'rb') as file:
    data = pkl.load(file)

# train data of shape (N,64)
x_train = data[data_file].x_train

# train prediction labels of shape (N)
# y_train = data[data_file].y_train

# test data
# x_test = data[data_file].x_test

# test prediction labels
# y_test = data[data_file].y_test

# train explanation ground truth masks of shape (N, 64)
# masks_train = data[data_file].masks_train.shape

# load model
model_file = "linear_1d1p_0.18_uncorrelated_LLR_1_0"
model_path = "./ai_model/" + model_file + ".pt"
model = load(model_path)

# taken from /xai/methods.py

# Each explanation takes:
# data: shape as was put into model (N,64)
# target: prediction target shape (N)
# model: trained model .pt object
# and optionally (here for GradSHAP and LIME, not for LRP)


def get_lrp_attributions(data: torch.Tensor, target: torch.Tensor, model: torch.nn.Module) -> torch.tensor:
    return LRP(model).attribute(data, target=target)


# calculate explanations for a batch, as seen in /xai/methods.py
# alternatively do this for the whole dataset (this can be very slow!!)
batch_size = 100

# Convert input data to the desired data type
# Assuming the desired data type is float32
x_train = data[data_file].x_train.to(torch.float32)

# Reshape your input data to match the expected shape [batch_size, channels, height, width]
# x_train_reshaped = x_train.view(-1, 1, 8, 8)  # Assuming your data is 8x8


# lrp_explanations = get_lrp_attributions(
#     x_train_reshaped[:batch_size][:batch_size], data[data_file].y_train[:batch_size], model)

lrp_explanations = get_lrp_attributions(
    x_train[:batch_size].to(t.float).reshape(100,1,8,8), data[data_file].y_train[:batch_size], model)

c = continuous_emd(data[data_file].masks_test[0], lrp_explanations[0].detach().numpy())
print(c)

# lrp_explanations = get_lrp_attributions(
#     data[data_file].x_train[:batch_size], data[data_file].y_train[:batch_size], model)

# producing the EMD score for LRP explanation of sample zero
# emd_score = continuous_emd(data[data_file].masks_train[0],
#                            lrp_explanations[0].detach().numpy())

# print(lrp_explanations)
