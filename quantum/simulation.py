from quantum.bb84 import BB84
from quantum.eve import Eve
from quantum.noise import Noise


class Simulation:

    def __init__(
        self,
        n_bits=8,
        eve_enabled=True,
        noise_enabled=False,
        noise_probability=0.05
    ):

        self.n_bits = n_bits

        self.bb84 = BB84(n_bits)
        self.eve = Eve()
        self.noise = Noise(noise_probability)

        self.eve_enabled = eve_enabled
        self.noise_enabled = noise_enabled
        self.noise_probability = noise_probability

        self.qber_values = []

    def run(self):

        # -------------------------
        # Alice
        # -------------------------

        alice_bits = self.bb84.generate_bits()
        alice_bases = self.bb84.generate_bases()

        # -------------------------
        # Bob
        # -------------------------

        bob_bases = self.bb84.generate_bases()

        # -------------------------
        # Alice encodes qubits
        # -------------------------

        circuits = self.bb84.encode_qubits(
            alice_bits,
            alice_bases
        )

        # -------------------------
        # Eve Attack
        # -------------------------

        if self.eve_enabled:

            eve_bases = self.eve.generate_bases(
                self.n_bits
            )

            eve_bits = self.eve.intercept(
                circuits,
                eve_bases
            )

            circuits = self.eve.resend(
                eve_bits,
                eve_bases
            )

        # -------------------------
        # Quantum Noise
        # (placeholder)
        # -------------------------

        if self.noise_enabled:
            circuits = self.noise.apply(circuits)

            # Noise implementation will be added
            # in the next step.
            pass

        # -------------------------
        # Bob measures qubits
        # -------------------------

        bob_bits = self.bb84.measure_qubits(
            circuits,
            bob_bases
        )

        # -------------------------
        # Sift key
        # -------------------------

        alice_key, bob_key = self.bb84.sift_key(
            alice_bits,
            alice_bases,
            bob_bits,
            bob_bases
        )

        # -------------------------
        # Calculate QBER
        # -------------------------

        qber = self.bb84.calculate_qber(
            alice_key,
            bob_key
        )

        self.qber_values.append(qber)

        return qber