class ErrorDetection:
    def __init__(self, parity_type='even'):
        self.parity_type = parity_type

    @staticmethod
    def binary_addition(a, b, n_bits):
        result = int(a, 2) + int(b, 2)
        carry = result >> n_bits  # Extract the carry bit(s)
        result = result & ((1 << n_bits) - 1)  # Keep only the n_bits
        while carry > 0:  # Continue to add carry bits until there are no more carry bits
            result += carry
            carry = result >> n_bits
            result = result & ((1 << n_bits) - 1)
        return bin(result)[2:].zfill(n_bits)

    @staticmethod
    def ones_complement(binary_str):
        return ''.join('1' if bit == '0' else '0' for bit in binary_str)

    @staticmethod
    def print_binary_addition(a, b, result):
        print(f"  {a}")
        print(f"+ {b}")
        print("-----------")
        print(f"  {result}")
        print()

    def calculate_checksum(self, data_blocks):
        n_bits = len(data_blocks[0])
        sum_result = data_blocks[0]
        print("Sender Side Calculation")
        print("========================")
        print("Data Blocks:")
        for block in data_blocks:
            print(block)
        print()

        for block in data_blocks[1:]:
            new_sum = self.binary_addition(sum_result, block, n_bits)
            print(f"Adding {sum_result} and {block}:")
            self.print_binary_addition(sum_result, block, new_sum)
            sum_result = new_sum

        checksum = self.ones_complement(sum_result)
        print("One's Complement of Sum (Checksum):")
        print("-----------")
        print(checksum)
        print()
        return checksum

    def verify_data(self, data_blocks, received_checksum):
        n_bits = len(data_blocks[0])
        sum_result = data_blocks[0]
        print("Receiver Side Verification")
        print("==========================")
        print("Data Blocks:")
        for block in data_blocks:
            print(block)
        print(f"Received Checksum: {received_checksum}\n")

        for block in data_blocks[1:]:
            new_sum = self.binary_addition(sum_result, block, n_bits)
            print(f"Adding {sum_result} and {block}:")
            self.print_binary_addition(sum_result, block, new_sum)
            sum_result = new_sum

        final_sum = self.binary_addition(sum_result, received_checksum, n_bits)
        print(f"Adding {sum_result} and received checksum {received_checksum}:")
        self.print_binary_addition(sum_result, received_checksum, final_sum)

        result = self.ones_complement(final_sum)
        print("One's Complement of Final Sum:")
        print("-----------")
        print(result)
        print()

        if result == '0' * n_bits:
            print("Verification successful: Data accepted (All zeros).")
        else:
            print("Verification failed: Data corrupted.")

    def calculate_parity_bit(self, data):
        count_of_ones = data.count('1')
        parity_bit = count_of_ones % 2 if self.parity_type == 'even' else (count_of_ones + 1) % 2
        return parity_bit

    def detect_error(self, sender_data, receiver_data):
        calculated_sender_parity = self.calculate_parity_bit(sender_data)
        calculated_receiver_parity = self.calculate_parity_bit(receiver_data)

        print(f"Sender Data: {sender_data}")
        print(f"Receiver Data: {receiver_data}")
        print(f"Calculated Sender Parity: {calculated_sender_parity}")
        print(f"Calculated Receiver Parity: {calculated_receiver_parity}")

        if calculated_sender_parity != calculated_receiver_parity:
            print("Error detected.")
            return True
        else:
            print("No error detected.")
            return False


if __name__ == '__main__':
    # Example usage for checksum:
    dt = ErrorDetection()
    sender_data_blocks = ["10011001", "11100010", "00100100", "10000100"]
    receiver_data_blocks = ["10011001", "11100010", "00100100", "10000100"]
    checksum = dt.calculate_checksum(sender_data_blocks)
    dt.verify_data(receiver_data_blocks, checksum)

    # Example usage for parity error detection:
    sender_data = "00011010"
    receiver_data = "00011100"
    parity_type = "even"

    dt = ErrorDetection(parity_type)
    error_detected = dt.detect_error(sender_data, receiver_data)
