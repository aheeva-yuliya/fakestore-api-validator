import requests
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

class ValidationError(Enum):
    EMPTY_TITLE = "Empty title"
    NEGATIVE_PRICE = "Negative price"
    RATING_EXCEEDS_5 = "Rating exceeds 5"

@dataclass
class ValidationResult:
    product_id: int
    errors: List[ValidationError]

def validate_product(product: Dict[str, Any]) -> List[ValidationError]:
    errors = []
    
    # Check if title is empty
    if not product.get('title') or not isinstance(product['title'], str) or not product['title'].strip():
        errors.append(ValidationError.EMPTY_TITLE)
    
    # Check if price is negative
    if not isinstance(product.get('price'), (int, float)) or product['price'] < 0:
        errors.append(ValidationError.NEGATIVE_PRICE)
    
    # Check if rating.rate exceeds 5
    rating = product.get('rating', {})
    if not isinstance(rating, dict) or not isinstance(rating.get('rate'), (int, float)) or rating['rate'] > 5:
        errors.append(ValidationError.RATING_EXCEEDS_5)
    
    return errors

def test_fake_store_api() -> List[ValidationResult]:
    url = "https://fakestoreapi.com/products"
    
    try:
        response = requests.get(url)
        
        # Check HTTP status code
        if response.status_code != 200:
            print(f"Error: Received status code {response.status_code}")
            return []
        
        products = response.json()
        validation_results = []
        
        for product in products:
            errors = validate_product(product)
            if errors:
                validation_results.append(ValidationResult(
                    product_id=product.get('id', 'Unknown'),
                    errors=errors
                ))
        
        return validation_results
    
    except requests.RequestException as e:
        print(f"Error making request: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return []

def main():
    print("Testing Fake Store API...")
    validation_results = test_fake_store_api()
    
    if not validation_results:
        print("No validation errors found!")
        return
    
    print("\nValidation Errors Found:")
    print("=======================")
    
    for result in validation_results:
        print(f"\nProduct ID: {result.product_id}")
        for error in result.errors:
            print(f"- {error.value}")

if __name__ == "__main__":
    main() 