# Importing requried libraries
import random
import matplotlib.pyplot as plt
random.seed(100)

# Bayesian network structure 
network = {
    'F': [],
    'E': [],
    'A': ['F', 'E'],
    'B': ['A'],
    'C': ['A']
}

# Conditional probability tables

probabilities = {
    'F': 0.01,
    'E': 0.02,
    'A': {'00': 0.01, '01': 0.29, '10': 0.94, '11': 0.95},
    'B': {'0': 0.05, '1': 0.90},
    'C': {'0': 0.01, '1': 0.70}
}

# Function to sample from the network
# This function samples from the network given the network structure, probabilities, and evidence
# It returns a sample and the weight of the sample
# The weight is the probability of the sample given the evidence

def sample_from_network(network, probabilities, evidence):
    sample = {}
    weight = 1.0

    for node in ['F', 'E', 'A', 'B', 'C']:
        parents = network[node]

        if node in evidence:
            sample[node] = evidence[node]
            if parents:
                parent_sequence = ''.join(str(sample[parent]) for parent in parents)
                weight *= probabilities[node][parent_sequence] if evidence[node] == 1 else 1 - probabilities[node][parent_sequence]
            else:
                weight *= probabilities[node] if evidence[node] == 1 else 1 - probabilities[node]
        else:
            if parents:
                parent_sequence = ''.join(str(sample[parent]) for parent in parents)
                prob = probabilities[node][parent_sequence]
            else:
                prob = probabilities[node]

            sample[node] = 1 if random.random() < prob else 0

    return sample, weight



# Function to perform rejection sampling
# This function performs rejection sampling given the network, probabilities, evidence, and the number of samples
# It returns the accepted samples
def rejection_sampling(network, probabilities, evidence, n):
    accepted_samples = []
    runs = 0
    

    while runs < n:
        sample, _ = sample_from_network(network, probabilities, {})
        if all(sample[node] == value for node, value in evidence.items()):
            accepted_samples.append((sample, 1))
        runs += 1

    return accepted_samples


# Function to perform likelihood weighting
# This function performs likelihood weighting given the network, probabilities, evidence, and the number of samples
# It returns the samples
def likelihood_weighting(network, probabilities, evidence, n):
    samples = []
    for _ in range(n):
        samples.append(sample_from_network(network, probabilities, evidence))
    return samples



# Function to calculate the joint probability
# This function calculates the joint probability of the target values given the samples
# it simply calculates the ratio of the total weight of the samples that satisfy the target values to the total weight of all samples
def calculate_joint_probability(samples, target_values):
    total_weight = sum(weight for sample, weight in samples)
    joint_weight = sum(weight for sample, weight in samples if all(sample[node] == value for node, value in target_values.items()))

    return joint_weight / total_weight if total_weight else 0


## Function to plot the results
def plot_results(sample_sizes, results, true_value, title):
    plt.figure(figsize=(10, 6))
    plt.plot(sample_sizes, [res * 100 for res in results], marker='o', label='Estimated Probability')
    plt.axhline(y=true_value * 100, color='r', linestyle='--', label='True Probability')
    plt.xlabel('Number of Samples')
    plt.ylabel('Probability (%)')
    plt.title(title)
    plt.xscale('log')  
    plt.legend()
    plt.grid(True)
    plt.show()



def main():


    results = {
    'rejection': {
        'P(F=1|B=1)': [],
        'P(F=1|C=1)': []
    },
    'likelihood': {
        'P(F=1|B=1)': [],
        'P(F=1|C=1)': []
    }
    }

    ## True values
    true_values = {
    'P(F=1|B=1)': 0.119,
    'P(F=1|C=1)': 0.242
    }


    # Sample sizes
    sample_sizes = [10, 100, 1000, 10000]
    evidence_and_targets = [
        ({'B': 1}, {'F': 1}),
        ({'C': 1}, {'F': 1})
    ]

    # Perform rejection sampling
    print("Rejection Sampling:")
    for evidence, target in evidence_and_targets:
        target_key = f"P(F={target['F']}|{list(evidence.keys())[0]}={list(evidence.values())[0]})"
        for n in sample_sizes:
            samples_rs = rejection_sampling(network, probabilities, evidence, n)
            prob_rs = calculate_joint_probability(samples_rs, target)
            print(f"{target_key} with N={n}: {prob_rs}")
            results['rejection'][target_key].append(prob_rs)


    # Perform likelihood weighting
    print("Likelihood Weighting Sampling:")
    for evidence, target in evidence_and_targets:
        target_key = f"P(F={target['F']}|{list(evidence.keys())[0]}={list(evidence.values())[0]})"
        for n in sample_sizes:
            samples_lw = likelihood_weighting(network, probabilities, evidence, n)
            prob_lw = calculate_joint_probability(samples_lw, target)
            print(f"{target_key} with N={n}: {prob_lw}")
            results['likelihood'][target_key].append(prob_lw)

    ## Plots are present in the written part of the homeowrk
    ## STill plots can be generted for all other cases like the one specified below
    plot_results(sample_sizes, results['rejection']['P(F=1|B=1)'], true_values['P(F=1|B=1)'], 'Rejection Sampling: P(F=1|B=1)')



if __name__ == '__main__':
    main()

