import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox, simpledialog
from PIL import Image, ImageTk
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import os

slides = []
profile_image_path = ""
profile_name = ""

def add_slide():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        bg = bg_color.get()
        fg = fg_color.get()
        img = bg_image_path.get()
        slides.append({"text": text, "bg": bg, "fg": fg, "img": img})
        text_entry.delete("1.0", tk.END)
        messagebox.showinfo("Slide Added", f"Slide {len(slides)} added!")
    else:
        messagebox.showwarning("Empty", "Please enter slide text.")

def choose_bg_image():
    path = filedialog.askopenfilename(title="Select Background Image",
                                      filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if path:
        bg_image_path.set(path)

def select_profile_image():
    global profile_image_path
    path = filedialog.askopenfilename(title="Select Profile Image",
                                      filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if path:
        profile_image_path = path
        messagebox.showinfo("Profile Image", "Profile image selected successfully.")

def set_profile_name():
    global profile_name
    name = simpledialog.askstring("Profile Name", "Enter your name/handle:")
    if name:
        profile_name = name

def export_pdf():
    if not slides:
        messagebox.showerror("Error", "No slides to export.")
        return

    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if not output_path:
        return

    c = canvas.Canvas(output_path, pagesize=(1080, 1080))

    for slide in slides:
        # Background color or image
        if slide["img"] and os.path.exists(slide["img"]):
            img = Image.open(slide["img"]) 
            img = img.resize((1080, 1080))
            c.drawImage(ImageReader(img), 0, 0, width=1080, height=1080)
        else:
            c.setFillColor(slide["bg"])
            c.rect(0, 0, 1080, 1080, stroke=0, fill=1)

        # Text Content
        c.setFillColor(slide["fg"])
        c.setFont("Helvetica-Bold", 40)
        c.drawCentredString(540, 540, slide["text"])

        # Profile Image & Name
        if profile_image_path and os.path.exists(profile_image_path):
            img = Image.open(profile_image_path).resize((100, 100))
            c.drawImage(ImageReader(img), 30, 950, width=100, height=100)
        if profile_name:
            c.setFont("Helvetica", 20)
            c.drawString(140, 990, profile_name)

        c.showPage()

    c.save()
    messagebox.showinfo("Exported", f"PDF saved to {output_path}")

# GUI Setup
app = tk.Tk()
app.title("LinkedIn Carousel Generator")

# Text Area
tk.Label(app, text="Slide Text:").pack()
text_entry = tk.Text(app, height=4, width=50)
text_entry.pack(pady=5)

# Background Color
bg_color = tk.StringVar(value="#FFFFFF")
tk.Label(app, text="Background Color (Hex e.g., #FFFFFF):").pack()
tk.Entry(app, textvariable=bg_color).pack()

# Text Color
fg_color = tk.StringVar(value="#000000")
tk.Label(app, text="Text Color (Hex e.g., #000000):").pack()
tk.Entry(app, textvariable=fg_color).pack()

# Background Image Selection
bg_image_path = tk.StringVar(value="")
tk.Button(app, text="Choose Background Image (Optional)", command=choose_bg_image).pack(pady=5)

# Profile Image & Name
tk.Button(app, text="Set Profile Image", command=select_profile_image).pack(pady=5)
tk.Button(app, text="Set Profile Name", command=set_profile_name).pack(pady=5)

# Slide Controls
tk.Button(app, text="Add Slide", command=add_slide, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(app, text="Export to PDF", command=export_pdf, bg="#2196F3", fg="white").pack(pady=5)

app.mainloop()
