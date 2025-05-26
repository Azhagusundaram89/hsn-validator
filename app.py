from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load and clean Excel data once at startup
df = pd.read_excel("HSN_SAC.xlsx")
df.columns = df.columns.str.strip()
df["HSNCode"] = df["HSNCode"].astype(str).str.strip()


def validate_hsn(hsn_code):
    hsn_code = str(hsn_code).strip()
    if not hsn_code.isdigit() or not (2 <= len(hsn_code) <= 8):
        return {"valid": False, "reason": "Invalid format"}

    row = df[df["HSNCode"] == hsn_code]
    if not row.empty:
        return {"valid": True, "description": row.iloc[0]["Description"]}
    else:
        return {"valid": False, "reason": "Not found"}

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        hsn_code = request.form.get("hsn_code")
        result = validate_hsn(hsn_code)
        result["hsn_code"] = hsn_code
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
