import math
import random
from utils import *

# Radius of cluster ball
RADIUS = 1e6 + 0.0


def generate_centroid(centroids, num_clusters):
    next_centroid = np.random.randint(0, NUM_CLUSTERS, NUM_DIMENSIONS)
    for cluster_id in range(0, num_clusters):
        if next_centroid == centroids[cluster_id]:
            return generate_centroid(centroids, num_clusters)
    return next_centroid


def generate_sample(pseudo_centroid):
    in_hypercube_side = 2 * int(RADIUS / math.sqrt(NUM_DIMENSIONS))
    sample = pseudo_centroid - (in_hypercube_side / 2) + random.randint(0,
                                                        in_hypercube_side)
    return sample


def generate_samples():
    pseudo_centroids = np.empty((NUM_CLUSTERS, NUM_DIMENSIONS),
                                dtype=np.float64)
    for cluster_id in range(0, NUM_CLUSTERS):
        pseudo_centroids[cluster_id] = generate_centroid(pseudo_centroids,
                                                         num_clusters=cluster_id)
    samples = np.empty((NUM_SAMPLES, NUM_DIMENSIONS), dtype=np.float64)
    expected_clustering = np.empty(NUM_SAMPLES, dtype=np.int)
    for sample_id in range(0, samples.size()):
        cluster_id = random.randint(0, NUM_CLUSTERS - 1)
        expected_clustering[sample_id] = cluster_id
        samples[sample_id] = generate_sample(pseudo_centroids[cluster_id])
        assert euclidean_distance(pseudo_centroids[cluster_id],
                                  samples[sample_id] <= RADIUS)
    return samples, expected_clustering
