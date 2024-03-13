# main.py
import logging
import gui

# Initialize logging
logging.basicConfig(filename='conversion.log', level=logging.INFO, format='%(asctime)s %(message)s')

if __name__ == "__main__":
    try:
        logging.info("Polyphron_PNG-JPG_ initialized successfully.")
        main_window = gui.create_main_window()
        main_window.mainloop()
    except Exception as e:
        logging.error("Error initializing Polyphron_PNG-JPG_: " + str(e))