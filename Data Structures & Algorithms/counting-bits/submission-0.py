class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        dp approach by relationship with even vs odd bit representation relationships
        """
        if not n:
            return [0]

        if n == 1:
            return [0, 1]

        output = [0] * (n + 1)
        output[0] = 0
        output[1] = 1

        for i in range(2, n+1):
            output[i] = output[i // 2] + (i % 2)

        return output