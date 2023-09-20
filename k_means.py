from generate_samples import *
from init_centroids import *

samples, expected_clustering = generate_samples()

# [0, NUM_SAMPLES) -> [0, NUM_CLUSTERS)
computed_clustering = np.empty(NUM_SAMPLES, dtype=int)
computed_centroids = np.empty((NUM_CLUSTERS, NUM_DIMENSIONS), dtype=np.float64)


def clustering():
    for sample_id in range(0, NUM_SAMPLES):
        min_centroid_dist = np.finfo(np.float64).max
        min_cluster_id = -1
        for cluster_id in range(0, NUM_CLUSTERS):
            centroid_dist = euclidean_distance(samples[sample_id],
                                               computed_centroids[cluster_id])
            if centroid_dist < min_centroid_dist:
                min_centroid_dist = centroid_dist
                min_cluster_id = cluster_id
        computed_clustering[sample_id] = min_cluster_id


def update_centroids():
    computed_cluster_size = np.zeros(NUM_CLUSTERS, dtype=int)
    global computed_centroids
    computed_centroids = np.zeros((NUM_CLUSTERS, NUM_DIMENSIONS),
                                  dtype=np.float64)
    for sample_id in range(0, NUM_SAMPLES):
        cluster_id = computed_clustering[sample_id]
        computed_cluster_size[cluster_id] += 1
        computed_centroids[cluster_id] += samples[sample_id]
    for cluster_id in range(0, NUM_CLUSTERS):
        if computed_cluster_size[cluster_id] > 0:
            computed_centroids[cluster_id] /= computed_cluster_size[cluster_id]


def lloyds_algorithm():
    global computed_centroids
    computed_centroids = init_centroids(samples)
    clustering()
    for _ in range(0, 50):
        update_centroids()
        clustering()
    evaluate()


def evaluate():
    error_metric = 0.0
    for sample_id in range(0, NUM_SAMPLES):
        cluster_id = computed_clustering[sample_id]
        error_metric += euclidean_distance(samples[sample_id],
                                           computed_centroids[cluster_id])
    print("L1 Norm: ", error_metric)


def main():
    lloyds_algorithm()


if __name__ == "__main__":
    main()
