# **Image Combiner** 🖼️✨  

A simple yet powerful GUI application to **combine multiple images into a single vertical image** with customizable spacing and alignment. Built with Python (`tkinter` and `PIL`), featuring the soothing **Catppuccin Mocha** color palette.  

---

## **Features**  
✅ **Combine images vertically** into one output file  
✅ **Adjustable spacing** between images  
✅ **Alignment options** (left, center, right)  
✅ **Drag-and-drop-like UI** (add/remove images easily)  
✅ **Progress bar** for visual feedback  
✅ **Beautiful Catppuccin Mocha theme** 🎨  
✅ Supports **JPEG, PNG, BMP, GIF**  

---

## **Installation**  

### **Prerequisites**  
- Python 3.6+  
- `Pillow` (PIL fork) for image processing  

### **Steps**  
1. Clone/download this repository.  
2. Install dependencies:  
   ```sh
   pip install pillow
   ```
3. Run the script:  
   ```sh
   python image_combiner.py
   ```

---

## **Usage**  
1. **Add Images** – Click *"Add Images"* to select files.  
2. **Remove/Reorder** – Select images in the list and use *"Remove Selected"* or *"Clear All"*.  
3. **Set Options**  
   - **Spacing** (px) – Adjust the gap between images.  
   - **Alignment** – Choose left, center, or right alignment.  
   - **Output File** – Specify the save location (JPEG/PNG).  
4. **Combine!** – Click *"Combine Images"* and wait for completion.  

---

## **Screenshots**  
*(Example UI with Catppuccin Mocha theme)*  

![Image Combiner UI](https://via.placeholder.com/800x600/1e1e2e/cdd6f4?text=Image+Combiner+UI+Preview)  

*(Example output with 3 combined images)*  

![Combined Image Example](https://via.placeholder.com/600x800/313244/a6adc8?text=Combined+Image+Example)  

---

## **Customization**  
Want a different theme? Modify the `colors` dictionary in the code:  
```python
self.colors = {
    "base": "#1e1e2e",  # Dark background
    "text": "#cdd6f4",  # Light text
    "blue": "#89b4fa",  # Accent color
    # ... (more Catppuccin Mocha colors)
}
```

---

## **License**  
MIT License – Free to use, modify, and distribute.  

---

## **Support**  
🐞 **Found a bug?** Open an issue!  
💡 **Want a new feature?** Let me know!  

Enjoy combining images! 🚀  

---  
**Made with ❤️ using Python & Catppuccin Mocha**
