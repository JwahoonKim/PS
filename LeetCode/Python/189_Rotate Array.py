from typing import List


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        return gcd(b, a)
    return gcd(b, a % b)


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m = gcd(len(nums), k)

        for i in range(m):
            now_value = nums[i % len(nums)]
            for j in range(len(nums) // m):
                next_value = nums[(i + k * (j + 1)) % len(nums)]
                nums[(i + (j + 1) * k) % len(nums)] = now_value
                now_value = next_value
