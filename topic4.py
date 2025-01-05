import tkinter as tk
from tkinter import ttk, messagebox

class ShoppingAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Assistant")
        self.root.geometry("400x450")
        self.root.configure(bg="#f0f0f0") 

        self.cart = []
        self.undo_stack = []
        self.redo_stack = []

        self.create_widgets()

    def create_widgets(self):
        
        title_label = ttk.Label(self.root, text="Shopping Assistant", font=("Helvetica", 18, "bold"), foreground="black")
        title_label.pack(pady=20)

        
        self.item_entry = ttk.Entry(self.root, width=30)
        self.item_entry.pack(pady=10)

    
        add_button = ttk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        add_button.pack(pady=5)

        remove_button = ttk.Button(self.root, text="Remove from Cart", command=self.remove_from_cart)
        remove_button.pack(pady=5)

        undo_button = ttk.Button(self.root, text="Undo", command=self.undo_last_action)
        undo_button.pack(pady=5)

        redo_button = ttk.Button(self.root, text="Redo", command=self.redo_last_action)
        redo_button.pack(pady=5)

        
        columns = ('#1', '#2')
        self.cart_table = ttk.Treeview(self.root, columns=columns, show='headings', height=10)
        self.cart_table.heading('#1', text='No.')
        self.cart_table.heading('#2', text='Item')
        self.cart_table.column('#1', width=50, anchor=tk.CENTER)
        self.cart_table.column('#2', width=300, anchor=tk.W)
        self.cart_table.pack(pady=10, fill=tk.BOTH, expand=True)

    
        scrollbar = ttk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.cart_table.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.cart_table.configure(yscrollcommand=scrollbar.set)

    def add_to_cart(self):
        item = self.item_entry.get().strip()
        if item:
            self.cart.append(item)
            self.undo_stack.append(("add", item))
            self.redo_stack = []  
            self.update_cart_table()
            self.item_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Added '{item}' to cart!")
        else:
            messagebox.showerror("Error", "Please enter an item name.")

    def remove_from_cart(self):
        item = self.item_entry.get().strip()
        if item in self.cart:
            self.cart.remove(item)
            self.undo_stack.append(("remove", item))
            self.redo_stack = []  
            self.update_cart_table()
            self.item_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Removed '{item}' from cart!")
        else:
            messagebox.showerror("Error", f"'{item}' not found in cart.")

    def undo_last_action(self):
        if self.undo_stack:
            action, item = self.undo_stack.pop()
            if action == "add":
                self.cart.remove(item)
            elif action == "remove":
                self.cart.append(item)
            self.redo_stack.append((action, item))
            self.update_cart_table()
            messagebox.showinfo("Undo", f"Undid {action} of '{item}'.")
        else:
            messagebox.showinfo("Undo", "No actions to undo.")

    def redo_last_action(self):
        if self.redo_stack:
            action, item = self.redo_stack.pop()
            if action == "add":
                self.cart.append(item)
            elif action == "remove":
                self.cart.remove(item)
            self.undo_stack.append((action, item))
            self.update_cart_table()
            messagebox.showinfo("Redo", f"Redid {action} of '{item}'.")
        else:
            messagebox.showinfo("Redo", "No actions to redo.")

    def update_cart_table(self):
        
        for item in self.cart_table.get_children():
            self.cart_table.delete(item)

        
        for index, item in enumerate(self.cart, start=1):
            self.cart_table.insert("", "end", values=(index, item))


if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingAssistant(root)
    root.mainloop()
