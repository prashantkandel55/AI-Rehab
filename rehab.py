import tkinter as tk
from tkinter import messagebox

def evaluate_condition():
    age = age_entry.get()
    bmi = bmi_entry.get()
    weight = weight_entry.get()
    injury_type = injury_var.get()
    pain_level = pain_var.get()

    # Check if all fields are filled
    if not (age and bmi and weight and injury_type and pain_level):
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return

    try:
        pain_level = int(pain_level)
    except ValueError:
        messagebox.showwarning("Input Error", "Pain level must be a number.")
        return

    # Provide recommendations based on injury type and pain level
    solutions = {
        "ACL Tear": [
            "Rest and avoid putting weight on the knee.",
            "Apply ice to reduce swelling.",
            "Consult a physical therapist for rehabilitation exercises."
        ],
        "Ankle Sprain": [
            "Rest the ankle and avoid weight-bearing activities.",
            "Apply ice for 15-20 minutes every hour.",
            "Elevate the ankle above heart level."
        ],
        "Hamstring Pull": [
            "Rest and avoid activities that cause pain.",
            "Apply ice to the injured area.",
            "Gentle stretching once the pain subsides."
        ],
        "Musculoskeletal Injury": [
            "Consult a healthcare professional for specific advice."
        ],
        "Bone Fracture": [
            "Immobilize the area and seek medical attention.",
            "Apply ice to reduce swelling."
        ],
        "Ligament Sprain": [
            "Rest the affected joint.",
            "Apply ice and elevate the joint.",
            "Consult a doctor if pain persists."
        ],
        "Tendon Injury": [
            "Rest and avoid activities that cause pain.",
            "Use a warm compress to ease discomfort.",
            "Gentle stretching may help."
        ],
        "Muscle Strain": [
            "Rest the muscle and avoid strenuous activity.",
            "Apply ice to reduce swelling.",
            "Gently stretch the muscle once pain decreases."
        ],
        "Shin Splint": [
            "Rest and avoid high-impact activities.",
            "Ice the shins after activity.",
            "Consider using arch supports in shoes."
        ],
        "Tennis Elbow": [
            "Rest the elbow and avoid activities that exacerbate pain.",
            "Apply ice to reduce swelling.",
            "Gentle stretching and strengthening exercises."
        ],
        "Sprain": [
            "Rest the injured area.",
            "Apply ice for 15-20 minutes every hour.",
            "Elevate the injured limb."
        ],
        "Fracture": [
            "Immobilize the area and seek medical attention.",
            "Apply ice to reduce swelling."
        ],
        "Tendonitis": [
            "Rest and avoid activities that cause pain.",
            "Use a warm compress to ease discomfort.",
            "Gentle stretching may help."
        ],
        "Other": [
            "Consult a healthcare professional for specific advice."
        ]
    }

    if pain_level > 5:
        messagebox.showinfo("Recommendation", "It's advisable to see a doctor.")
    else:
        home_solutions = solutions.get(injury_type, [])
        if home_solutions:
            solution_text = "\n".join(home_solutions)
            messagebox.showinfo("Home Solutions", f"Here are some home solutions for {injury_type}:\n{solution_text}")
        else:
            messagebox.showinfo("Home Solutions", "No specific solutions available.")

# Create the main window
root = tk.Tk()
root.title("AI_Rehab GUI")
root.geometry("500x500")
root.configure(bg="#EAEAEA")

# Add a title label
title_label = tk.Label(root, text="AI-Rehab", font=("Arial", 22, 'bold'), bg="#4CAF50", fg="white")
title_label.pack(pady=20, fill=tk.X)

# Frame for input fields
input_frame = tk.Frame(root, bg="#EAEAEA")
input_frame.pack(pady=20)

# Function to create styled entry fields
def create_styled_entry(parent):
    entry = tk.Entry(parent, font=("Arial", 12), width=20, bd=2, relief="groove", bg="#FFFFFF", fg="#333333")
    entry.config(highlightbackground="#4CAF50", highlightcolor="#4CAF50", highlightthickness=2)
    return entry

# Age input
tk.Label(input_frame, text="Age:", bg="#EAEAEA", font=("Arial", 12)).grid(row=0, column=0, sticky='w', padx =10, pady=10)
age_entry = create_styled_entry(input_frame)
age_entry.grid(row=0, column=1, padx=10, pady=10)

# BMI input
tk.Label(input_frame, text="BMI:", bg="#EAEAEA", font=("Arial", 12)).grid(row=1, column=0, sticky='w', padx=10, pady=10)
bmi_entry = create_styled_entry(input_frame)
bmi_entry.grid(row=1, column=1, padx=10, pady=10)

# Weight input
tk.Label(input_frame, text="Weight (kg):", bg="#EAEAEA", font=("Arial", 12)).grid(row=2, column=0, sticky='w', padx=10, pady=10)
weight_entry = create_styled_entry(input_frame)
weight_entry.grid(row=2, column=1, padx=10, pady=10)

# Injury type dropdown
tk.Label(input_frame, text="Injury Type:", bg="#EAEAEA", font=("Arial", 12)).grid(row=3, column=0, sticky='w', padx=10, pady=10)
injury_var = tk.StringVar(root)
injury_var.set("Select Injury")  # default value
injury_menu = tk.OptionMenu(input_frame, injury_var, 
                            "ACL Tear", "Ankle Sprain", "Hamstring Pull", 
                            "Musculoskeletal Injury", "Bone Fracture", 
                            "Ligament Sprain", "Tendon Injury", 
                            "Muscle Strain", "Shin Splint", 
                            "Tennis Elbow", "Sprain", "Fracture", 
                            "Tendonitis", "Other")
injury_menu.config(font=("Arial", 12), width=18)
injury_menu.grid(row=3, column=1, padx=10, pady=10)

# Pain level dropdown
tk.Label(input_frame, text="Pain Level (1-10):", bg="#EAEAEA", font=("Arial", 12)).grid(row=4, column=0, sticky='w', padx=10, pady=10)
pain_var = tk.StringVar(root)
pain_var.set("Select Pain Level")  # default value
pain_menu = tk.OptionMenu(input_frame, pain_var, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
pain_menu.config(font=("Arial", 12), width=18)
pain_menu.grid(row=4, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", command=evaluate_condition, bg="#4CAF50", fg="white", font=("Arial", 14, 'bold'), width=15)
submit_button.pack(pady=30)

# Run the application
root.mainloop()