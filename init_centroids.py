import random
from utils import *

MARKOV_CHAIN_LENGTH = 10


def d2_sampling(samples):
    closest_centroid_distance_sq = np.full(NUM_SAMPLES,
                                           np.finfo(np.float64).max)
    centroids = np.empty((NUM_CLUSTERS, NUM_DIMENSIONS), dtype=np.float64)
    centroids[0] = samples[random.randint(0, NUM_SAMPLES - 1)]
    for cluster_id in range(1, NUM_CLUSTERS):
        for sample_id in range(0, NUM_SAMPLES):
            closest_centroid_distance_sq[sample_id] = min(
                closest_centroid_distance_sq[sample_id], euclidean_distance(
                    samples[sample_id], centroids[cluster_id - 1]) ** 2)
            chosen_sample_id = np.random.choice(
                a=NUM_SAMPLES, p=closest_centroid_distance_sq / np.sum(
                    closest_centroid_distance_sq))
            centroids[cluster_id] = samples[chosen_sample_id]
    return centroids


def metropolis_hastings(samples):
    centroids = np.empty((NUM_CLUSTERS, NUM_DIMENSIONS), dtype=np.float64)
    centroids[0] = samples[random.randint(0, NUM_SAMPLES - 1)]
    for cluster_id in range(1, NUM_CLUSTERS):
        x = samples[random.randint(0, NUM_SAMPLES - 1)]
        closest_centroid_dist_x = np.finfo(np.float64).max
        for k in range(0, cluster_id - 1):
            closest_centroid_dist_x = min(closest_centroid_dist_x,
                                          euclidean_distance(x, centroids[k]))
        for j in range(1, MARKOV_CHAIN_LENGTH):
            y = samples[random.randint(0, NUM_SAMPLES - 1)]
            closest_centroid_dist_y = np.finfo(np.float64).max
            for k in range(0, cluster_id - 1):
                closest_centroid_dist_y = min(closest_centroid_dist_y,
                                              euclidean_distance(y,
                                                                 centroids[k]))
            prob_p = min(1, (closest_centroid_dist_y /
                             closest_centroid_dist_x) ** 2)
            if np.random.choice(a=2, p=[prob_p, 1 - prob_p]) == 0:
                x = y
                closest_centroid_dist_x = closest_centroid_dist_y
        centroids[cluster_id] = x
    return centroids


def init_centroids(samples):
    # return d2_sampling(samples)
    return metropolis_hastings(samples)
