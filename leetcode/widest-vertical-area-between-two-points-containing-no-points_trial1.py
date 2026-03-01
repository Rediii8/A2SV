class Solution:
    def maxWidthOfVerticalArea(self, points):
        xs = sorted(point[0] for point in points)

        max_width = 0
        for i in range(1, len(xs)):
            max_width = max(max_width, xs[i] - xs[i - 1])

        return max_width