import tkinter as tk
import random
import time

# Sample text for the typing test
sample_text = "The quick brown fox jumps over the lazy dog."

# Function to start the typing test
def start_typing_test():
    global start_time
    start_time = time.time()
    input_entry.config(state=tk.NORMAL)
    input_entry.delete(0, tk.END)
    display_label.config(text=sample_text)
    start_button.config(state=tk.DISABLED)
    result_label.config(text="Type the text above and press 'Done' when finished.")

# Function to calculate and display the results
def calculate_results():
    global start_time
    elapsed_time = time.time() - start_time
    typed_text = input_entry.get()
    correct_characters = sum(1 for a, b in zip(sample_text, typed_text) if a == b)
    accuracy = (correct_characters / len(sample_text)) * 100
    wpm = int((len(sample_text.split()) / elapsed_time) * 60)

    result_label.config(text=f"Time: {elapsed_time:.2f} seconds\nAccuracy: {accuracy:.2f}%\nWords per Minute (WPM): {wpm}")
    start_button.config(state=tk.NORMAL)
    input_entry.config(state=tk.DISABLED)

# Create the main window
window = tk.Tk()
window.title("Speed Typing Test")

# Set the dimensions of the window (width x height)
window.geometry("800x400")  # Adjust the dimensions as needed

# Create and configure widgets
display_label = tk.Label(window, text="", font=("Arial", 14))
input_entry = tk.Entry(window, state=tk.DISABLED, font=("Arial", 16))  # Increase the font size here
start_button = tk.Button(window, text="Start Test", command=start_typing_test)
done_button = tk.Button(window, text="Done", command=calculate_results)
result_label = tk.Label(window, text="", font=("Arial", 12))

# Place widgets in the window
display_label.pack(pady=10)
input_entry.pack(pady=10)
start_button.pack()
done_button.pack()
result_label.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()
