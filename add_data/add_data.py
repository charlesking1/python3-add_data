total = 0

with open('data.txt') as infile:
    with open('results.txt', 'w') as outfile:

        for line in infile:
            try:
                num = float(line)
                total += num
                print(num, file=outfile)
            except ValueError:
                print(
                    "'{}' is not a number".format(line.rstrip())
                )

print(total)
