from flask import Flask, render_template, request, send_file
import os

from quantum.simulation import Simulation
from quantum.metrics import Metrics
from quantum.graphs import Graphs
from quantum.report import Report

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)


@app.route("/", methods=["GET", "POST"])
def index():

    # Default values
    total_runs = 100
    threshold = 0.11
    noise_probability = 0.05
    eve_enabled = True
    noise_enabled = False

    if request.method == "POST":

        try:
            total_runs = int(request.form.get("runs", 100))
        except ValueError:
            total_runs = 100

        try:
            threshold = float(request.form.get("threshold", 0.11))
        except ValueError:
            threshold = 0.11

        try:
            noise_probability = float(request.form.get("noise", 0.05))
        except ValueError:
            noise_probability = 0.05

        eve_enabled = "eve" in request.form
        noise_enabled = "noise_enabled" in request.form

    simulation = Simulation(
        eve_enabled=eve_enabled,
        noise_enabled=noise_enabled,
        noise_probability=noise_probability
    )

    metrics = Metrics()
    graphs = Graphs()
    report = Report()

    qber_values = []

    # Run Simulation
    for _ in range(total_runs):
        qber = simulation.run()
        qber_values.append(qber)

    # Calculate Metrics
    avg_qber = metrics.average_qber(qber_values)
    max_qber = metrics.maximum_qber(qber_values)
    min_qber = metrics.minimum_qber(qber_values)

    attack_rate = metrics.attack_detection_rate(qber_values)
    secure_rate = metrics.secure_rate(qber_values)

    secure_runs = round((secure_rate / 100) * total_runs)
    attack_runs = total_runs - secure_runs

    # Generate Graphs
    graphs.plot_qber(qber_values)
    graphs.plot_histogram(qber_values)
    graphs.plot_security_status(qber_values)
    graphs.plot_threshold(qber_values)
    graphs.plot_bar_chart(qber_values)

    # Generate PDF Report
    report.generate_report(
        total_runs,
        avg_qber,
        max_qber,
        min_qber,
        attack_rate,
        secure_rate
    )

    # Convert to percentage
    qber_percent = round(avg_qber * 100, 2)
    attack_percentage = round((attack_runs / total_runs) * 100, 1) if total_runs else 0

    return render_template(
        "index.html",

        avg_qber=qber_percent,
        qber_percent=qber_percent,

        secure_runs=secure_runs,
        attack_runs=attack_runs,
        total_runs=total_runs,

        threshold=round(threshold * 100, 2),
        channel_secure=avg_qber <= threshold,

        eve_enabled=eve_enabled,
        noise_enabled=noise_enabled,
        noise_probability=noise_probability,

        warning=(11 < qber_percent <= 20),
        critical=(qber_percent > 20),
        attack_percentage=attack_percentage
    )


@app.route("/download")
def download():

    pdf_path = os.path.join(
        BASE_DIR,
        "reports",
        "QuantumShield_Report.pdf"
    )

    return send_file(
        pdf_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)