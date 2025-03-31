import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.constants import *

class ImageCombinerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Combiner - Catppuccin Mocha")
        self.root.geometry("800x600")
        
        # Catppuccin Mocha color palette
        self.colors = {
            "base": "#1e1e2e",
            "mantle": "#181825",
            "crust": "#11111b",
            "text": "#cdd6f4",
            "subtext1": "#bac2de",
            "subtext0": "#a6adc8",
            "overlay2": "#9399b2",
            "overlay1": "#7f849c",
            "overlay0": "#6c7086",
            "surface2": "#585b70",
            "surface1": "#45475a",
            "surface0": "#313244",
            "blue": "#89b4fa",
            "lavender": "#b4befe",
            "sapphire": "#74c7ec",
            "sky": "#89dceb",
            "teal": "#94e2d5",
            "green": "#a6e3a1",
            "yellow": "#f9e2af",
            "peach": "#fab387",
            "maroon": "#eba0ac",
            "red": "#f38ba8",
            "mauve": "#cba6f7",
            "pink": "#f5c2e7",
            "flamingo": "#f2cdcd",
            "rosewater": "#f5e0dc"
        }
        
        # Configure theme
        self.configure_theme()
        
        # Variables
        self.image_paths = []
        self.output_path = ""
        
        # GUI Elements
        self.create_widgets()
    
    def configure_theme(self):
        self.root.configure(bg=self.colors["base"])
        
        # Custom style configuration
        style = ttk.Style()
        style.theme_use("clam")
        
        # Configure colors
        style.configure(".", 
                      background=self.colors["base"],
                      foreground=self.colors["text"],
                      fieldbackground=self.colors["surface0"],
                      selectbackground=self.colors["blue"],
                      selectforeground=self.colors["crust"],
                      insertcolor=self.colors["text"],
                      troughcolor=self.colors["surface1"],
                      highlightthickness=0)
        
        # Frame styles
        style.configure("TLabelframe", 
                      background=self.colors["mantle"],
                      foreground=self.colors["text"],
                      bordercolor=self.colors["surface1"])
        style.configure("TLabelframe.Label", 
                      background=self.colors["mantle"],
                      foreground=self.colors["lavender"])
        
        # Button styles
        style.configure("TButton",
                      background=self.colors["surface0"],
                      foreground=self.colors["text"],
                      bordercolor=self.colors["surface1"],
                      focusthickness=0,
                      focuscolor=self.colors["surface0"])
        style.map("TButton",
                background=[("active", self.colors["surface1"])])
        
        # Entry styles
        style.configure("TEntry",
                      fieldbackground=self.colors["surface0"],
                      foreground=self.colors["text"],
                      insertcolor=self.colors["text"],
                      bordercolor=self.colors["surface1"],
                      lightcolor=self.colors["surface0"],
                      darkcolor=self.colors["surface0"])
        
        # Combobox styles
        style.configure("TCombobox",
                      selectbackground=self.colors["blue"],
                      selectforeground=self.colors["crust"])
        
        # Scrollbar styles
        style.configure("Vertical.TScrollbar",
                      background=self.colors["surface0"],
                      troughcolor=self.colors["mantle"],
                      bordercolor=self.colors["mantle"],
                      arrowcolor=self.colors["text"])
        
        # Progressbar styles
        style.configure("Horizontal.TProgressbar",
                      background=self.colors["mauve"],
                      troughcolor=self.colors["mantle"],
                      bordercolor=self.colors["mantle"],
                      lightcolor=self.colors["mauve"],
                      darkcolor=self.colors["mauve"])
    
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Image selection frame
        select_frame = ttk.LabelFrame(
            main_frame, 
            text="Image Selection", 
            padding=10
        )
        select_frame.pack(fill=tk.X, pady=5)
        
        # Button frame
        btn_frame = ttk.Frame(select_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        # Add images button
        self.add_btn = ttk.Button(
            btn_frame,
            text="Add Images",
            command=self.add_images,
            style="TButton"
        )
        self.add_btn.pack(side=tk.LEFT, padx=5)
        
        # Remove selected button
        self.remove_btn = ttk.Button(
            btn_frame,
            text="Remove Selected",
            command=self.remove_selected,
            style="TButton"
        )
        self.remove_btn.pack(side=tk.LEFT, padx=5)
        
        # Clear all button
        self.clear_btn = ttk.Button(
            btn_frame,
            text="Clear All",
            command=self.clear_all,
            style="TButton"
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Listbox to display selected images
        list_frame = ttk.Frame(main_frame)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.listbox = tk.Listbox(
            list_frame,
            selectmode=tk.EXTENDED,
            height=10,
            bg=self.colors["surface0"],
            fg=self.colors["text"],
            selectbackground=self.colors["blue"],
            selectforeground=self.colors["crust"],
            highlightthickness=0,
            relief=tk.FLAT,
            font=("Segoe UI", 10)
        )
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbar for listbox
        scrollbar = ttk.Scrollbar(
            list_frame,
            orient=tk.VERTICAL,
            command=self.listbox.yview
        )
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        
        # Options Frame
        options_frame = ttk.LabelFrame(
            main_frame, 
            text="Combination Options", 
            padding=10
        )
        options_frame.pack(fill=tk.X, pady=5)
        
        # Spacing option
        spacing_frame = ttk.Frame(options_frame)
        spacing_frame.pack(fill=tk.X, pady=5)
        ttk.Label(spacing_frame, text="Spacing (px):").pack(side=tk.LEFT, padx=5)
        self.spacing_var = tk.IntVar(value=0)
        self.spacing_spin = ttk.Spinbox(
            spacing_frame,
            from_=0,
            to=100,
            textvariable=self.spacing_var,
            width=5
        )
        self.spacing_spin.pack(side=tk.LEFT)
        
        # Alignment option
        align_frame = ttk.Frame(options_frame)
        align_frame.pack(fill=tk.X, pady=5)
        ttk.Label(align_frame, text="Alignment:").pack(side=tk.LEFT, padx=5)
        self.alignment_var = tk.StringVar(value="center")
        align_menu = ttk.Combobox(
            align_frame,
            textvariable=self.alignment_var,
            values=["left", "center", "right"],
            state="readonly",
            width=8
        )
        align_menu.pack(side=tk.LEFT)
        
        # Output file option
        output_frame = ttk.Frame(options_frame)
        output_frame.pack(fill=tk.X, pady=5)
        ttk.Label(output_frame, text="Output File:").pack(side=tk.LEFT, padx=5)
        self.output_entry = ttk.Entry(output_frame, width=40)
        self.output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(
            output_frame,
            text="Browse",
            command=self.select_output,
            width=8
        ).pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            main_frame,
            orient=tk.HORIZONTAL,
            length=200,
            mode='determinate'
        )
        self.progress.pack(fill=tk.X, pady=10)
        
        # Combine button
        self.combine_btn = ttk.Button(
            main_frame,
            text="Combine Images",
            command=self.combine_images,
            style="TButton"
        )
        self.combine_btn.pack(pady=10)

    def add_images(self):
        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if files:
            for file in files:
                if file not in self.image_paths:
                    self.image_paths.append(file)
                    self.listbox.insert(tk.END, os.path.basename(file))

    def remove_selected(self):
        selected = self.listbox.curselection()
        for index in selected[::-1]:
            self.listbox.delete(index)
            del self.image_paths[index]

    def clear_all(self):
        self.listbox.delete(0, tk.END)
        self.image_paths = []

    def select_output(self):
        output_file = filedialog.asksaveasfilename(
            title="Save Combined Image As",
            defaultextension=".jpg",
            filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png"), ("All Files", "*.*")]
        )
        if output_file:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, output_file)

    def combine_images(self):
        if not self.image_paths:
            messagebox.showerror("Error", "No images selected!")
            return
        
        output_path = self.output_entry.get()
        if not output_path:
            messagebox.showerror("Error", "Please specify an output file!")
            return
        
        spacing = self.spacing_var.get()
        alignment = self.alignment_var.get()
        
        try:
            self.progress["value"] = 0
            self.root.update_idletasks()
            
            # Open all images and convert to RGB if necessary
            images = []
            for i, path in enumerate(self.image_paths):
                img = Image.open(path)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                images.append(img)
                self.progress["value"] = (i + 1) / len(self.image_paths) * 50
                self.root.update_idletasks()
            
            # Calculate total height and max width
            total_height = sum(img.height for img in images) + spacing * (len(images) - 1)
            max_width = max(img.width for img in images)
            
            # Create new blank image
            combined = Image.new('RGB', (max_width, total_height), (255, 255, 255))
            
            # Paste images vertically
            y_offset = 0
            for i, img in enumerate(images):
                if alignment == "left":
                    x_offset = 0
                elif alignment == "center":
                    x_offset = (max_width - img.width) // 2
                elif alignment == "right":
                    x_offset = max_width - img.width
                else:
                    x_offset = 0
                
                combined.paste(img, (x_offset, y_offset))
                y_offset += img.height + spacing
                
                self.progress["value"] = 50 + (i + 1) / len(images) * 50
                self.root.update_idletasks()
            
            # Save the combined image
            combined.save(output_path)
            self.progress["value"] = 100
            messagebox.showinfo(
                "Success", 
                f"Successfully combined {len(images)} images into:\n{output_path}"
            )
        
        except Exception as e:
            messagebox.showerror(
                "Error", 
                f"An error occurred:\n{str(e)}"
            )
            self.progress["value"] = 0

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCombinerApp(root)
    root.mainloop()