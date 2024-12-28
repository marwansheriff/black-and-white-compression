import os
from tkinter import Tk, Label, Button, filedialog, Scale, HORIZONTAL, StringVar, messagebox
from PIL import Image

def compress_image():
    file_path = file_var.get()
    if not file_path:
        messagebox.showerror("Error", "Please select an image.")
        return

    try:
        compression_percent = int(compression_var.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid compression percentage.")
        return


    if compression_percent not in [25, 50, 75]:
        messagebox.showerror("Error", "Please select a valid compression percentage (25%, 50%, or 75%).")
        return

    
    quality = 100 - compression_percent 

    try:
        img = Image.open(file_path)

        bw_img = img.convert("L")

        output_dir = os.path.join(os.path.dirname(file_path), "compressed_images")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"compressed_{compression_percent}%.jpg")

        bw_img.save(output_path, quality=quality)

        messagebox.showinfo("Success", f"Image saved at: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to process image: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if file_path:
        file_var.set(file_path)
        selected_file_label.config(text=f"Selected: {os.path.basename(file_path)}")

root = Tk()
root.title("Image Compressor")

file_var = StringVar()

compression_var = StringVar(value="50")

Label(root, text="Image Compressor", font=("Arial", 16)).pack(pady=10)

Button(root, text="Select Image", command=browse_file).pack(pady=5)
selected_file_label = Label(root, text="No file selected", wraplength=400)
selected_file_label.pack(pady=5)

Label(root, text="Compression Quality (%)", font=("Arial", 12)).pack(pady=5)

compression_slider = Scale(root, from_=25, to=75, orient=HORIZONTAL, variable=compression_var, tickinterval=25)
compression_slider.pack(pady=5)

Button(root, text="Compress Image", command=compress_image).pack(pady=10)

root.geometry("400x300")
root.mainloop()
