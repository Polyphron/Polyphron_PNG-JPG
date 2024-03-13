import tkinter as tk
from tkinter import filedialog, messagebox
import logging
import image_conversion

# Global variable to store the directory path
selected_directory = ""

def create_main_window():
    root = tk.Tk()
    root.title("PNG to JPG Converter")
    root.geometry("600x400")

    def select_directory():
        global selected_directory
        directory = filedialog.askdirectory()
        if directory:  # Ensure a directory was selected
            selected_directory = directory  # Store the selected directory path
            logging.info(f"Directory selected: {directory}")
            messagebox.showinfo("Directory Selected", f"Directory {directory} has been selected for conversion.")
        else:
            logging.info("Directory selection was cancelled.")
    
    def convert_images():
        global selected_directory
        try:
            logging.info("Starting image conversion...")
            image_conversion.convert_directory_to_jpg(selected_directory)
            messagebox.showinfo("Conversion Complete", "we have done it again boys")
            logging.info("Image conversion completed successfully.")
        except Exception as e:
            logging.error("Error during image conversion: " + str(e), exc_info=True)
            messagebox.showerror("Conversion Error", "An error occurred during the conversion process. Check logs for details.")

    # GUI Components
    select_dir_btn = tk.Button(root, text="Select Directory", command=select_directory)
    select_dir_btn.pack(pady=20)

    convert_btn = tk.Button(root, text="Convert", command=convert_images)
    convert_btn.pack(pady=10)

    log_text_area = tk.Text(root, height=10)
    log_text_area.pack(pady=20)

    # Redirecting logging output to the text area
    class TextHandler(logging.Handler):
        def __init__(self, text):
            super().__init__()
            self.text = text

        def emit(self, record):
            msg = self.format(record)
            self.text.insert(tk.END, msg + '\n')
            self.text.see(tk.END)

    logging_handler = TextHandler(log_text_area)
    logging.basicConfig(handlers=[logging_handler], level=logging.INFO)

    return root