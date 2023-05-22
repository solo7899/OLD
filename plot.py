import random
import matplotlib.pyplot as plt
import mplcursors


def random_money(people, rounds):
    for i in range(rounds):
        for j in range(len(people)):
            if people[j] > 0:
                people[j] -= 1

                person2 = random.randrange(0, 50)
                while people[person2] == 0:
                    person2 = random.randrange(0, 50)
                people[person2] += 1
            else:
                continue
    return people


people = [100 for i in range(50)]
money = random_money(people, 10000)
people = list(range(50))
print(money)

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])

plt.title("RANDOMIZATION")
plt.xticks(ticks=people, rotation=0)

plt.bar(people, money, color='blue', align='center')
mplcursors.cursor(hover=True)
plt.show()
