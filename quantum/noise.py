import random
from qiskit import QuantumCircuit


class Noise:

    def __init__(self, probability=0.05):
        self.probability = probability

    def apply(self, circuits):

        noisy_circuits = []

        for circuit in circuits:

            qc = circuit.copy()

            # Bit Flip Noise
            if random.random() < self.probability:
                qc.x(0)

            noisy_circuits.append(qc)

        return noisy_circuits