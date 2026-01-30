import csv
import os


# Simulated HTML content representing an e-commerce product page
SAMPLE_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>TechStore - Electronics Shop</title>
</head>
<body>
    <div class="product-list">
        <div class="product">
            <h2 class="product-name">Wireless Bluetooth Headphones</h2>
            <span class="price">$89.99</span>
            <span class="rating">4.5</span>
        </div>
        <div class="product">
            <h2 class="product-name">Smart Watch Pro</h2>
            <span class="price">$199.99</span>
            <span class="rating">4.8</span>
        </div>
        <div class="product">
            <h2 class="product-name">Portable Power Bank 20000mAh</h2>
            <span class="price">$45.50</span>
            <span class="rating">4.2</span>
        </div>
        <div class="product">
            <h2 class="product-name">USB-C Hub Adapter</h2>
            <span class="price">$29.99</span>
            <span class="rating">4.0</span>
        </div>
        <div class="product">
            <h2 class="product-name">Mechanical Gaming Keyboard</h2>
            <span class="price">$129.99</span>
            <span class="rating">4.7</span>
        </div>
        <div class="product">
            <h2 class="product-name">4K Webcam</h2>
            <span class="price"></span>
            <span class="rating">3.9</span>
        </div>
    </div>
</body>
</html>
"""


def extract_text_between_tags(html, start_tag, end_tag):
    """
    Extract text content between HTML opening and closing tags.
    
    Args:
        html (str): The HTML string to parse
        start_tag (str): The opening HTML tag (e.g., '<span class="price">')
        end_tag (str): The closing HTML tag (e.g., '</span>')
    
    Returns:
        str: The extracted text, or empty string if not found
    """
    try:
        # Find the position where the start tag ends
        start_pos = html.find(start_tag)
        if start_pos == -1:
            return ""
        
        # Move position to after the start tag
        start_pos = html.find('>', start_pos) + 1
        
        # Find the position of the closing tag
        end_pos = html.find(end_tag, start_pos)
        if end_pos == -1:
            return ""
        
        # Extract and return the text between tags, removing extra whitespace
        return html[start_pos:end_pos].strip()
    
    except Exception as e:
        # Handle any unexpected errors gracefully
        return ""


def parse_products(html):
    """
    Parse all product information from the HTML string.
    
    Args:
        html (str): The complete HTML document as a string
    
    Returns:
        list: A list of dictionaries, each containing product information
    """
    products = []
    
    # Split HTML by product divs to process each product separately
    # We look for '<div class="product">' as the delimiter
    product_sections = html.split('<div class="product">')
    
    # Skip the first element (it's the content before the first product)
    for section in product_sections[1:]:
        product_data = {}
        
        # Extract product name from <h2 class="product-name"> tag
        product_name = extract_text_between_tags(
            section, 
            '<h2 class="product-name">', 
            '</h2>'
        )
        
        # Extract price from <span class="price"> tag
        price = extract_text_between_tags(
            section, 
            '<span class="price">', 
            '</span>'
        )
        
        # Extract rating from <span class="rating"> tag
        rating = extract_text_between_tags(
            section, 
            '<span class="rating">', 
            '</span>'
        )
        
        # Store extracted data with proper handling of missing values
        product_data['name'] = product_name if product_name else "N/A"
        product_data['price'] = price if price else "N/A"
        product_data['rating'] = rating if rating else "N/A"
        
        # Only add product if at least the name was found
        if product_data['name'] != "N/A":
            products.append(product_data)
    
    return products


def save_to_csv(products, filename='products.csv'):
    """
    Save the extracted product data to a CSV file.
    
    Args:
        products (list): List of product dictionaries
        filename (str): Name of the CSV file to create
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Open file in write mode with proper encoding
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            
            # Define CSV column headers
            fieldnames = ['name', 'price', 'rating']
            
            # Create a CSV writer object
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header row
            writer.writeheader()
            
            # Write each product as a row in the CSV
            for product in products:
                writer.writerow(product)
        
        return True
    
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return False


def display_products(products):
    """
    Display the extracted products in a formatted table on the console.
    
    Args:
        products (list): List of product dictionaries to display
    """
    # Print a decorative header
    print("\n" + "=" * 80)
    print("EXTRACTED PRODUCT INFORMATION".center(80))
    print("=" * 80)
    
    # Check if there are any products to display
    if not products:
        print("\nNo products found!")
        return
    
    # Print table header
    print(f"\n{'Product Name':<45} {'Price':<15} {'Rating':<10}")
    print("-" * 80)
    
    # Print each product in a formatted row
    for idx, product in enumerate(products, 1):
        name = product['name']
        price = product['price']
        rating = product['rating']
        
        # Truncate long product names for better display
        if len(name) > 42:
            name = name[:42] + "..."
        
        print(f"{name:<45} {price:<15} {rating:<10}")
    
    # Print summary statistics
    print("-" * 80)
    print(f"Total Products Found: {len(products)}")
    print("=" * 80 + "\n")


def calculate_statistics(products):
    """
    Calculate and display basic statistics about the products.
    
    Args:
        products (list): List of product dictionaries
    """
    print("\n" + "=" * 80)
    print("PRODUCT STATISTICS".center(80))
    print("=" * 80 + "\n")
    
    # Count products with valid prices
    valid_prices = []
    for product in products:
        if product['price'] != "N/A":
            # Remove the dollar sign and convert to float
            try:
                price_value = float(product['price'].replace('$', ''))
                valid_prices.append(price_value)
            except ValueError:
                pass
    
    # Count products with valid ratings
    valid_ratings = []
    for product in products:
        if product['rating'] != "N/A":
            try:
                rating_value = float(product['rating'])
                valid_ratings.append(rating_value)
            except ValueError:
                pass
    
    # Display statistics
    print(f"Total Products: {len(products)}")
    print(f"Products with Price: {len(valid_prices)}")
    print(f"Products with Rating: {len(valid_ratings)}")
    
    if valid_prices:
        avg_price = sum(valid_prices) / len(valid_prices)
        max_price = max(valid_prices)
        min_price = min(valid_prices)
        print(f"\nPrice Statistics:")
        print(f"  Average Price: ${avg_price:.2f}")
        print(f"  Highest Price: ${max_price:.2f}")
        print(f"  Lowest Price: ${min_price:.2f}")
    
    if valid_ratings:
        avg_rating = sum(valid_ratings) / len(valid_ratings)
        max_rating = max(valid_ratings)
        min_rating = min(valid_ratings)
        print(f"\nRating Statistics:")
        print(f"  Average Rating: {avg_rating:.2f}")
        print(f"  Highest Rating: {max_rating:.1f}")
        print(f"  Lowest Rating: {min_rating:.1f}")
    
    print("\n" + "=" * 80 + "\n")


def main():
    """
    Main function that orchestrates the web scraping simulation.
    """
    print("\n" + "=" * 80)
    print("WEB SCRAPING SIMULATION PROJECT".center(80))
    print("E-Commerce Product Data Extractor".center(80))
    print("=" * 80 + "\n")
    
    print("Starting HTML parsing...")
    
    # Step 1: Parse the simulated HTML and extract product data
    products = parse_products(SAMPLE_HTML)
    
    print(f"Successfully parsed {len(products)} products from HTML.\n")
    
    # Step 2: Display the extracted products on console
    display_products(products)
    
    # Step 3: Calculate and display statistics
    calculate_statistics(products)
    
    # Step 4: Save the data to a CSV file
    csv_filename = 'products.csv'
    print(f"Saving data to '{csv_filename}'...")
    
    if save_to_csv(products, csv_filename):
        # Get the absolute path of the saved file
        abs_path = os.path.abspath(csv_filename)
        print(f"✓ Data successfully saved to: {abs_path}")
    else:
        print("✗ Failed to save data to CSV file.")
    
    print("\n" + "=" * 80)
    print("SCRAPING COMPLETE!".center(80))
    print("=" * 80 + "\n")


# Entry point of the program
if __name__ == "__main__":
    main()
