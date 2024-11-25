import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors

# This script was generated with help from Microsoft's Bing AI model.

# Parameters
N = 100            # Total population
grid_size = int(np.sqrt(N))  # Size of the 2D grid
beta_base = 0.3    # Base infection rate
gamma = 0.1        # Recovery rate
timesteps = 100    # Number of simulation steps
move_prob = 0.99   # Probability of moving away if neighbors are infected
vaccine_effectiveness = 0.5  # Effectiveness of the vaccine

# Initialize the population and agents' attributes
def initialize_population():
    return np.array([{
        'state': 'S',
        'susceptibility': random.uniform(0.5, 1.5),
        'movement_probability': random.uniform(0.6, 1.0),
        'asymptomatic': random.choice([True, False]),
        'contact_rate': random.randint(1, 5),
        'immune': False,
        'vaccinated': False
    } for _ in range(N)])

# Infect one random individual initially
def infect_initial_individual(population):
    initial_infected = random.randint(0, N-1)
    population[initial_infected]['state'] = 'I'
    return population

# Function to simulate one timestep
def simulate_step(population, beta_base, gamma, move_prob):
    new_population = population.copy()
    
    for i in range(N):
        agent = population[i]
        
        if agent['state'] == 'I':
            if random.random() < gamma:
                new_population[i]['state'] = 'R'
                new_population[i]['immune'] = True
            # Asymptomatic agents have a different recovery rate
            if agent['asymptomatic'] and random.random() < gamma:
                new_population[i]['state'] = 'R'
                new_population[i]['immune'] = True
        elif agent['state'] == 'S':
            effective_beta = beta_base * agent['susceptibility']
            if agent['vaccinated']:
                effective_beta *= (1 - vaccine_effectiveness)
            neighbors = [population[(i-1) % N], population[(i+1) % N]]
            if any(neighbor['state'] == 'I' for neighbor in neighbors) and random.random() < effective_beta:
                new_population[i]['state'] = 'I'
                # Move away if neighbors are infected
                safe_spots = [x for x in range(N) if new_population[x]['state'] == 'S']
                if any(neighbor['state'] == 'I' for neighbor in neighbors) and safe_spots and random.random() < move_prob:
                    move_to = random.choice(safe_spots)
                    new_population[move_to], new_population[i] = new_population[i], new_population[move_to]
    
    return new_population

# Define state colors and create color map
states = {'S': 0, 'I': 1, 'R': 2}
cmap = sns.color_palette("YlGnBu", as_cmap=True)
boundaries = [0, 1, 2, 3]
norm = mcolors.BoundaryNorm(boundaries, cmap.N, clip=True)

# Function to run the simulation
def run_simulation(simulation_function, beta_base, gamma, move_prob=None):
    population = initialize_population()
    population = infect_initial_individual(population)
    
    # Ensure only one initial infection
    initial_infected = sum(1 for agent in population if agent['state'] == 'I')
    assert initial_infected == 1, f"Expected 1 initial infection, but found {initial_infected}."
    
    S_counts, I_counts, R_counts = [], [], []

    # Plot the initial population (timestep 0)
    heat_map = np.vectorize(lambda agent: states[agent['state']])(population).reshape(grid_size, grid_size)
    plt.figure(figsize=(8, 6))
    sns.heatmap(heat_map, annot=False, cbar=True, cmap=cmap, norm=norm, xticklabels=False, yticklabels=False,
                cbar_kws={'ticks': [0, 1, 2], 'format': '%.0f'})
    plt.title(f'Timestep 0')
    colorbar = plt.gcf().axes[-1]
    colorbar.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])
    plt.show()

    for t in range(timesteps):
        population = simulation_function(population, beta_base, gamma, move_prob)
        S_counts.append(np.sum([agent['state'] == 'S' for agent in population]))
        I_counts.append(np.sum([agent['state'] == 'I' for agent in population]))
        R_counts.append(np.sum([agent['state'] == 'R' for agent in population]))

        # Debugging: Print the counts at each timestep
        print(f"Timestep {t}: S={S_counts[-1]}, I={I_counts[-1]}, R={R_counts[-1]}")

        # Plot the heatmap for each iteration
        heat_map = np.vectorize(lambda agent: states[agent['state']])(population).reshape(grid_size, grid_size)
        plt.figure(figsize=(8, 6))
        sns.heatmap(heat_map, annot=False, cbar=True, cmap=cmap, norm=norm, xticklabels=False, yticklabels=False,
                    cbar_kws={'ticks': [0, 1, 2], 'format': '%.0f'})
        plt.title(f'Timestep {t + 1}')
        
        # Add colorbar labels
        colorbar = plt.gcf().axes[-1]
        colorbar.set_yticklabels(['Susceptible', 'Infected', 'Recovered'])
        
        plt.show()
    
    return S_counts, I_counts, R_counts

# Run the simulation
S_counts, I_counts, R_counts = run_simulation(simulate_step, beta_base, gamma, move_prob=move_prob)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(range(timesteps), S_counts, label='Susceptible (S)')
plt.plot(range(timesteps), I_counts, label='Infected (I)')
plt.plot(range(timesteps), R_counts, label='Recovered (R)')
plt.xlabel('Timestep')
plt.ylabel('Number of Individuals')
#plt.title('Agent-Based Simulation of Disease Spread with Complex Behaviors')
plt.legend(loc='upper right')

plt.show()
