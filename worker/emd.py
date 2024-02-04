# EMD code taken from /eval/eval_utils

from scipy.spatial.distance import cdist
from scipy.ndimage import gaussian_filter
import numpy as np
import torch as t
from torch import load
from upload import XAI_Method
import pickle as pkl

from ot.lp import emd

# normal_t = [[1,0],[1,1],[1,0]]
# normal_l = [[1,0],[1,0],[1,1]]
# combined_mask = np.zeros((8,8))
# combined_mask[1:4, 1:3] = normal_t
# combined_mask[4:7, 5:7] = normal_l
# combined_mask = combined_mask.reshape((8,8))

# euclidean distance cost matrix


def create_cost_matrix(edge_length=64):
    mat = np.indices((edge_length, edge_length))
    coords = []
    for i in range(edge_length):
        for j in range(edge_length):
            coords.append((mat[0][i][j], mat[1][i][j]))
    coords = np.array(coords)
    return cdist(coords, coords)


cost_matrix_8by8 = create_cost_matrix(8)

# Scale matrix to sum to 1


def sum_to_1(mat):
    return mat / np.sum(mat)


# Calculate EMD for full, continuous-valued, attribution
# score = 1-(EMD/Dmax), where Dmax = max euclidean distance, aka sqrt(7^2 + 7^2)=9.8995 for the 8x8 data
def continuous_emd(gt_mask, attribution, n_dim=64):
    #     cost_matrix = cost_matrix_64by64
    #     if n_dim == 64:
    cost_matrix = cost_matrix_8by8

    _, log = emd(sum_to_1(gt_mask.reshape(n_dim)).astype(np.float64), sum_to_1(np.abs(
        attribution).reshape(n_dim)).astype(np.float64), cost_matrix, numItermax=200000, log=True)

    return 1 - (log['cost']/np.sqrt(n_dim + n_dim))


data_file = "linear_1d1p_0.18_uncorrelated"
data_path = "./data/" + data_file + ".pkl"
with open(data_path, 'rb') as file:
    data = pkl.load(file)

model_file = "linear_1d1p_0.18_uncorrelated_LLR_1_0"
model_path = "./ai_model/" + model_file + ".pt"
model = load(model_path)

batch_size = 100

lrp_explanations = XAI_Method(data[data_file].data[data_file].x_train[:batch_size].to(t.float), data[data_file].y_train[:batch_size], model)


emd_score = continuous_emd(data[data_file].masks_train[0], XAI_Method[0].detach().numpy())

print(continuous_emd)