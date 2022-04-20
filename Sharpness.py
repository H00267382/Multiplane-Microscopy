from numpy import linspace, sum as Sigma, array as Array
import matplotlib.pyplot as plt


class ImageProcessing:
    def __init__(self, Img, planeNum: int = 1):
        self.Img = Img
        self.planeNum = planeNum

    def sharpness(self, weighted: bool = False):
        """Takes in an image and returns a single float value denoting its sharpness

        Args:
            planeNum (int): The z location of the input image. Defaults to 1.
        """
        if weighted:
            return (
                self.planeNum
                * Sigma(Sigma(self.Img, axis=0) ** 2 - Sigma(self.Img, axis=0))
                / Sigma(self.Img) ** 2
            )
        else:
            return [
                self.planeNum,
                Sigma(Sigma(self.Img, axis=0) ** 2 - Sigma(self.Img, axis=0))
                / Sigma(self.Img) ** 2,
            ]

    def __repr__(self) -> str:
        return "ImageProcessing({})".format("Image")

    def __add__(self, other):
        """Defines an object addition operator for adding weighted sharpness values together

        Args:
            other (float or ImageProcessing): The value to sum with

        Returns:
            float: The summed values
        """
        if isinstance(other, float):
            return self.sharpness(weighted=True) + other
        elif isinstance(other, ImageProcessing):
            return self.sharpness(weighted=True) + other.sharpness(weighted=True)


if __name__ == "__main__":
    imgs = []
    for i in linspace(10, 15.75, 24):
        imgs.append(
            ImageProcessing(Sigma(plt.imread(str(i) + ".png"), axis=2), planeNum=i)
        )

    weighted_sum, sharp_sum = (0.0, 0)
    s, sampled_vals, popi = ([], [], [])
    underfit_factor = 1

    for i, img in enumerate(imgs):
        sharpness = img.sharpness()
        s.append(sharpness)

        if i % underfit_factor == 0:
            weighted_sum = img + weighted_sum
            sharp_sum += sharpness[1]
            sampled_vals.append(sharpness)
            popi.append(i)

    s_plot = Array(s)
    sampled_vals_plot = Array(sampled_vals)

    plt.scatter(s_plot[:, 0], s_plot[:, 1] * 100)
    plt.xlabel("z position (m)")
    plt.ylabel("Sharpness (arb.)")
    plt.title("Sharpness as a function of z")
    plt.show()

    for i in reversed(popi):
        s.pop(i)

    print(
        "The predicted z value based on sharpness is %.3f m"
        % (weighted_sum / sharp_sum)
    )
    print("With %d samples" % len(sampled_vals))

    if len(s) > 0:
        s_plot = Array(s)
        plt.scatter(s_plot[:, 0], s_plot[:, 1] * 100)
    plt.scatter(sampled_vals_plot[:, 0], sampled_vals_plot[:, 1] * 100)
    plt.xlabel("z position (m)")
    plt.ylabel("Sharpness (arb.)")
    plt.title("Undersampled sharpness as a function of z")
    plt.show()
