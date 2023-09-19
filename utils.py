import numpy as np

NUM_SAMPLES = 1e3
NUM_CLUSTERS = 10
NUM_DIMENSIONS = 2


def euclidean_distance(x_1, x_2):
    return np.linalg.norm(x_1 - x_2)
