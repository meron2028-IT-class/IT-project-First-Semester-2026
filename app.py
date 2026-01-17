from flask import Flask, render_template, request
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Your data structures will go here
# diseases = {}
# recommendations = {}

# Your functions will go here
# def calculate_disease_probability(selected_symptoms):
#     pass

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize variables
    results = None
    recommendation = ""
    current_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    if request.method == "POST":
        # Get selected symptoms from form
        selected_symptoms = request.form.getlist("symptoms")
        
        if selected_symptoms:
            # YOUR LOGIC GOES HERE:
            # 1. Calculate disease probabilities
            # 2. Sort and get top 3
            # 3. Get recommendation for top disease
            
            # Example placeholder (remove this):
            # results = [("Common Cold", 75), ("Flu", 60), ("Allergies", 40)]
            # recommendation = "Visit the school nurse for evaluation."
            
            # Remove the pass when you add your logic
            pass
    
    # Render template with results
    return render_template("index.html", 
                         results=results, 
                         recommendation=recommendation,
                         date=current_date)

# Run the app
if __name__ == "__main__":
    app.run(debug=True, port=5000)