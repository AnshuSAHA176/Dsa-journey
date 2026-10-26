class Solution:
    def compress(self, chars: list[str]) -> int:
        count = 1
        cheack = chars[0]
        write = 0

        for i in range(1, len(chars)):
            if chars[i] == cheack:
                count += 1
            else:
                chars[write] = cheack
                write += 1

                if count != 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1

                cheack = chars[i]
                count = 1

        # Handle the final group
        chars[write] = cheack
        write += 1

        if count != 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

        return write