import simpy
import random
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Global list to store the processing events (simulation time, baggage id)
processed_data = []

class Baggage:
    def __init__(self, id):  # Fixed constructor typo
        self.id = id

def process_baggage(env, baggage, station, proc_time_range):
    with station.request() as request:
        yield request
        processing_time = random.uniform(*proc_time_range)
        yield env.timeout(processing_time)
        print(f"Time {env.now:.2f}: Baggage {baggage.id} processed at station {station.name}")
        # Record the simulation time and baggage id when processing is complete
        processed_data.append((env.now, baggage.id))

def baggage_arrival(env, station, arrival_interval, proc_time_range):
    id = 0  # Initialize baggage id counter
    while True:
        baggage = Baggage(id)
        env.process(process_baggage(env, baggage, station, proc_time_range))
        id += 1
        # Wait for the next baggage arrival
        yield env.timeout(random.uniform(*arrival_interval))

class Station(simpy.Resource):
    def __init__(self, env, name, capacity):
        super().__init__(env, capacity=capacity)
        self.name = name

def run_simulation():
    env = simpy.Environment()
    # Create a station (Check-In Conveyor) with capacity 3
    check_in = Station(env, "Check-In Conveyor", capacity=3)
    # Define arrival and processing time ranges
    arrival_interval = (0.5, 1.5)  # Baggage arrives every 0.5 to 1.5 time units
    processing_time = (1, 3)       # Processing takes 1 to 3 time units
    # Start the baggage arrival process
    env.process(baggage_arrival(env, check_in, arrival_interval, processing_time))
    # Run the simulation for 20 time units
    env.run(until=20)

    # After simulation, plot the processing events if any data was collected
    if processed_data:
        # Unzip the recorded times and baggage IDs
        times, ids = zip(*processed_data)
        plt.scatter(times, ids)
        plt.xlabel('Simulation Time')
        plt.ylabel('Baggage ID')
        plt.title('Baggage Processing Events')
        plt.show()
    else:
        print("No processing data available to plot.")

if __name__ == "__main__":
    run_simulation()
