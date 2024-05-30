import threading
import random
import time

# Function to simulate a cashier processing customers in self-checkout lanes
def self_checkout_cashier(lane_id, customers):
    print(f"Self-checkout lane {lane_id} starts processing.")
    for customer in customers:
        process_customer(lane_id, customer)
    print(f"Self-checkout lane {lane_id} has finished processing.")

# Function to simulate a cashier processing customers in a single checkout lane
def traditional_cashier(lane_id, customers):
    print(f"Cashier at lane {lane_id} starts processing.")
    for customer in customers:
        process_customer(lane_id, customer)
    print(f"Cashier at lane {lane_id} has finished processing.")

# Function to simulate processing of a customer
def process_customer(lane_id, customer):
    processing_time = random.uniform(0.5, 2.0)
    print(f"Lane {lane_id} processing customer {customer}...")
    time.sleep(processing_time)
    print(f"Lane {lane_id} finished processing customer {customer}.")

# Main function to simulate the supermarket checkout process
def main():


    num_customers = 20  # Total number of customers
    num_self_checkout_lanes = 0 # Number of self-checkout lanes
    num_traditional_lanes = 3  # Number of traditional checkout lanes

    customers = list(range(1, num_customers + 1))
    random.shuffle(customers)

    # Divide customers among self-checkout lanes
    self_checkout_customers = [customers[i::num_self_checkout_lanes] for i in range(num_self_checkout_lanes)]

    # Divide customers among traditional checkout lanes
    traditional_checkout_customers = [customers[i::num_traditional_lanes] for i in range(num_traditional_lanes)]

    threads = []

    # Start threads for self-checkout cashier
    for i in range(num_self_checkout_lanes):
        thread = threading.Thread(target=self_checkout_cashier, args=(i + 1, self_checkout_customers[i]))
        threads.append(thread)
        thread.start()

    # Start threads for traditional cashiers
    for i in range(num_traditional_lanes):
        thread = threading.Thread(target=traditional_cashier, args=(i + 1, traditional_checkout_customers[i]))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All customers have been processed.")

if __name__ == "__main__":
    main()


