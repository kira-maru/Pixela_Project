import tkinter as tk
from tkinter import messagebox


class Interface:

    def __init__(self, root, graphbrain):
        self.graphbrain = graphbrain

        # Graph frame
        self.graph_frame = tk.LabelFrame(root, text="Add Graph", padx=10, pady=10)
        self.graph_frame.pack(padx=10, pady=10)

        # Adding graph
        self.graph_id_entry = self.create_input(self.graph_frame, "Graph ID:")
        self.graph_name_entry = self.create_input(self.graph_frame, "Graph Name:")
        self.graph_unit_entry = self.create_input(self.graph_frame, "Graph Unit:")
        self.data_type_entry = self.create_input(self.graph_frame, "Data Type (float/int):")
        self.graph_color_entry = self.create_input(self.graph_frame, "Color of Pixels:")

        # Graph add button
        tk.Button(self.graph_frame, text="Add Graph", command=self.add_graph).pack(pady=5)

        self.graph_select_label = tk.Label(root, text="Enter Graph ID for Pixel Actions")
        self.graph_select_label.pack()
        self.graph_id_input = self.create_input(root, "Graph ID for Pixel:")

        # Pixel frame
        self.pixel_frame = tk.LabelFrame(root, text="Add/Update Pixel", padx=10, pady=10)
        self.pixel_frame.pack(padx=10, pady=10)

        # Add/update pixel frame
        self.year_entry = self.create_input(self.pixel_frame, "Year:")
        self.month_entry = self.create_input(self.pixel_frame, "Month:")
        self.day_entry = self.create_input(self.pixel_frame, "Day:")
        self.quantity_entry = self.create_input(self.pixel_frame, "Quantity:")

        # Pixel add button
        tk.Button(self.pixel_frame, text="Add Pixel", command=self.add_pixel).pack(pady=5)
        # Pixel update button
        tk.Button(self.pixel_frame, text="Update Pixel", command=self.update_pixel).pack(pady=5)

        # Przycisk do aktualizacji profilu
        tk.Button(root, text="Update Profile", command=self.graphbrain.update_profile).pack(pady=10)

    def create_input(self, parent, label_text):
        """Entries"""
        label = tk.Label(parent, text=label_text)
        label.pack()
        entry = tk.Entry(parent)
        entry.pack()
        return entry


    def add_graph(self):
        """Adding graph"""
        graph_id = self.graph_id_entry.get()
        graph_name = self.graph_name_entry.get()
        graph_unit = self.graph_unit_entry.get()
        data_type = self.data_type_entry.get()
        graph_color = self.graph_color_entry.get()

        success, message = self.graphbrain.add_graph(graph_id, graph_name, graph_unit, data_type, graph_color)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def add_pixel(self):
        """Adding pixel"""
        graph_id = self.graph_id_input.get()
        if graph_id == "Select Graph":
            messagebox.showwarning("Warning", "Please select a graph ID first!")
            return

        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        day = int(self.day_entry.get())
        quantity = self.quantity_entry.get()

        success, message = self.graphbrain.add_pixel(graph_id, year, month, day, quantity)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

    def update_pixel(self):
        """Updating pixel"""
        graph_id = self.graph_id_input.get()
        if graph_id == "Select Graph":
            messagebox.showwarning("Warning", "Please select a graph ID first!")
            return

        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        day = int(self.day_entry.get())
        quantity = self.quantity_entry.get()

        success, message = self.graphbrain.update_pixel(graph_id, year, month, day, quantity)
        if success:
            messagebox.showinfo("Success", message)
        else:
            messagebox.showerror("Error", message)

