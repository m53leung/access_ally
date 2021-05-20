def count_arithmetic(totalMinutes):
    h = 12
    m1 = 0
    m2 = 0

    def incrementTime():
        """ Increments current time by one minute. """
        nonlocal h
        nonlocal m1
        nonlocal m2
        m2 += 1
        if m2 > 9:
            m2 = 0
            m1 += 1
            if m1 > 5:
                m1 = 0
                h += 1
                if h > 12:
                    h = 1

    def is_arithmetic():
        """ Checks if the current time is an arithmetic sequence. """
        nonlocal h
        nonlocal m1
        nonlocal m2
        if h > 9:
            step = (h%10) - (h//10)
            if m1 - (h%10) != step:
                return False
        else:
            step = m1 - h
            
        if m2 - m1 != step:
            return False

        return True
    
    if totalMinutes <= 720:
        # Iterate through all the times, and count the arithmetic sequences
        i = 0
        counter = 0
        while i < totalMinutes:
            if is_arithmetic():
                counter += 1
            incrementTime()
            i += 1
        # Check ending time
        if is_arithmetic():
            counter += 1
    else:
        # There are 720 in a full cycle (12:00 - 12:00), so we can call count_arithmetic once to determine the arithmetic sequences in one cycle, and multiply by the number of cycles
        # Since function checks ending time, pass 719 instead of 720 to prevent double counting 12:00, even though 12:00 is not an arithmetic sequence
        counter = count_arithmetic(719) * (totalMinutes // 720);
        counter += count_arithmetic(totalMinutes % 720)

    return counter

i = int(input())
print(count_arithmetic(i))
