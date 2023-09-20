# K-means

## Overview

This project contains the implementation of Lloyd's k-means algorithm, which is used for clustering data into K distinct clusters.

## Experiment Details

The Lloyd's algorithm is run using two different initialization methods: D2 sampling initialization (green line plots) and Metropolis Hastings initialization (red line plots) of cluster centroids. The experiment is conducted with three different values of K: 10, 100, and 500. When using Metropolis Hastings initialization, the experiment varies in terms of the lengths of the Markov chain, which is represented on the x-axis of the plots.

## Results

The results reveal that the D2 Sampling approach consistently outperforms Metropolis Hastings in terms of accuracy. Performance is measured on the y-axis, which represents the sum of squared distances of samples from their respective cluster centroids. Smaller values on the y-axis indicate better performance.

### Experiment 1: K=10

![Figure 1: K=10](result%20plots/K_10.png)

### Experiment 2: K=100

![Figure 1: K=10](result%20plots/K_100.png)

### Experiment 1: K=500

![Figure 1: K=500](result%20plots/K_500.png)

