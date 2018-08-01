# Complete the minimumBribes function below.


def calculate_if_too_chaotic(chaotoc_list):
    people_that_moved = []
    for ppl in range(1, len(chaotoc_list) + 1):
        if not (ppl == chaotoc_list[ppl - 1]):
            people_that_moved.append(ppl)

    peoples_final_position = []
    for mp in people_that_moved:
        peoples_final_position.append(chaotoc_list.index(mp) + 1)

    for z in range(len(people_that_moved)):
        movement_value = people_that_moved[z] - peoples_final_position[z]
        if movement_value > 2:
            return "Too chaotic"

    return "ok"


def minimum_bribes(this_queue):
    if len(this_queue) == 1:
        return 0

    elif calculate_if_too_chaotic(this_queue) == "Too chaotic":
            print("Too chaotic")

    else:
        number_of_bribes = 0
        for h in range(0, len(this_queue)-1):
            for k in range(0, len(this_queue)-1):
                if this_queue[k] > this_queue[k+1]:
                    temp = this_queue[k]
                    this_queue[k] = this_queue[k+1]
                    this_queue[k+1] = temp
                    number_of_bribes += 1

        print(number_of_bribes)


if __name__ == '__main__':
    t = int(input())
    assert 1 <= t <= 10, "Minimum 1 and maximum 10 test cases are allowed."

    for t_itr in range(t):
        n = int(input())
        assert 1 <= n <= 10 ** 5, "Minimum 1 and maximum 10**5 people are allowed in the queue."

        q = list(map(int, input().rstrip().split()))
        assert len(q) == n, "The amount of entered number does not equal to the initially planned number of people."

        minimum_bribes(q)
