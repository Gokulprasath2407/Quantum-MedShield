import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


class Graphs:

    def __init__(self):
        os.makedirs("static/images", exist_ok=True)

    # -----------------------------
    # 1. QBER Trend Graph
    # -----------------------------
    def plot_qber(self, qber_values):

        plt.figure(figsize=(10, 5))
        plt.plot(
            range(1, len(qber_values) + 1),
            qber_values,
            marker='o',
            linewidth=1.5
        )

        plt.title("QBER Over Multiple Simulations")
        plt.xlabel("Simulation Number")
        plt.ylabel("QBER")
        plt.grid(True)

        plt.savefig("static/images/qber_plot.png")
        plt.close()

    # -----------------------------
    # 2. Histogram
    # -----------------------------
    def plot_histogram(self, qber_values):

        plt.figure(figsize=(8, 5))

        plt.hist(
            qber_values,
            bins=10,
            edgecolor='black'
        )

        plt.title("QBER Distribution")
        plt.xlabel("QBER")
        plt.ylabel("Frequency")

        plt.grid(True)

        plt.savefig("static/images/qber_histogram.png")
        plt.close()

    # -----------------------------
    # 3. Pie Chart
    # -----------------------------
    def plot_security_status(self, qber_values, threshold=0.11):

        secure = 0
        attacked = 0

        for value in qber_values:

            if value <= threshold:
                secure += 1
            else:
                attacked += 1

        plt.figure(figsize=(6, 6))

        plt.pie(
            [secure, attacked],
            labels=["Secure", "Attack Detected"],
            autopct="%1.1f%%",
            startangle=90
        )

        plt.title("Secure vs Attack Detection")

        plt.savefig("static/images/security_status.png")
        plt.close()

    # -----------------------------
    # 4. Threshold Comparison
    # -----------------------------
    def plot_threshold(self, qber_values, threshold=0.11):

        plt.figure(figsize=(10, 5))

        plt.plot(
            range(1, len(qber_values) + 1),
            qber_values,
            marker='o',
            label="QBER"
        )

        plt.axhline(
            y=threshold,
            color='red',
            linestyle='--',
            label="Threshold (11%)"
        )

        plt.xlabel("Simulation Number")
        plt.ylabel("QBER")
        plt.title("QBER Threshold Comparison")

        plt.legend()
        plt.grid(True)

        plt.savefig("static/images/qber_threshold.png")
        plt.close()

    # -----------------------------
    # 5. Bar Chart
    # -----------------------------
    def plot_bar_chart(self, qber_values, threshold=0.11):

        secure = 0
        attacked = 0

        for value in qber_values:

            if value <= threshold:
                secure += 1
            else:
                attacked += 1

        plt.figure(figsize=(6, 5))

        plt.bar(
            ["Secure", "Attack"],
            [secure, attacked]
        )

        plt.title("Simulation Summary")

        plt.ylabel("Number of Runs")

        plt.savefig("static/images/summary_bar.png")
        plt.close()