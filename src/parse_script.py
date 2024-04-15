# Imports
import redis
import json

# Connect to Redis
r = redis.Redis(host="redis", port=6379)

def parse_log(log_line):
    '''
    Parse a single log line and extract relevant data.
    '''

    # Split the string by spaces
    parts = log_line.split()

    # Initialize variables
    timestamp = None
    value = None
    log = None

    # Iterate to find timestamp and depth
    for i in range(len(parts)):
        if parts[i] == 'D':
            # The value is the element after 'D'
            value = str(parts[i+1])
        elif '#' in parts[i]:
            # The timestamp is the element before '#' (assuming '#' always follows the timestamp)
            timestamp = f'{parts[i-2]} {parts[i-1]}'
    
    log = f'{timestamp} {value}'
    
    return timestamp, value, log


def process_log_file(log_file_path):
    '''
    Process a log file line by line and store in Redis.
    '''

    with open(log_file_path, 'r') as file:
        for line in file:
            parsed_data = parse_log(line)
            # Store data in Redis as a JSON string
            r.lpush('parsed_logs', json.dumps(parsed_data))


def parse():
    # TODO: Add file path. Do we need to fetch the data from somewhere?
    log_file_path = 'PATH'
    # Process log file
    process_log_file(log_file_path)

    