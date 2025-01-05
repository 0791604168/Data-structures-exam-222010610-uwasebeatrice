import tkinter as tk
from tkinter import ttk
from collections import deque

class DoublyLinkedList:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove(self, item):
        if item in self.items and self.items[item] > 0:
            self.items[item] -= 1
            if self.items[item] == 0:  # Remove the item completely if quantity is 0
                del self.items[item]

    def __str__(self):
        return ", ".join([f"{item} x{count}" for item, count in self.items.items()])


class VirtualShoppingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Shopping Assistant")
        self.root.geometry("800x600")
        self.root.config(bg="#f7f7f7")

        # Initialize objects
        self.cart = DoublyLinkedList()
        self.cart_history = deque(maxlen=20)  # Limit the history to 20 actions

        self.create_widgets()

    def create_widgets(self):
        # Treeview for Categories and Items
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Categories and Items", anchor="w")

        # Populate Treeview with categories and items
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

        # Add/Remove Buttons
        self.add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove from Cart", command=self.remove_from_cart)
        self.remove_button.pack(pady=5)

        # Cart Display Section
        self.cart_display_label = tk.Label(self.root, text="Cart: Empty", bg="#f7f7f7", width=50)
        self.cart_display_label.pack(pady=10)

        # History Table
        self.history_table = ttk.Treeview(self.root, columns=("No.", "Action", "Item", "Quantity"), show="headings", height=10)
        self.history_table.heading("No.", text="No.")
        self.history_table.heading("Action", text="Action")
        self.history_table.heading("Item", text="Item")
        self.history_table.heading("Quantity", text="Quantity")
        self.history_table.pack(pady=10)

    def update_cart_display(self):
        if not self.cart.items:
            self.cart_display_label.config(text="Cart: Empty")
        else:
            self.cart_display_label.config(text="Cart: " + str(self.cart))

    def add_to_cart(self):
        item_name = self.get_selected_item_or_entry()
        if item_name:
            self.cart.add(item_name)
            self.cart_history.append(("Add", item_name))
            self.update_cart_display()
            self.history_table.insert("", "end", values=(len(self.cart_history), "Add", item_name, self.cart.items[item_name]))

    def remove_from_cart(self):
        item_name = self.get_selected_item_or_entry()
        if item_name in self.cart.items and self.cart.items[item_name] > 0:
            self.cart.remove(item_name)
            self.cart_history.append(("Remove", item_name))
            self.update_cart_display()
            if self.cart.items.get(item_name, 0) > 0:
                self.history_table.insert("", "end", values=(len(self.cart_history), "Remove", item_name, self.cart.items[item_name]))
            else:
                self.history_table.insert("", "end", values=(len(self.cart_history), "Remove", item_name, "Removed"))
        else:
            self.show_warning("Item not found in cart or quantity is 0.")

    def get_selected_item_or_entry(self):
        """
        Retrieve the item name from the selected tree item or the entry box.
        Priority is given to the entry box if it is not empty.
        """
        item_name = self.item_entry.get().strip()
        if item_name:  # If the entry box is not empty, use it
            self.item_entry.delete(0, tk.END)  # Clear the entry box after use
            return item_name
        # Otherwise, use the selected item in the tree
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item, "text")
        self.show_warning("No item selected or entered.")
        return None

    def show_warning(self, message):
        warning_popup = tk.Toplevel(self.root)
        warning_popup.title("Warning")
        warning_label = tk.Label(warning_popup, text=message)
        warning_label.pack(padx=20, pady=20)
        ok_button = tk.Button(warning_popup, text="OK", command=warning_popup.destroy)
        ok_button.pack(pady=10)


# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualShoppingAssistant(root)
    root.mainloop()




    import tkinter as tk
from tkinter import ttk
from collections import deque

class DoublyLinkedList:
    def __init__(self):
        self.items = {}

    def add(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def remove(self, item):
        if item in self.items:
            self.items[item] -= 1
            if self.items[item] <= 0:  # Remove item entirely if quantity is zero
                del self.items[item]

    def __str__(self):
        return ", ".join([f"{item} x{count}" for item, count in self.items.items()])


class VirtualShoppingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Shopping Assistant")
        self.root.geometry("800x600")
        self.root.config(bg="#f7f7f7")

        # Initialize objects
        self.cart = DoublyLinkedList()
        self.cart_history = deque(maxlen=20)  # Limit the history to 20 actions

        self.create_widgets()

    def create_widgets(self):
        # Treeview for Categories and Items
        self.tree = ttk.Treeview(self.root)
        self.tree.heading("#0", text="Categories and Items", anchor="w")

        # Populate Treeview with categories and items
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

        # Add/Remove Buttons
        self.add_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove from Cart", command=self.remove_from_cart)
        self.remove_button.pack(pady=5)

        # Cart Display Section
        self.cart_display_label = tk.Label(self.root, text="Cart: Empty", bg="#f7f7f7", width=50)
        self.cart_display_label.pack(pady=10)

        # History Table
        self.history_table = ttk.Treeview(self.root, columns=("No.", "Action", "Item", "Quantity"), show="headings", height=10)
        self.history_table.heading("No.", text="No.")
        self.history_table.heading("Action", text="Action")
        self.history_table.heading("Item", text="Item")
        self.history_table.heading("Quantity", text="Quantity")
        self.history_table.pack(pady=10)

    def update_cart_display(self):
        if not self.cart.items:
            self.cart_display_label.config(text="Cart: Empty")
        else:
            self.cart_display_label.config(text="Cart: " + str(self.cart))

    def add_to_cart(self):
        item_name = self.get_selected_item_or_entry()
        if item_name:
            self.cart.add(item_name)
            self.cart_history.append(("Add", item_name))
            self.update_cart_display()
            self.history_table.insert("", "end", values=(len(self.cart_history), "Add", item_name, self.cart.items[item_name]))

    def remove_from_cart(self):
        item_name = self.get_selected_item_or_entry()
        if item_name in self.cart.items:
            self.cart.remove(item_name)
            self.cart_history.append(("Remove", item_name))
            self.update_cart_display()
            if item_name in self.cart.items:
                self.history_table.insert("", "end", values=(len(self.cart_history), "Remove", item_name, self.cart.items[item_name]))
            else:
                self.history_table.insert("", "end", values=(len(self.cart_history), "Remove", item_name, "Removed"))
        else:
            self.show_warning("Item not found in cart or already removed.")

    def get_selected_item_or_entry(self):
        """
        Retrieve the item name from the selected tree item or the entry box.
        Priority is given to the entry box if it is not empty.
        """
        item_name = self.item_entry.get().strip()
        if item_name:  # If the entry box is not empty, use it
            self.item_entry.delete(0, tk.END)  # Clear the entry box after use
            return item_name
        # Otherwise, use the selected item in the tree
        selected_item = self.tree.focus()
        if selected_item:
            return self.tree.item(selected_item, "text")
        self.show_warning("No item selected or entered.")
        return None

    def show_warning(self, message):
        warning_popup = tk.Toplevel(self.root)
        warning_popup.title("Warning")
        warning_label = tk.Label(warning_popup, text=message)
        warning_label.pack(padx=20, pady=20)
        ok_button = tk.Button(warning_popup, text="OK", command=warning_popup.destroy)
        ok_button.pack(pady=10)


# Create and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualShoppingAssistant(root)
    root.mainloop()



