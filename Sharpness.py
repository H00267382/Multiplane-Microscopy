import numpy as np
import matplotlib.pyplot as plt


def sharpness(Img: np.array, planeNum: int = 1):
    """Takes in an image and returns a single float value denoting its sharpness

    Args:
        Img (np.array): The input image, should be of shape (nx, ny)
        planeNum (int): The z location of the input image. Defaults to 1.
    """
    return [
        planeNum,
        np.sum(np.sum(Img, axis=0) ** 2 - np.sum(Img, axis=0)) / np.sum(Img) ** 2,
    ]


s = []

for i in np.linspace(10, 15.75, 24):
    img = np.sum(plt.imread(str(i) + ".png"), axis=2)
    s.append(sharpness(img, planeNum=i))
s_plot = np.array(s)

plt.scatter(s_plot[:, 0], s_plot[:, 1] * 100)
plt.xlabel("z position (m)")
plt.ylabel("Sharpness (arb.)")
plt.title("Sharpness as a function of z")
plt.show()

weighted_sum, sharp_sum = (0, 0)
underfit_factor = 4
numberOfSamples = 0
sampled_vals, popi = ([], [])

for i, vals in enumerate(s):
    if i % underfit_factor == 0:
        weighted_sum += vals[0] * vals[1]
        sharp_sum += vals[1]
        numberOfSamples += 1
        sampled_vals.append([vals[0], vals[1]])
        popi.append(i)
for i in reversed(popi):
    s.pop(i)


print("The predicted z value based on sharpness is %.3f m" % (weighted_sum / sharp_sum))
print("With %d samples" % numberOfSamples)

sampled_vals_plot = np.array(sampled_vals)
if len(s) > 0:
    s_plot = np.array(s)
    plt.scatter(s_plot[:, 0], s_plot[:, 1] * 100)
plt.scatter(sampled_vals_plot[:, 0], sampled_vals_plot[:, 1] * 100)
plt.xlabel("z position (m)")
plt.ylabel("Sharpness (arb.)")
plt.title("Undersampled sharpness as a function of z")
plt.show()
