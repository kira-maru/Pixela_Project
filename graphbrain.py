import requests
from datetime import datetime
import os
from dotenv import load_dotenv
load_dotenv(".env")

# -----------------ENV VARIABLES------------------ #

PIXELA_USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("TOKEN")

# ------------------ GLOBAL ---------------------- #

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# ------------------ Class ---------------------- #


class GraphBrain:

    def __init__(self):
        self.graphs_ids = []
        self.profile_name = ""
        self.timezone = ""

    def add_graph(self, graph_id, graph_name, graph_unit, data_type, graph_color):
        """Adding a graph."""
        graph_config = {
            "id": graph_id,
            "name": graph_name,
            "unit": graph_unit,
            "type": data_type,
            "color": graph_color
        }
        graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
        response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)

        if response.status_code == 200:
            self.graphs_ids.append(graph_id)
            return True, "Graph added successfully!"
        return False, response.text

    def add_pixel(self, graph_id, year, month, day, quantity):
        """Adding pixel to a graph."""
        pixel_date = datetime(year=year, month=month, day=day)
        post_pixel = {
            "date": pixel_date.strftime("%Y%m%d"),
            "quantity": quantity
        }
        pixel_create_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}"
        response = requests.post(url=pixel_create_endpoint, json=post_pixel, headers=HEADERS)

        if response.status_code == 200:
            return True, "Pixel added successfully!"
        return False, response.text

    def update_pixel(self, graph_id, year, month, day, quantity):
        """Updating pixel."""
        pixel_date = datetime(year=year, month=month, day=day)
        update_pixel = {"quantity": quantity}
        update_pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{graph_id}/{pixel_date.strftime('%Y%m%d')}"
        response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=HEADERS)

        if response.status_code == 200:
            return True, "Pixel updated successfully!"
        return False, response.text

    def update_profile(self):
        """Updating profile info."""
        profile_info = {
            "displayName": self.profile_name,
            "timezone": self.timezone,
            "pinnedGraphID": self.graphs_ids
        }
        edit_profile_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}"
        response = requests.put(url=edit_profile_endpoint, json=profile_info, headers=HEADERS)

        if response.status_code == 200:
            return True, "Profile updated successfully!"
        return False, response.text
