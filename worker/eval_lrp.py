from captum.attr import GradientShap, Lime, LRP
import pickle as pkl
from torch import load
from emd import *

# load the generated tetris data
file_name = "linear_1d1p_0.18_uncorrelated"
path = "./data/" + file_name + ".pkl"
with open(path, 'rb') as file:
    data = pkl.load(file)

# train data of shape (N,64)
x_train = data[file_name].x_train

# train prediction labels of shape (N)
y_train = data[file_name].y_train

# test data
x_test = data[file_name].x_test

# test prediction labels
y_test = data[file_name].y_test

# train explanation ground truth masks of shape (N, 64)
masks_train = data[file_name].masks_train.shape

# load the xai model
file_name = "linear_1d1p_0.18_uncorrelated"
path = "./xai_model/" + file_name + ".pt"
model = load(
    './artifacts/tetris/training/2022-09-01-13-07/linear_0.18_uncorrelated_LLR_0_0.pt')

# taken from /xai/methods.py

# Each explanation takes:
# data: shape as was put into model (N,64)
# target: prediction target shape (N)
# model: trained model .pt object
# and optionally (here for GradSHAP and LIME, not for LRP)
# baselines: starting point for explanation computation, can be a tensor of zeroes shape (N,64)


def get_gradient_shap_attributions(data: torch.Tensor, target: torch.Tensor, model: torch.nn.Module, baselines: torch.Tensor) -> torch.tensor:
    return GradientShap(model).attribute(data.float(), target=target, baselines=baselines)


def get_lime_attributions(data: torch.Tensor, target: torch.Tensor, model: torch.nn.Module, baselines: torch.Tensor) -> torch.tensor:
    return Lime(model).attribute(data, target=target, baselines=baselines)


def get_lrp_attributions(data: torch.Tensor, target: torch.Tensor, model: torch.nn.Module) -> torch.tensor:
    return LRP(model).attribute(data, target=target)


# calculate explanations for a batch, as seen in /xai/methods.py
# alternatively do this for the whole dataset (this can be very slow!!)
batch_size = 100

lrp_explanations = get_lrp_attributions(
    data['linear_0.18_uncorrelated'].x_train[:batch_size], data['linear_0.18_uncorrelated'].y_train[:batch_size], model)

# producing the EMD score for LRP explanation of sample zero
continuous_emd(data['linear_0.18_uncorrelated'].masks_train[0],
               lrp_explanations[0].detach().numpy())

print(x_train)
