def climbingLeaderboard(ranked, player):
    ranked = list(dict.fromkeys(ranked))
    i = len(ranked) - 1
    for player in player:
        while i >= 0:
            if player >= ranked[i]:
                i -= 1
            else:
                print(i + 2)
                break
        if i < 0:
            print(1)


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)