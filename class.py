import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class RandomLoadoutApp:
    def __init__(self, root, assets_dir):
        """
        Initialize the RandomLoadoutApp with the given root window and assets directory.
        """
        self.root = root
        self.assets_dir = assets_dir
        self.list_of_items = self.load_items()
        self.images = self.load_images()
        
        self.root.geometry("800x600") 
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.generate_button = ttk.Button(self.frame, text="Generate Loadout", 
                                          command=self.generate_random_loadout)
        self.generate_button.grid(row=1, column=1, columnspan=5, pady=10, sticky="ew")
        
        self.images_frame = ttk.Frame(self.frame)
        self.images_frame.grid(row=2, column=0, columnspan=5, pady=10)

    def load_items(self):
        """
        Load the list of items from the assets directory.
        """
        items = []
        # _ is a throwaway variable for directories 
        for root, _, files in os.walk(self.assets_dir):
            for file in files:
                if file.endswith(('.png', '.jpg', '.jpeg')): # INclude PNG ? 
                    items.append(file)
        return items

    def load_images(self):
        """
        Load images from the assets directory and return a dictionary of images.
        """
        images = {}
        for item in self.list_of_items:
            image_path = os.path.join(self.assets_dir, item)
            image = Image.open(image_path)
            image = ImageTk.PhotoImage(image)
            images[item] = image
        return images

    def generate_random_loadout(self):
        """
        Generate a random loadout of 4 items and display their images.
        """
        if len(self.list_of_items) < 4:
            self.display_images([])
            return
        random_items = random.sample(self.list_of_items, 4)
        self.display_images(random_items)
    
    def display_error_message(self, message):
        """
        Display an error message in the images frame.
        """
        self.clear_images_frame()
        error_label = ttk.Label(self.images_frame, text=message, 
                                foreground="red", font=('Helvetica', 12))
        error_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

    def display_images(self, random_items):
        """
        Display the images of the given random items in the images frame.

        Some images are not the same size, maybe fix that later.
        """
        self.clear_images_frame()
        
        for i, item in enumerate(random_items):
            self.display_image(item, i)
        
        self.add_empty_spaces(len(random_items))

    def clear_images_frame(self):
        """
        Clear all widgets from the images frame.
        """
        for widget in self.images_frame.winfo_children():
            widget.destroy()

    def display_image(self, item, index):
        """
        Display the image and name of the given item at the specified index.
        """
        image_label = ttk.Label(self.images_frame, image=self.images[item])
        image_label.grid(row=0, column=index, padx=10, pady=10)
        image_label.image = self.images[item]  # Store the image to avoid garbage collection

        item_name = os.path.splitext(item)[0].replace("-", " ")
        name_label = ttk.Label(self.images_frame, text=item_name, font=('Helvetica', 12))
        name_label.grid(row=1, column=index, padx=10, pady=5)

    def add_empty_spaces(self, num_items):
        """
        Add empty spaces to the images frame to fill up to 5 columns.
        """
        for i in range(num_items, 5):
            ttk.Label(self.images_frame, text="").grid(row=0, column=i, padx=10, pady=10)
            ttk.Label(self.images_frame, text="").grid(row=1, column=i, padx=10, pady=5)

if __name__ == "__main__":
    assets_dir = './assets/ALL'
    root = tk.Tk()
    root.title("Random Loadout Selector")
    app = RandomLoadoutApp(root, assets_dir)
    root.mainloop()