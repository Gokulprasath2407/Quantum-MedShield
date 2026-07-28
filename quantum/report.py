import os
from datetime import datetime
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image
)


class Report:

    def __init__(self):
        os.makedirs("reports", exist_ok=True)

    def generate_report(
        self,
        total_runs,
        average_qber,
        maximum_qber,
        minimum_qber,
        attack_rate,
        secure_rate
    ):

        filename = "reports/QuantumShield_Report.pdf"

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        story = []

        story.append(
            Paragraph(
                "<b><font size=18>QuantumShield MedEdge</font></b>",
                styles["Title"]
            )
        )

        story.append(
            Paragraph(
                "<b>BB84 Quantum Key Distribution Simulation Report</b>",
                styles["Heading2"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph(
                f"Generated on : {datetime.now()}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("<b>Simulation Summary</b>", styles["Heading2"])
        )

        story.append(
            Paragraph(f"Total Runs : {total_runs}", styles["Normal"])
        )

        story.append(
            Paragraph(
                f"Average QBER : {average_qber:.3f}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Maximum QBER : {maximum_qber:.3f}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Minimum QBER : {minimum_qber:.3f}",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Attack Detection Rate : {attack_rate:.2f}%",
                styles["Normal"]
            )
        )

        story.append(
            Paragraph(
                f"Secure Channel Rate : {secure_rate:.2f}%",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 20))

        story.append(
            Paragraph("<b>Generated Graphs</b>", styles["Heading2"])
        )

        graph_files = [
            "static/images/qber_plot.png",
            "static/images/qber_histogram.png",
            "static/images/security_status.png",
            "static/images/qber_threshold.png",
            "static/images/summary_bar.png"
        ]

        for graph in graph_files:

            if os.path.exists(graph):

                story.append(Image(graph, width=450, height=250))
                story.append(Spacer(1, 15))

        story.append(
            Paragraph(
                "<b>Conclusion</b>",
                styles["Heading2"]
            )
        )

        if average_qber <= 0.11:

            result = (
                "The communication channel is considered SECURE. "
                "The average QBER remains below the BB84 security threshold."
            )

        else:

            result = (
                "The communication channel shows evidence of possible "
                "eavesdropping because the average QBER exceeds the "
                "recommended BB84 threshold."
            )

        story.append(
            Paragraph(result, styles["Normal"])
        )

        doc.build(story)

        print("\nPDF Report Generated Successfully.")
        print(filename)