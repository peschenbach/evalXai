import pickle as pkl


# load the generated tetris data
file_name = "linear_1d1p_0.18_uncorrelated"
path = "./data/" + file_name + ".pkl"
with open(path, 'rb') as file:
    data = pkl.load(file)

# train data of shape (N,64)
x_train = data[file_name].x_train

# train explanation ground truth masks of shape (N, 64)
masks_train = data[file_name].masks_train.shape

print(x_train)
