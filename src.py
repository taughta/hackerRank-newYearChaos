def minimum_bribes(this_queue):

    peoples_final_position = this_queue
    nr_of_all_people = len(this_queue)
    peoples_original_position = [z for z in range(1, nr_of_all_people+1)]

    if nr_of_all_people == 1:
        return 0
    else:
        # Create a dictionary where the number of movements can be logged
        movement_log = {}
        for i in range(1, nr_of_all_people+1):
            movement_log[i] = 0

        # Counter for number of movements
        nr_of_movements = 0

        while True:
            for s in range(nr_of_all_people-1, 0, -1):
                if peoples_final_position[s] < peoples_final_position[s-1]:
                    temp_a, temp_b = peoples_final_position[s], peoples_final_position[s-1]
                    peoples_final_position[s], peoples_final_position[s-1] = temp_b, temp_a
                    movement_log[peoples_final_position[s]] += 1
                    nr_of_movements += 1
                else:
                    continue
            if peoples_original_position == peoples_final_position:
                break

        # Check in the movement log dictionary if any of the people has more than 2 movements
        for k in movement_log:
            if movement_log.get(k) > 2:
                return "Too chaotic"
        return nr_of_movements


if __name__ == '__main__':
    t = int(input())
    assert 1 <= t <= 10, "Minimum 1 and maximum 10 test cases are allowed."

    for t_itr in range(t):
        n = int(input())
        assert 1 <= n <= 10 ** 5, "Minimum 1 and maximum 10**5 people are allowed in the queue."

        q = list(map(int, input().rstrip().split()))
        assert len(q) == n, "The amount of entered number does not equal to the initially planned number of people."

        print(minimum_bribes(q))
