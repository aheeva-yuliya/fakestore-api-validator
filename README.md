# Fake Store API Linter

A Python-based API testing tool that validates product data from the Fake Store API (https://fakestoreapi.com/products).

## Overview

This tool performs automated validation of the Fake Store API's product data to identify potential defects. It checks for:

- HTTP response status code (must be 200 OK)
- Product title validation (must be non-empty string)
- Price validation (must be non-negative number)
- Rating validation (must be ≤ 5)

## Requirements

- Python 3.6 or higher
- requests library

## Installation

1. Clone this repository or download the source files
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script using Python:

```bash
python api_test.py
```

### Example Output

```
Testing Fake Store API...

Validation Errors Found:
=======================

Product ID: 1
- Empty title
- Rating exceeds 5

Product ID: 2
- Negative price
```

## Validation Rules

The script checks for the following validation rules:

1. **Title Validation**
   - Must be a non-empty string
   - Must not be whitespace-only

2. **Price Validation**
   - Must be a number (integer or float)
   - Must be non-negative

3. **Rating Validation**
   - Rating.rate must be a number
   - Rating.rate must be less than or equal to 5

## Error Handling

The script includes error handling for:
- Network connectivity issues
- Invalid JSON responses
- Unexpected HTTP status codes

## Contributing

Feel free to submit issues and enhancement requests! 