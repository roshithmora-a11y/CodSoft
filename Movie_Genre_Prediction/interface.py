import tkinter as tk
from tkinter import scrolledtext
import joblib

# Load trained model and vectorizer
model = joblib.load("genre_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Predict function (called every button click)
def predict_genre():
    plot = text_area.get("1.0", tk.END).strip()

    if plot == "":
        result_label.config(text="⚠ Please enter a movie plot")
        return

    plot_vector = vectorizer.transform([plot])
    prediction = model.predict(plot_vector)[0]

    result_label.config(
        text=f"🎬 Predicted Genre: {prediction}",
        fg="green"
    )

# GUI Window
root = tk.Tk()
root.title("Movie Genre Prediction")
root.geometry("700x500")

# Title
tk.Label(
    root,
    text="Movie Genre Prediction (Real-Time)",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Text Input
text_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=12,
    font=("Arial", 11)
)
text_area.pack(padx=10, pady=10)

# Predict Button
tk.Button(
    root,
    text="Predict Genre",
    command=predict_genre,
    font=("Arial", 14),
    bg="blue",
    fg="white"
).pack(pady=10)

# Result Label (UPDATES EVERY TIME)
result_label = tk.Label(
    root,
    text="Enter a movie plot and click Predict",
    font=("Arial", 14)
)
result_label.pack(pady=10)

# Start GUI
root.mainloop()
