class Solution:

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def fill(image: List[List[int]], sr: int, sc: int, current: int, color: int):
            if sr < 0 or sc < 00 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != current:
                return
            image[sr][sc] = color
            fill(image, sr-1, sc, current, color)
            fill(image, sr+1, sc, current, color)
            fill(image, sr, sc-1, current, color)
            fill(image, sr, sc+1, current, color)

        if image[sr][sc] == color:
            return image

        fill(image, sr, sc, image[sr][sc], color)
        return image