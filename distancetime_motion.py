import matplotlib.pyplot as plt
import numpy as np


class Graphs():
    def uniform_motion(totaldistance, totaltime, title="Object moving with uniform motion."):
        ######################################
        # Object moving with uniform motion. #
        ######################################
        try:
            xpoints = np.array([0, totaltime])
            ypoints = np.array([0, totaldistance])

            plt.plot(xpoints, ypoints, marker="o")
            plt.title(title)
            plt.xlabel("Time-->")
            plt.ylabel("Distance-->")

            plt.show()
        except:
            print(ValueError)

    def non_uniform(distance_array, totaltime_array, title="Object moving with non-uniform motion."):
        ##########################################
        # Object moving with non-uniform motion. #
        ##########################################
        try:
            plt.plot(totaltime_array, distance_array, marker="o")
            plt.title(title)
            plt.xlabel('Time-->')
            plt.ylabel('Distance-->')

            plt.show()
        except:
            print("Error occurred make sure to send a numpy array!")

xpoints=np.array([2, 4, 6, 8, 10, 12])
ypoints=np.array([1, 4, 9, 16, 25, 36])

print("NON UNIFORM")
Graphs.non_uniform(totaltime_array=xpoints, distance_array=ypoints, title="A object moving with non-uniform speed!")

print("Uniform")
Graphs.uniform_motion(totaldistance=36, totaltime=12, title="Object moving with uniform motion!")