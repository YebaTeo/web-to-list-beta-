def create_table(data):
    # Header row
    table = "| Product Name | Product Style | Price |\n"
    # Separator row
    table += "| --- | --- | --- |\n"

    # Iterate over the data list and add rows to the table
    for item in data:
        # Extract product details with error handling
        name = item.get('Product Name', '')
        style = item.get('Product Style', '')
        price = item.get('Price', '')

        # Format the row
        row = f"| {name} | {style} | {price} |\n"
        table += row

    return table

# Read the list from a file
file_path = "C:\codingan\longchamp.txt"

with open(file_path, 'r') as file:
    # Assuming each product is separated by an empty line in the file
    products = file.read().strip().split('\n\n')

    # Process each product and extract details
    my_list = []
    for product in products:
        lines = product.strip().split('\n')
        item = {}
        for line in lines:
            key, value = line.split(":")
            item[key.strip()] = value.strip()
        my_list.append(item)

# Create the table
table = create_table(my_list)

# Print the table
print(table)
