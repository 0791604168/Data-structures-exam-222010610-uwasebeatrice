import tkinter as tk
from tkinter import ttk
from collections import deque


class VirtualShoppingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Shopping Assistant")
        self.root.geometry("800x600")
        self.root.config(bg="#f7f7f7")

        #  deque
        self.cart = deque()  # Using deque for LIFO processing
        self.cart_history = []  

        self.create_widgets()

    def create_widgets(self):
        # Treeview
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Categories and Items", anchor="w")

        
        electronics = self.tree.insert("", "end", text="Electronics", open=True)
        self.tree.insert(electronics, "end", text="Phones")
        self.tree.insert(electronics, "end", text="Laptops")
        clothing = self.tree.insert("", "end", text="Clothing", open=True)
        self.tree.insert(clothing, "end", text="Men's Wear")
        self.tree.insert(clothing, "end", text="Women's Wear")
        groceries = self.tree.insert("", "end", text="Groceries", open=True)
        self.tree.insert(groceries, "end", text="Fruits")
        self.tree.insert(groceries, "end", text="Vegetables")

        self.tree.pack(side="left", fill="y", padx=10, pady=10)

        # Enter Item Section
        self.item_entry_label = tk.Label(self.root, text="Enter Item Name:")
        self.item_entry_label.pack(pady=5)
        self.item_entry = tk.Entry(self.root, width=40)
        self.item_entry.pack(pady=5)

        # Add/Process Buttons
        self.add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=5)

        self.process_button = tk.Button(self.root, text="Process Order", command=self.process_order)
        self.process_button.pack(pady=5)

        # Cart
        self.cart_display_label = tk.Label(self.root, text="Cart: Empty", bg="#f7f7f7", width=50)
        self.cart_display_label.pack(pady=10)

        
        self.history_table = ttk.Treeview(self.root, columns=("No.", "Action", "Item"), show="headings", height=10)
        self.history_table.heading("No.", text="No.")
        self.history_table.heading("Action", text="Action")
        self.history_table.heading("Item", text="Item")
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
        item_name = self.get_selected_item_or_entry()
        if item_name:
            self.cart.append(item_name)  # Add the item to the cart deque
            self.cart_history.append(("Add", item_name))  # Log history
            self.update_cart_display()
            self.history_table.insert("", "end", values=(len(self.cart_history), "Add", item_name))

    def process_order(self):
        """
        Process the most recently added item (LIFO order) and remove it from the cart.
        """
        if self.cart:
            item_name = self.cart.pop()  # Remove the last item added to the cart
            self.cart_history.append(("Process", item_name))  
            self.update_cart_display()  # Update the cart display immediately
            self.history_table.insert("", "end", values=(len(self.cart_history), "Process", item_name))
        else:
            self.show_warning("Cart is empty. No items to process.")

    def get_selected_item_or_entry(self):
        """
        Retrieve the item name from the selected tree item or the entry box.
        Priority is given to the entry box if it is not empty.
        """
        item_name = self.item_entry.get().strip()
        if item_name:  # If the entry box is not empty, use it
            self.item_entry.delete(0, tk.END)  # Clear the entry box after use
            return item_name
        
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item, "text")
        self.show_warning("No item selected or entered.")
        return None

    def show_warning(self, message):
        """
        Display a warning popup with the given message.
        """
        warning_popup = tk.Toplevel(self.root)
        warning_popup.title("Warning")
        warning_label = tk.Label(warning_popup, text=message)
        warning_label.pack(padx=20, pady=20)
        ok_button = tk.Button(warning_popup, text="OK", command=warning_popup.destroy)
        ok_button.pack(pady=10)



if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualShoppingAssistant(root)
    root.mainloop()
