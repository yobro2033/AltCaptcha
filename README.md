# Altcha POW

## altcha_pow.py

This module provides a function to match a target hash by iterating and hashing the input data with an increasing counter.

### Functions

#### `hash_match(target_hash, data, algorithm="sha256")`

Matches the target hash by iterating and hashing the input data with an increasing counter.

- **Parameters:**
  - `target_hash` (str): The hash to match.
  - `data` (str): The input data to hash.
  - `algorithm` (str): Hash algorithm (default: 'sha256').

- **Returns:**
  - `dict`: A dictionary with iteration number and time taken, or `None` if no match is found.

#### `generate_hash(data, iteration, algorithm)`

Generates a hash of the input data combined with an iteration counter.

- **Parameters:**
  - `data` (str): The input data to hash.
  - `iteration` (int): The iteration counter to append to the data.
  - `algorithm` (str): Hash algorithm (e.g., 'sha256').

- **Returns:**
  - `str`: Hexadecimal hash string.

## hash_match.js

This module provides a function to match a target hash by iterating and hashing the input data with an increasing counter using JavaScript.

### Functions

#### `async hashMatch(t, e, r = "SHA-256", maxIterations = 1e6, start = 0)`

Matches the target hash by iterating and hashing the input data with an increasing counter.

- **Parameters:**
  - `t` (string): The hash to match.
  - `e` (string): The input data to hash.
  - `r` (string): Hash algorithm (default: 'SHA-256').
  - `maxIterations` (number): Maximum iterations to attempt.
  - `start` (number): Starting iteration number.

- **Returns:**
  - `Promise<object|null>`: A promise that resolves to an object with iteration number and time taken, or `null` if no match is found.

#### `async generateHash(data, iteration, algorithm)`

Generates a hash of the input data combined with an iteration counter.

- **Parameters:**
  - `data` (string): The input data to hash.
  - `iteration` (number): The iteration counter to append to the data.
  - `algorithm` (string): Hash algorithm (e.g., 'SHA-256').

- **Returns:**
  - `Promise<string>`: A promise that resolves to a hexadecimal hash string.