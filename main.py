from quantum.simulation import Simulation
from quantum.graphs import Graphs
from quantum.metrics import Metrics
from quantum.report import Report


def main():

    NUM_RUNS = 100

    print("=" * 60)
    print("      QuantumShield MedEdge - BB84 Simulation")
    print("=" * 60)

    simulation = Simulation()
    graphs = Graphs()
    metrics = Metrics()
    report = Report()

    print(f"Running {NUM_RUNS} simulations...\n")

    for _ in range(NUM_RUNS):
        simulation.run()

    average_qber = metrics.average_qber(simulation.qber_values)
    maximum_qber = metrics.maximum_qber(simulation.qber_values)
    minimum_qber = metrics.minimum_qber(simulation.qber_values)
    attack_rate = metrics.attack_detection_rate(simulation.qber_values)
    secure_rate = metrics.secure_rate(simulation.qber_values)

    print("=" * 60)
    print("SIMULATION RESULTS")
    print("=" * 60)

    print(f"Total Runs            : {NUM_RUNS}")
    print(f"Average QBER          : {average_qber:.3f}")
    print(f"Maximum QBER          : {maximum_qber:.3f}")
    print(f"Minimum QBER          : {minimum_qber:.3f}")
    print(f"Attack Detection Rate : {attack_rate:.2f}%")
    print(f"Secure Channel Rate   : {secure_rate:.2f}%")

    print("=" * 60)

    graphs.plot_qber(simulation.qber_values)
    graphs.plot_histogram(simulation.qber_values)
    graphs.plot_security_status(simulation.qber_values)
    graphs.plot_threshold(simulation.qber_values)
    graphs.plot_bar_chart(simulation.qber_values)

    report.generate_report(
        NUM_RUNS,
        average_qber,
        maximum_qber,
        minimum_qber,
        attack_rate,
        secure_rate
    )


if __name__ == "__main__":
    main()