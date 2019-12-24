class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int):

        MEMO = {} #用字典缓存，避免重复计算，几步之后会有大量重复的点
        def get_next(r, c):

            for x, y in [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]:
                yield r + x, c + y

        def is_avaliable(r, c):
            return 0 <= r < N and 0 <= c < N

        def dfs(r, c, steps):

            if (r, c, steps) in MEMO:
                return MEMO[(r, c, steps)]

            if is_avaliable(r, c):
                if steps <= 0:
                    return 1
                else:
                    pp = 0
                    for x, y in get_next(r, c):
                        pp += 0.125 * dfs(x, y, steps - 1)

                    MEMO[(r, c, steps)] = pp
                    return pp
            else:
                return 0


        return dfs(r, c, K)
