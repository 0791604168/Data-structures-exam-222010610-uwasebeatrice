import tkinter as tk
from tkinter import ttk
from collections import deque


class VirtualShoppingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Shopping Assistant")
        self.root.geometry("900x600")
        self.root.config(bg="#f0f0f0")

        # Initialize cart as a deque
        self.cart = deque()  # Using deque for LIFO processing
        self.cart_history = []  # Track history of actions

        self.style_widgets()
        self.create_widgets()

    def style_widgets(self):
        """
        Apply styles to widgets.
        """
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12), background="#f0f0f0")
        style.configure("TButton", font=("Helvetica", 12), padding=5)
        style.configure("Treeview.Heading", font=("Helvetica", 14, "bold"))
        style.configure("Treeview", font=("Helvetica", 12), rowheight=25)
        self.root.option_add("*Font", "Helvetica 12")

    def create_widgets(self):
        # TreeView for Hierarchical Categories and Items
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Categories and Items", anchor="w")

        # Populate TreeView with hierarchical data
        electronics = self.tree.insert("", "end", text="Electronics", open=True)
        self.tree.insert(electronics, "end", text="Phones")
        self.tree.insert(electronics, "end", text="Laptops")
        clothing = self.tree.insert("", "end", text="Clothing", open=True)
        mens_wear = self.tree.insert(clothing, "end", text="Men's Wear")
        womens_wear = self.tree.insert(clothing, "end", text="Women's Wear")
        self.tree.insert(mens_wear, "end", text="Shirts")
        self.tree.insert(mens_wear, "end", text="Trousers")
        self.tree.insert(womens_wear, "end", text="Dresses")
        self.tree.insert(womens_wear, "end", text="Skirts")
        groceries = self.tree.insert("", "end", text="Groceries", open=True)
        fruits = self.tree.insert(groceries, "end", text="Fruits")
        vegetables = self.tree.insert(groceries, "end", text="Vegetables")
        self.tree.insert(fruits, "end", text="Apples")
        self.tree.insert(fruits, "end", text="Bananas")
        self.tree.insert(vegetables, "end", text="Carrots")
        self.tree.insert(vegetables, "end", text="Broccoli")

        self.tree.pack(side="left", fill="y", padx=10, pady=10)

        self.item_entry_label = ttk.Label(self.root, text="Enter Custom Item:")
        self.item_entry_label.pack(pady=5)
        self.item_entry = tk.Entry(self.root, width=30, font=("Helvetica", 12))
        self.item_entry.pack(pady=5)

        # Add/Process Buttons
        self.add_button = ttk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=5)

        self.process_button = ttk.Button(self.root, text="Process Order", command=self.process_order)
        self.process_button.pack(pady=5)

        
        self.cart_display_label = ttk.Label(self.root, text="Cart: Empty", width=50)
        self.cart_display_label.pack(pady=10)

        
        self.history_table = ttk.Treeview(
            self.root, columns=("No.", "Action", "Item"), show="headings", height=10
        )
        self.history_table.heading("No.", text="No.")
        self.history_table.heading("Action", text="Action")
        self.history_table.heading("Item", text="Item")
        self.history_table.column("No.", width=50, anchor="center")
        self.history_table.column("Action", width=100, anchor="center")
        self.history_table.column("Item", width=300, anchor="w")
        self.history_table.pack(pady=10)

    def update_cart_display(self):
        """
        Update the cart display dynamically based on current cart contents.
        """
        if not self.cart:
            self.cart_display_label.config(text="Cart: Empty")
        else:
            items = ", ".join(self.cart)
            self.cart_display_label.config(text=f"Cart: {items}")

    def add_to_cart(self):
        """
        Add an item to the cart. Updates cart and history.
        """
        custom_item = self.item_entry.get().strip()
        selected_item = self.tree.focus()

        if custom_item:
            self.cart.append(custom_item)
            self.cart_history.append(("Add", custom_item))
            self.update_cart_display()
            self.history_table.insert("", "end", values=(len(self.cart_history), "Add", custom_item))
            self.item_entry.delete(0, tk.END)  # Clear the input field
        elif selected_item:
            item_name = self.tree.item(selected_item, "text")
            self.cart.append(item_name)
            self.cart_history.append(("Add", item_name))
            self.update_cart_display()
            self.history_table.insert("", "end", values=(len(self.cart_history), "Add", item_name))
        else:
            self.show_warning("No item selected or entered. Please select an item or enter a custom item.")

    def process_order(self):
        """
        Process all items in the cart and clear the cart.
        """
        if self.cart:
            while self.cart:  
                item_name = self.cart.pop()
                self.cart_history.append(("Process", item_name))
                self.history_table.insert("", "end", values=(len(self.cart_history), "Process", item_name))
            self.update_cart_display()  
        else:
            self.show_warning("Cart is empty. No items to process.")

    def show_warning(self, message):
        """
        Display a warning popup with the given message.
        """
        warning_popup = tk.Toplevel(self.root)
        warning_popup.title("Warning")
        warning_label = tk.Label(warning_popup, text=message, font=("Helvetica", 12), wraplength=300)
        warning_label.pack(padx=20, pady=20)
        ok_button = ttk.Button(warning_popup, text="OK", command=warning_popup.destroy)
        ok_button.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualShoppingAssistant(root)
    root.mainloop()
