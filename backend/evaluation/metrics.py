import time


class Metrics:

    def __init__(self):

        self.requests = 0

        self.failures = 0

        self.total_latency = 0

        self.runtime_validation_score = 0

        self.repairs = 0

        self.failure_types = []

    # Request Start

    def record(self):

        self.requests += 1

        return time.time()

    # Failure

    def fail(self, error_type="Unknown"):

        self.failures += 1

        self.failure_types.append(
            error_type
        )

    # Latency

    def add_latency(self, latency_ms):

        self.total_latency += latency_ms

    # Runtime Validation Score

    def set_validation_score(
        self,
        score
    ):

        self.runtime_validation_score = score

    # Repair Count

    def record_repair(self):

        self.repairs += 1

    # Final Report

    def report(self):

        success = (

            self.requests -

            self.failures
        )

        success_rate = 0

        if self.requests > 0:

            success_rate = (

                success /

                self.requests

            ) * 100

        average_latency = 0

        if self.requests > 0:

            average_latency = (

                self.total_latency /

                self.requests

            )

        repair_rate = 0

        if self.requests > 0:

            repair_rate = (

                self.repairs /

                self.requests

            ) * 100

        return {

            "requests":

            self.requests,

            "failures":

            self.failures,

            "success_rate":

            round(
                success_rate,
                2
            ),

            "runtime_validation_score":

            self.runtime_validation_score,

            "average_latency_ms":

            round(
                average_latency,
                2
            ),

            "repair_rate":

            round(
                repair_rate,
                2
            ),

            "failure_types":

            self.failure_types
        }


metrics = Metrics()