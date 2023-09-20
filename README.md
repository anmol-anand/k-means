# K-means

## Overview

This project contains the implementation of Lloyd's k-means algorithm, which is used for clustering data into K distinct clusters.

## Experiment Details

Lloyd's algorithm is run using two different initialization methods of cluster centroids: D2 sampling initialization (green line plots) and Metropolis Hastings initialization (red line plots). The experiment is conducted with three different values of K: 10, 100, and 500. When using Metropolis Hastings initialization, the experiment varies in terms of the lengths of the Markov chain, which is represented on the x-axis of the plots.

## Results

The results reveal that the D2 Sampling approach consistently outperforms Metropolis Hastings in terms of accuracy. Performance is measured on the y-axis, which represents the sum of squared distances of samples from their respective cluster centroids. Smaller values on the y-axis indicate better performance.

<p align="center">
  <img src="result%20plots/K_10.png" alt="Figure 1: K=10">
  <br>
  Experiment 1: K=10
</p>

<p align="center">
  <img src="result%20plots/K_100.png" alt="Figure 1: K=100">
  <br>
  Experiment 2: K=100
</p>

<p align="center">
  <img src="result%20plots/K_500.png" alt="Figure 1: K=500">
  <br>
  Experiment 3: K=500
</p>

## Running the Code

To run the code, follow these steps:

1. Clone this repository locally
2. Change directory to the cloned repository
3. Set the desired value of K by modifying NUM_CLUSTERS variable in utils.py
4. Run the python script k_means.py

Once the script completes, a plot like the ones above will be generated.

Note: You might have to install the necessary dependencies like NumPy, Matplotlib, etc.
