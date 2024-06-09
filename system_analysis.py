from sympy import symbols, Or, And, Not
import math


class SystemAnalysis:
    @staticmethod
    def hamming_distance(x, y):
        if len(x) != len(y):
            raise ValueError("Input strings must be of the same length")

        # Calculate Hamming distance
        hamming_dist = sum(el1 != el2 for el1, el2 in zip(x, y))

        # Number of errors that can be detected
        detectable_errors = hamming_dist - 1

        # Number of errors that can be corrected
        correctable_errors = (hamming_dist - 1) / 2

        return {"Hamming Distance": hamming_dist, "Detectable Errors": detectable_errors,
                "Correctable Errors": correctable_errors}

    @staticmethod
    def weighted_mean(data):
        s = 0
        try:
            for i in range(len(data)):
                d, prob = data[i]
                s += prob * d
            return s
        except:
            return sum(data) / len(data)

    @staticmethod
    def mean(data):
        return sum(data) / len(data)

    @staticmethod
    def harmonic_mean(data):
        inv = []
        for i in range(len(data)):
            inv.append(1 / data[i])
        return len(data) / sum(inv)

    @staticmethod
    def geometric_mean(data):
        m = 1
        for d in data:
            m *= d
        return m ** (1 / len(data))

    @staticmethod
    def norm_geometric_mean(reference_data, data):
        if len(data) != len(reference_data):
            raise ValueError("Input lists must be of the same length")
        normalized = [reference_data[i] / data[i] for i in range(len(data))]
        return SystemAnalysis.geometric_mean(normalized)

    @staticmethod
    def comparison(system_a, system_b):
        return {
            "normalized": system_a / system_b,
            "percentage": (((system_a / system_b) - 1) * 100)
        }

    @staticmethod
    def amdahls_law(p, n):
        """
        Calculate the speedup according to Amdahl's Law.

        Parameters:
        p (float): The proportion of the program that can be parallelized (0 <= p <= 1).
        n (int): The number of processors.

        Returns:
        float: The speedup.
        """
        if not (0 <= p <= 1):
            raise ValueError("The proportion p must be between 0 and 1.")
        if n <= 0:
            raise ValueError("The number of processors n must be greater than 0.")

        speedup = 1 / ((1 - p) + (p / n))
        return speedup

    @staticmethod
    def truth_table_to_expression(truth_table):
        """
        Convert a truth table to its Boolean expression using minterms and maxterms.

        Parameters:
        truth_table (list of lists): The truth table, where the last column is the function value.

        Returns:
        tuple: (minterm_expression, maxterm_expression)
        """
        # Extract the variable names from the first row
        variables = truth_table[0][:-1]
        num_vars = len(variables)
        variable_symbols = symbols(variables)

        # Extract the rows from the truth table
        rows = truth_table[1:]

        minterms = []
        maxterms = []

        for row in rows:
            inputs = row[:-1]
            output = row[-1]

            if output == 1:
                minterm = And(*[var if val else Not(var) for var, val in zip(variable_symbols, inputs)])
                minterms.append(minterm)
            else:
                maxterm = Or(*[Not(var) if val else var for var, val in zip(variable_symbols, inputs)])
                maxterms.append(maxterm)

        minterm_expression = Or(*minterms) if minterms else "0"
        maxterm_expression = And(*maxterms) if maxterms else "1"

        return minterm_expression, maxterm_expression

    @staticmethod
    def calculate_entropy_and_information(data):
        information = [-math.log(p, 2) for p in data]
        entropy = -sum([-information[i] * data[i] for i in range(len(data))])
        return {"entropy": entropy, "information": information}



if __name__ == '__main__':
    # amdahl's law test
    p = 0.9  # 90% of the program can be parallelized
    n = 4  # using 4 processors

    speedup = SystemAnalysis.amdahls_law(p, n)
    print(f"Speedup: {speedup}")

    # Hamming Distance usage
    x = "11111111"
    y = "11110000"
    print(SystemAnalysis.hamming_distance(x, y))

    # Example usage of truth table to expression
    truth_table = [
        ['a', 'b', 'f(a, b)'],
        [0, 0, 0],
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]

    minterm_expr, maxterm_expr = SystemAnalysis.truth_table_to_expression(truth_table)
    print(f"Minterm Expression: {minterm_expr}")
    print(f"Maxterm Expression: {maxterm_expr}")

    # Example usage of entropy and information
    print(SystemAnalysis.calculate_entropy_and_information([0.7, 0.25, 0.05]))
