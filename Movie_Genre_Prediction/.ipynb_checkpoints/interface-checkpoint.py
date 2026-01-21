from model import predict_genre
import tkinter as tk
from tkinter import scrolledtext

# Function to predict genre
def predict():
    plot = text_area.get("1.0", tk.END).strip()
    if plot:
        genre = predict_genre(plot)
        result_label.config(text=f"Predicted Genre: {genre}")
    else:
        result_label.config(text="Please enter a movie plot!")

# GUI window
window = tk.Tk()
window.title("Movie Genre Predictor")

# Text area for input
text_area = scrolledtext.ScrolledText(window, width=60, height=10)
text_area.pack(padx=10, pady=10)

# Predict button
predict_button = tk.Button(window, text="Predict Genre", command=predict)
predict_button.pack(pady=5)

# Label to display result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run GUI
window.mainloop()
