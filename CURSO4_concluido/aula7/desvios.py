from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


# x = random.normal(size=(10,3))
# x = random.normal(loc=1, scale=2, size=(2,3))
# x = random.binomial(n=10, p=0.5, size=10)
# print(x)

# # sns.displot(random.normal(size=1000), kind="kde")
# sns.displot(random.binomial(n=10, p=0.5, size=1000))

# plt.show()

data = {
    "normal": random.normal(loc=50, scale=5, size=1000),
    "binominal": random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(data, kind="kde")

plt.show()