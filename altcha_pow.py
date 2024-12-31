import hashlib, time

# Hash function
def hash_match(target_hash, data, algorithm="sha256", max_iterations=1_000_000, start=0):
    """
    Matches the target hash by iterating and hashing the input data with an increasing counter.

    :param target_hash: The hash to match.
    :param data: The input data to hash.
    :param algorithm: Hash algorithm (default: 'sha256').
    :param max_iterations: Maximum iterations to attempt.
    :param start: Starting iteration number.
    :return: A dictionary with iteration number and time taken, or None if no match is found.
    """
    algorithm = algorithm.lower().replace("-", "")
    start_time = int(time.time()*10000)

    for iteration in range(start, max_iterations + 1):
        computed_hash = generate_hash(data, iteration, algorithm)
        if computed_hash == target_hash:
            return {
                "number": iteration,
                "took": int(time.time()*10000) - start_time
            }

    return None  # Return None if no match is found.

def generate_hash(data, iteration, algorithm):
    """
    Generates a hash of the input data combined with an iteration counter.

    :param data: The input data to hash.
    :param iteration: The iteration counter to append to the data.
    :param algorithm: Hash algorithm (e.g., 'sha256').
    :return: Hexadecimal hash string.
    """
    combined_data = f"{data}{iteration}".encode('utf-8')
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(combined_data)
    return hash_obj.hexdigest()

# Test the hash_match function
# print(f"Hash match: {hash_match('499f774cf02c567175befd1e482c6193fa841323a21d6b66b4dd34575dfc04f8', 'CtJfpgyME29J', 'SHA-256')}")