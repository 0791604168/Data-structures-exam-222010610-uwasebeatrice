import tkinter as tk
from tkinter import messagebox
from tkinter import font

# Insertion Sort Function
def insertion_sort(data):
    for i in range(1, len(data)):
        current_item = data[i]
        j = i - 1
        while j >= 0 and data[j]['priority'] > current_item['priority']:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = current_item
    return data

# Add Product to the List
def add_product():
    product_name = selected_product.get()
    priority = entry_priority.get()
    if not product_name or not priority.isdigit():
        messagebox.showerror("Input Error", "Please select a valid product and enter a valid priority (numeric).")
        return
    priority = int(priority)
    products_list.append({"product": product_name, "priority": priority})
    update_product_list()

# Update Listbox to display products
def update_product_list():
    listbox.delete(0, tk.END)
    for product in products_list:
        listbox.insert(tk.END, f"{product['product']} - Priority: {product['priority']}")

# Sort Products
def sort_products():
    global products_list
    sorted_products = insertion_sort(products_list)
    update_product_list()
    messagebox.showinfo("Sort Complete", "Products have been sorted by priority.")

# GUI Setup
root = tk.Tk()
root.title("Shopping Assistant - Product Priority Sorting")

# Maximize the window to fit the screen, without hiding the window controls
root.state('zoomed')  # This will maximize the window without hiding controls

# Set the background color for the window
root.configure(bg='#f4f4f9')

# Create a list to store products
products_list = []

# Fonts
header_font = font.Font(family="Helvetica", size=16, weight="bold")
label_font = font.Font(family="Arial", size=12)
entry_font = font.Font(family="Verdana", size=10)
button_font = font.Font(family="Arial", size=12, weight="bold")

# List of 10 basic products in Rwanda
product_options = [
    "Rice", "Beans", "Maize flour", "Sugar", "Salt", 
    "Cooking oil", "Milk", "Tea", "Soap", "Water"
]

# Create and place widgets
frame = tk.Frame(root, bg="#f4f4f9")
frame.pack(padx=20, pady=20)

# Product Name Label and OptionMenu
label_name = tk.Label(frame, text="Select Product:", font=label_font, bg="#f4f4f9")
label_name.grid(row=0, column=0, padx=10, pady=5, sticky='e')

# OptionMenu for product selection
selected_product = tk.StringVar()
selected_product.set(product_options[0])  # Default value

product_menu = tk.OptionMenu(frame, selected_product, *product_options)
product_menu.config(font=entry_font, width=30)
product_menu.grid(row=0, column=1, padx=10, pady=5)

# Product Priority Label and Entry
label_priority = tk.Label(frame, text="Priority (Numeric):", font=label_font, bg="#f4f4f9")
label_priority.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_priority = tk.Entry(frame, font=entry_font, width=30)
entry_priority.grid(row=1, column=1, padx=10, pady=5)

# Add Product Button
button_add = tk.Button(frame, text="Add Product", font=button_font, bg="#4CAF50", fg="white", relief="flat", command=add_product)
button_add.grid(row=2, column=0, columnspan=2, pady=10, ipady=5)

# Sort Products Button
button_sort = tk.Button(frame, text="Sort by Priority", font=button_font, bg="#2196F3", fg="white", relief="flat", command=sort_products)
button_sort.grid(row=3, column=0, columnspan=2, pady=10, ipady=5)

# Title Label
title_label = tk.Label(root, text="Product List", font=header_font, bg="#f4f4f9", fg="#333")
title_label.pack(pady=10)

# Listbox to display products
listbox = tk.Listbox(root, font=entry_font, width=50, height=10, bg="#ffffff", fg="#333", selectbackground="#ffcc00", selectforeground="black")
listbox.pack(padx=20, pady=10)

# Start the GUI loop
root.mainloop()
