class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def sort_key(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        sorted_points = sorted(points, key=sort_key)

        return sorted_points[:k]