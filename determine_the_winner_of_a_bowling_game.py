
def get_score(player: list[int]) -> int:
    if len(player) == 1:
        return player[0]

    result = player[0] + (player[1] if player[0] != 10 else 2 * player[1])
    if len(player) == 2:
        return result

    for i in range(2, len(player)):
        if player[i-1] == 10 or player[i-2] == 10:
            result += player[i] * 2
        else:
            result += player[i]
    return result


class Solution:
    """
    https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
    """
    def isWinner(self, player1: list[int], player2: list[int]) -> int:
        player1_score = get_score(player1)
        player2_score = get_score(player2)

        if player1_score > player2_score:
            return 1
        elif player1_score == player2_score:
            return 0
        return 2


print(Solution().isWinner([5,10,3,2], [6,5,7,3]))
# Solution().isWinner([7,10,2,6,8,5,4,6,10,9,1,4,3,10,0,9,6,1,0], [2,1,9,4,5,0,6,5,6,10,10,4,8,8,6,9,2,9,5])
