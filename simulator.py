"""This simulation uses the SimPy library to model and simulate a baggage processesing system at a check-in conveyor. The purpose is to sumulate bags arriving at random intervals and being processed by a station with a limited capacitym and then to plots when each bag was processed."""

import simpy  # Used for discrete-event simulation
import random  # Random Module
import matplotlib.pyplot as plt  # Plotting

processed_data = []  # list to store bagging data


class Baggage:
    """Class to represent a persons luggage"""

    def __init__(self, id):  # initialize baggage object with an id
        self.id = id  # uniquely identifies each baggage


def process_baggage(env, baggage, station, proc_time_range):
    """Processing baggage function
    inputs:
    1. env: SimPy simulation environment
    2. baggage: The instance of the Baggage class
    3. station: The resource (i.e, check-in conveyor) where the baggage is processed.
    4. proc_time_range:"""
    with station.request() as request:
        yield request
        processing_time = random.uniform(*proc_time_range)
        yield env.timeout(processing_time)
        print(
            f"Time {env.now:.2f}: Baggage {baggage.id} processed at station {station.name}"
        )
        # Record the simulation time and baggage id when processing is complete
        processed_data.append((env.now, baggage.id))


def baggage_arrival(env, station, arrival_interval, proc_time_range):
    """Baggage arival function:
    inputs:
    1. env: SimPy simulation environment
    2. Station: The resource (i.e, check-in conveyor) where the baggage is processed.
    3. arrival_interval: A tuple representing the the time between differnt baggage arrivals
    4. proc_time_range: A tuple representing the time it takes to process each baggage.
    Outputs:
    1. A generator that yields the time until the next baggage arrives.
    """
    id = 0  # Initialize baggage id counter
    while True:
        baggage = Baggage(id)
        env.process(process_baggage(env, baggage, station, proc_time_range))
        id += 1
        # Wait for the next baggage arrival
        yield env.timeout(random.uniform(*arrival_interval))


class Station(simpy.Resource):
    """Class to represent a station (e.g., The airport check-in)"""

    def __init__(
        self, env, name, capacity
    ):  # initialize the sation object with a name and a capacity
        super().__init__(
            env, capacity=capacity
        )  # Call the parent class constuctor evv and pass the capacity
        self.name = name  # Assign the name of the station to the Station object


def run_simulation():
    """Run the simulation function:
    Inputs:
    1. None
    Outputs:
    prints the tome and baggage id after each processing is complete."""
    env = simpy.Environment()
    # Create a station (Check-In Conveyor) with capacity 3
    check_in = Station(env, "Check-In Conveyor", capacity=3)
    # Define arrival and processing time ranges
    arrival_interval = (0.5, 1.5)  # Baggage arrives every 0.5 to 1.5 time units
    processing_time = (1, 3)  # Processing takes 1 to 3 time units
    # Start the baggage arrival process
    env.process(baggage_arrival(env, check_in, arrival_interval, processing_time))
    # Run the simulation for 20 time units
    env.run(until=20)

    # After simulation, plot the processing events if any data was collected
    if processed_data:
        # Unzip the recorded times and baggage IDs
        times, ids = zip(*processed_data)
        plt.scatter(times, ids)
        plt.xlabel("Simulation Time")
        plt.ylabel("Baggage ID")
        plt.title("Baggage Processing Events")
        plt.show()
    else:
        print("No processing data available to plot.")


if __name__ == "__main__":
    run_simulation()
