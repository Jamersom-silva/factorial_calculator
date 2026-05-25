from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            number = int(request.form["number"])

            if number < 0:
                error = "The number cannot be negative."
            else:
                result = calculate_factorial(number)
                result = f"{result:,}"

        except ValueError:
            error = "Enter a valid number."

    return render_template(
        "index.html",
        result=result,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)