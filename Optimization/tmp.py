import numpy as np

x = np.array([
    1.0,
    1.0,
    1.0,
    1.0,
    1.0,

    1.3,
    1.3,
    1.3,
    1.3,
    1.3,

    1.6,
    1.6,
    1.6,
    1.6,
    1.6,

    2.1,
    2.1,
    2.1,
    2.1,
    2.1,

    2.5,
    2.5,
    2.5,
    2.5,
    2.5,
    2.5,

    2.9,
    2.9,
    2.9,
    2.9,
    2.9,

    3.2,
    3.2,
    3.2,
    3.2,

    3.6,
    3.6,
    3.6,
    3.6,
    3.6,
    3.6,

    4.3,
    4.3,
    4.3,
    4.3,

    4.6,
    4.6,
    4.6,
    4.6,
    4.6,
    4.6,

    4.9,
    4.9,
    4.9,
    4.9,
    4.9,
])

y = np.array([
    1.0,
    1.5,
    1.6,
    1.7,
    1.9,

    1.0,
    1.5,
    1.6,
    1.7,
    1.9,

    1.0,
    1.5,
    1.6,
    1.7,
    1.9,

    1.0,
    1.6,
    1.7,
    1.9,
    2.4,

    1.3,
    1.7,
    1.9,
    2.4,
    2.6,
    2.9,

    1.9,
    2.1,
    2.3,
    2.5,
    3.1,

    2.3,
    2.5,
    3.1,
    3.7,

    2.3,
    3.1,
    3.3,
    3.7,
    4.1,
    4.2,

    3.3,
    3.6,
    4.0,
    4.5,

    3.9,
    4.2,
    4.4,
    4.5,
    4.6,
    4.7,

    4.4,
    4.5,
    4.6,
    4.7,
    4.9,
])

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x, y)
plt.xlim([0.9, 5.])
plt.ylim([0.9, 5.])

plt.savefig('semi.png', dpi=300, bbox_inches='tight')


x_unique = list(set(x))
y_unique = list(set(y))

xv, yv = np.meshgrid(x_unique, y_unique)

plt.figure()
plt.scatter(xv, yv)
plt.xlim([0.9, 5.])
plt.ylim([0.9, 5.])

plt.savefig('struct.png', dpi=300, bbox_inches='tight')


points = np.random.random_sample((100, 2)) * 3.9 + 1
plt.figure()
plt.scatter(points[:, 0], points[:, 1])
plt.xlim([0.9, 5.])
plt.ylim([0.9, 5.])

plt.savefig('unstruct.png', dpi=300, bbox_inches='tight')