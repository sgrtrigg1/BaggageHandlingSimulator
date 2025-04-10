# Baggage Handling Simulator

## Overview

This project simulate a simplified baggage handling system using discrete-event simulation framework **SimPy**. The simulatiion models key componments like check-in, conveyor belts, and processing stations.

## Objectives

- **Demonstrate System Modeling.** Represent the real-life flow of baggage processing and handling.
**Lean Discrete-Event Simulation** Use SimPy to simulate randomized processes in a logistics context.
**Provide a Foundation for Future Extensions** Possible next steps include multi-station modeling, visualizing simulation data, and incorporating error-handling for system failures.

## Key Features

- **Baggage Object:** Represents individual lugggage items.
- **Processing Stations** Simulate check-in or sorting stations with limited capacity.
- **Randomized Timing** Uses Python's 'random' module to model variable arrival and processing times.
- **Event Logging:** Prints simulation events to the terminal for analysis.#

##Getting Started

### Preequisites

- Python 3.x
- [SimPy](https://simpy.readthedocs.io/) library

### Installation

1. Clone the repository (if applicable):
'''bash
git clone https://github.com/sgrtrigg1/BaggageHandlingSimulator.git
'''
2. Navigate into the project folder:
'''bash
cd BaggageHandlingSimulator
'''
3. Install SimPy using pip:
'''bash
pip install simpy
'''

### Running the Simulation

To start the simulation:
'''bash
python simulator.py