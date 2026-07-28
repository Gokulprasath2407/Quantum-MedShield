class Metrics:

    def __init__(self):
        pass

    def average_qber(self, qber_values):
        if not qber_values:
            return 0
        return sum(qber_values) / len(qber_values)

    def maximum_qber(self, qber_values):
        if not qber_values:
            return 0
        return max(qber_values)

    def minimum_qber(self, qber_values):
        if not qber_values:
            return 0
        return min(qber_values)

    def attack_detection_rate(self, qber_values, threshold=0.11):
        if not qber_values:
            return 0

        detected = sum(1 for qber in qber_values if qber > threshold)
        return (detected / len(qber_values)) * 100

    def secure_rate(self, qber_values, threshold=0.11):
        if not qber_values:
            return 0

        secure = sum(1 for qber in qber_values if qber <= threshold)
        return (secure / len(qber_values)) * 100