import numpy as np

NUM_SAMPLES = 1000
NUM_CLUSTERS = 10
NUM_DIMENSIONS = 2

# centroid initialization methods
D2_SAMPLING = "d2_sampling"
METROPOLIS_HASTINGS = "metropolis_hastings"


def euclidean_distance(x_1, x_2):
    return np.linalg.norm(x_1 - x_2)
