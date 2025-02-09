"""
This scriptloads a product catalog and a sales record
to compute the total sales cost and shows the execution time.
"""
import json
import sys
import time


def load_json(filename):
    """Load JSON data from a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("File Error")
        sys.exit(1)


def compute_sales(prices, sales):
    """Calculate total sales cost and collect errors"""
    total = 0.0
    errors = []
    for sale in sales:
        product, quantity = sale.get("Product"), sale.get("Quantity", 0)
        if product not in prices:
            errors.append(f"Unknown product: {product}")
        elif not isinstance(quantity, (int, float)) or quantity < 0:
            errors.append(f"Invalid quantity: {quantity}")
        else:
            total += prices[product] * quantity
    return total, errors


def main():
    """Main Function"""
    if len(sys.argv) != 3:
        print("Use: python computeSales.py " +
              "priceCatalogue.json " +
              "salesRecord.json")
        sys.exit(1)

    timer = time.time()
    prices = {p["title"]: p["price"] for p in load_json(sys.argv[1])}
    sales = load_json(sys.argv[2])
    total, errors = compute_sales(prices, sales)
    cont = time.time() - timer

    output = f"Total Sales Cost: ${total:.2f}\n"
    output += f"Execution Time: {cont:.4f} seconds\n"
    if errors:
        output += "\nErrors Encountered:\n" + "\n".join(errors) + "\n"

    print(output)
    with open("SalesResults.txt", "w", encoding="utf-8") as file:
        file.write(output)


if __name__ == "__main__":
    main()
