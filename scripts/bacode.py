import keyboard
import time

# Mock product database (To replace this with a real database or API call)
product_database = {
    "0123456789123": {"name": "Hammer", "price": 15.99},
    "1234567890128": {"name": "Screwdriver", "price": 9.49},
    "2345678901234": {"name": "Wrench", "price": 12.75},
}

def lookup_product(barcode):
    """Look up a product by its barcode."""
    return product_database.get(barcode, None)

def main():
    print("Product Scanner Ready. Scan a barcode...")
    
    barcode = ""
    start_time = None
    while True:
        event = keyboard.read_event()
        if event.event_type == "down":
            if event.name == "enter":
                # Handle complete barcode
                if barcode:
                    product = lookup_product(barcode)
                    if product:
                        print(f"Product Found: {product['name']} - ${product['price']:.2f}")
                    else:
                        print(f"No product found for barcode: {barcode}")
                    barcode = ""  # Reset barcode
                else:
                    print("No barcode entered.")
            elif event.name == "esc":
                print("Exiting scanner.")
                break
            else:
                if len(event.name) == 1 and event.name.isnumeric():
                    # Append character to the barcode
                    if start_time is None:
                        start_time = time.time()
                    barcode += event.name
                elif time.time() - start_time > 1:  # Reset if delay is too long
                    barcode = ""
                    start_time = None

if __name__ == "__main__":
    main()
