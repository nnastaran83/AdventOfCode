def main():
    total_square_feet_of_wrapping_paper()


# Part 1 + 2
def total_square_feet_of_wrapping_paper():
    input_file = open("input.txt")
    line = None
    wrapping_paper_amount = 0
    ribbon = 0
    add = 0
    while line != '':
        line = input_file.readline()
        if line == '':
            break
        line = line.split('x')
        l_w_h = []
        for item in line:
            l_w_h.append(int(item))
        x = l_w_h[0] * l_w_h[1]
        smallest = x
        add = 2 * (l_w_h[0] + l_w_h[1])
        y = l_w_h[1] * l_w_h[2]
        if y < smallest:
            smallest = y
            add = 2 * (l_w_h[1] + l_w_h[2])
        z = l_w_h[2] * l_w_h[0]
        if z < smallest:
            smallest = z
            add = 2 * (l_w_h[2] + l_w_h[0])

        ribbon += l_w_h[0] * l_w_h[1] * l_w_h[2] + add

        wrapping_paper_amount += 2 * (x + y + z) + smallest

    print(wrapping_paper_amount)
    print(ribbon)


main()
