import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            return False  # Queue is full
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        return True

    def dequeue(self):
        if self.is_empty():
            return None  # Queue is empty
        item = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:  # Queue becomes empty after dequeuing
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return item

    def display(self):
        if self.is_empty():
            return []
        result = []
        index = self.front
        while True:
            result.append(self.queue[index])
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        return result

class ShoppingAssistantApp:
    def __init__(self, root):
        self.queue = CircularQueue(5)
        self.order_count = 0  # Counter to number the orders

        root.title("Shopping Assistant - Circular Queue")
        root.geometry("800x600")
        root.state('zoomed')  # Maximize window

        # Enqueue Frame
        self.enqueue_frame = ttk.Frame(root, padding=10)
        self.enqueue_frame.pack(pady=10)

        self.order_label = ttk.Label(self.enqueue_frame, text="Enter Order:", font=("Arial", 14))
        self.order_label.pack(side=tk.LEFT, padx=5)

        self.order_entry = ttk.Entry(self.enqueue_frame, width=30, font=("Arial", 14))
        self.order_entry.pack(side=tk.LEFT, padx=5)

        self.price_label = ttk.Label(self.enqueue_frame, text="Price:", font=("Arial", 14))
        self.price_label.pack(side=tk.LEFT, padx=5)

        self.price_entry = ttk.Entry(self.enqueue_frame, width=15, font=("Arial", 14))
        self.price_entry.pack(side=tk.LEFT, padx=5)

        self.enqueue_button = ttk.Button(self.enqueue_frame, text="Add Order", command=self.add_order)
        self.enqueue_button.pack(side=tk.LEFT, padx=5)

        # Dequeue Button
        self.dequeue_button = ttk.Button(root, text="Process Order", command=self.process_order)
        self.dequeue_button.pack(pady=20)

        # Display Orders
        self.display_label = ttk.Label(root, text="Order Queue:", font=("Arial", 16))
        self.display_label.pack(pady=10)

        self.order_list = tk.Listbox(root, width=100, height=20, font=("Arial", 14))
        self.order_list.pack(pady=10)

        # Status Bar
        self.status_label = ttk.Label(root, text="Welcome to the Shopping Assistant!", relief=tk.SUNKEN, anchor="w", font=("Arial", 12))
        self.status_label.pack(fill=tk.X, side=tk.BOTTOM)

    def update_queue_display(self):
        self.order_list.delete(0, tk.END)
        orders = self.queue.display()
        for i, order in enumerate(orders, start=1):  # Enumerate to add numbering
            self.order_list.insert(tk.END, f"{i}. {order}")

    def add_order(self):
        order = self.order_entry.get().strip()
        price = self.price_entry.get().strip()

        if not order or not price:
            messagebox.showwarning("Input Error", "Please enter both an order and a price!")
            return

        if not price.isdigit():
            messagebox.showerror("Input Error", "Price must be a valid number!")
            return

        # Add numbering and price to the order
        self.order_count += 1
        numbered_order = f"Order #{self.order_count}: {order} (Price: ${price})"

        if self.queue.enqueue(numbered_order):
            self.status_label.config(text=f"Order '{numbered_order}' added to the queue.")
            self.update_queue_display()
        else:
            messagebox.showerror("Queue Full", "Cannot add order. The queue is full!")
            self.order_count -= 1  # Roll back count if enqueue fails

        self.order_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def process_order(self):
        order = self.queue.dequeue()
        if order:
            self.status_label.config(text=f"Processed order: {order}")
            self.update_queue_display()
        else:
            messagebox.showinfo("Queue Empty", "No orders to process!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingAssistantApp(root)
    root.mainloop()
