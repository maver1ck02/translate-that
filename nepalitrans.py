from deep_translator import GoogleTranslator
import tkinter as tk

# Function to translate text to Nepali
def translate_to_nepali():
    text = entry.get()  # Get the input text
    translated_text = GoogleTranslator(source='en', target='ne').translate(text)  # Translate from English to Nepali
    result_label.config(text="Translated Text: " + translated_text)  # Show the translated text

# GUI setup
root = tk.Tk()
root.title("Real-Time Translation to Nepali")

# Instructions Label
instruction_label = tk.Label(root, text="Enter text to translate into Nepali:")
instruction_label.pack(pady=10)

# Text entry field
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_to_nepali)
translate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Translated Text: ")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
