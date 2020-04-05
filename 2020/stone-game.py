       alice = 0
        bob = 0
        print(alice)
        i = 0
        turn = "Alice"
        while i < len(stoneValue):
            acc_sum = []
            s = 0
            j, count = i, 0
            while j < len(stoneValue) and count < 3:
                s += stoneValue[j]
                acc_sum.append(s)
            max_sum = -sys.maxsize
            for k, val in acc_sum:
                if max_sum < val:
                    max_sum = val
                    i = k
            if turn == "Alice":
                alice += max_sum
                turn = "Bob"
            else:
                bob += max_sum
                turn = "Alice"
        if alice > bob:
            return "Alice"
        elif alice == bob:
            return "Bob"
        return "Tie"