import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import bezier


def read_csv(csv_path):
    np_path_XYs = np.genfromtxt(csv_path, delimiter = ',')
    path_XYs = []
    for i in np.unique (np_path_XYs[: , 0]):
        npXYs = np_path_XYs [ np_path_XYs [: , 0] == i ][: , 1:]
        XYs = []
        for j in np . unique ( npXYs [: , 0]):
            XY = npXYs [ npXYs [: , 0] == j ][: , 1:]
            XYs . append ( XY )
            path_XYs . append ( XYs )
    return path_XYs


def plot(path_XYs):
    fig,ax = plt.subplots(tight_layout=True, figsize =(8 , 8))
    colours = ['b']
    for i, XYs in enumerate(path_XYs):
        c = colours[i % len(colours)]
        for XY in XYs :
            ax.plot ( XY [: , 0] , XY [: , 1] , c =c , linewidth =2)
    ax.set_aspect ( 'equal')
    plt.show()


# Function to fit a cubic Bézier curve
def fit_bezier_curve(points):
    # Convert points to bezier curve control points
    curve = bezier.Curve.from_nodes(points)
    return curve

# Example function to regularize and plot Bézier curves
def regularize_and_plot(path_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for XYs in path_XYs:
        for XY in XYs:
            # Fit a Bézier curve to the polyline
            if len(XY) < 4:
                continue  # Skip if not enough points to fit a curve
            # Convert polyline to bezier control points
            nodes = np.array(XY)
            curve = fit_bezier_curve(nodes)
            # Plot the original polyline
            ax.plot(XY[:, 0], XY[:, 1], 'b-', linewidth=2, label='Original')
            # Plot the Bézier curve
            curve_points = curve.evaluate_multi(np.linspace(0, 1, 100)).T
            ax.plot(curve_points[:, 0], curve_points[:, 1], 'r--', linewidth=2, label='Bézier Curve')
    ax.set_aspect('equal')
    plt.legend()
    plt.show()


csv_path = "problems/isolated.csv"
path_XYs = read_csv(csv_path)
plot(path_XYs)
regularize_and_plot(path_XYs)
