from generate_samples import *
from init_centroids import *
import matplotlib.pyplot as plt

samples = np.empty((NUM_SAMPLES, NUM_DIMENSIONS), dtype=np.float64)
# expected_clustering: [0, NUM_SAMPLES) -> [0, NUM_CLUSTERS)
expected_clustering = np.empty(NUM_SAMPLES, dtype=int)

# computed_clustering: [0, NUM_SAMPLES) -> [0, NUM_CLUSTERS)
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


def lloyds_algorithm(init_method, markov_chain_length):
    global computed_centroids
    computed_centroids = init_centroids(samples, method=init_method,
                                        markov_chain_length=markov_chain_length)
    clustering()
    for _ in range(0, 50):
        update_centroids()
        clustering()
    return evaluation()


def lloyds_algorithm_multiple_runs(init_method, markov_chain_length):
    NUM_RUNS = 20
    repeated_run_metrics = np.empty(NUM_RUNS, dtype=np.float64)
    for run in range(0, NUM_RUNS):
        repeated_run_metrics[run] = lloyds_algorithm(init_method,
                                                     markov_chain_length)
    average_metric = np.mean(repeated_run_metrics)
    print(init_method, " - ", markov_chain_length, "\n\t\t\t", average_metric)
    return average_metric


def evaluation():
    l1_deviation = 0.0
    l2_deviation = 0.0
    for sample_id in range(0, NUM_SAMPLES):
        cluster_id = computed_clustering[sample_id]
        l1_deviation += euclidean_distance(samples[sample_id],
                                           computed_centroids[cluster_id])
        l2_deviation += euclidean_distance(samples[sample_id],
                                           computed_centroids[cluster_id]) ** 2
    assert l1_deviation ** 2 >= l2_deviation
    return l2_deviation


def main():
    global samples
    global expected_clustering
    samples, expected_clustering = generate_samples()
    d2_metric = lloyds_algorithm_multiple_runs(init_method=D2_SAMPLING,
                                               markov_chain_length=None)
    x_coordinates = []
    metropolis_hastings_metrics = []
    for m in range(5, 50, 5):
        x_coordinates.append(m)
        metropolis_hastings_metrics.append(
            lloyds_algorithm_multiple_runs(init_method=METROPOLIS_HASTINGS,
                                           markov_chain_length=m))

    plt.plot(x_coordinates, [d2_metric] * len(x_coordinates), marker='o',
             linestyle='-', color='g', label='D2 Sampling')
    plt.plot(x_coordinates, metropolis_hastings_metrics, marker='o',
             linestyle='-', color='r', label='Metropolis Hastings')

    plt.title("Analysing Lloyd's algorithm performance for D2 and Metropolis "
              "Hastings initialization ------ K = " + str(NUM_CLUSTERS))
    plt.xlabel('Markov Chain Length')
    plt.ylabel('L2 deviation of samples from cluster centers')

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
