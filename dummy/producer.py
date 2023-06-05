from kafka import KafkaProducer
import random
import time

# Kafka configuration
bootstrap_servers = 'kafka:9092'
topic = 'temperature_data'

# Create Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Generate and send temperature sensor data
while True:
    # Generate random temperature between 0 and 100
    temperature = random.uniform(0, 100)

    # Convert temperature to string
    temperature_str = str(temperature)

    # Send temperature data to Kafka topic
    producer.send(topic, value=temperature_str.encode('utf-8'))

    # Print the sent temperature data
    print(f"Sent temperature: {temperature}")

    # Wait for 1 second before sending the next temperature
    time.sleep(1)