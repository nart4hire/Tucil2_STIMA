# Import Library For Data Visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# Import Test Datasets
from sklearn import datasets

class ConvexHull():
    points = []
    hull = []

    def __init__(self):
        self.points = []
        self.hull = []

    def add(self, point):
        self.points.append(point)

    def sortPoints(self):
        self.points = sorted(self.points, key=lambda x: [x[0], x[1]])

    def getPartition(p1, p2, p3):
        #       x1    * y2    + x3    * y1    + x2    * y3      -   x3    * y2    - x2    * y1    - x1    * y3
        return (p1[0] * p2[1] + p3[0] * p1[1] + p2[0] * p3[1]) - (p3[0] * p2[1] + p2[0] * p1[1] + p1[0] * p3[1])

    def getLength(x, y):
        return sqrt(x ** 2 + y ** 2)

    def getDistance(p1, p2, p3):
        num = abs((p2[0] - p1[0]) * (p1[1] - p3[1]) -
                  (p1[0] - p3[0]) * (p2[1] - p1[1]))
        den = ConvexHull.getLength(p2[0] - p1[0], p2[1] - p1[1])
        return num / den

    def getAngle(p1, p2, p3):
        v1 = [p2[0] - p1[0], p2[1] - p1[1]]
        v2 = [p3[0] - p1[0], p3[1] - p1[1]]
        num = (v1[0] * v2[0] + v1[1] * v2[1])
        den = (ConvexHull.getLength(v1[0], v1[1]) * ConvexHull.getLength(v2[0], v2[1]))
        return np.arccos( num / den )

    def getDivided(points, direction=0, p1=None, pn=None):
        partition = []
        if p1 is None and pn is None:
            p1 = points[0]
            pn = points[-1]
        partition.append(p1)
        for point in points[1:-1]:
            determinant = ConvexHull.getPartition(p1, pn, point)
            if not direction and determinant > 0:
                partition.append(point)
            elif direction and determinant < 0:
                partition.append(point)
        partition.append(pn)
        return partition

    def pickFurthest(points):
        candidate = points[1]
        p1 = points[0]
        pn = points[-1]
        for point in points[2:-1]:
            d1 = ConvexHull.getDistance(p1, pn, candidate)
            d2 = ConvexHull.getDistance(p1, pn, point)
            if d1 < d2 or (d1 == d2 and ConvexHull.getAngle(p1, pn, candidate) < ConvexHull.getAngle(p1, pn, point)):
                candidate = point
        return candidate

    def getHull(self, points=None):
        if points is None:
            self.sortPoints()
            # Append Hullpoints in a clockwise manner
            self.hull.append(self.points[0])  # p1
            self.getHull(points=ConvexHull.getDivided(self.points, direction=0))  # left points
            self.hull.append(self.points[-1])  # pn
            self.getHull(points=ConvexHull.getDivided(self.points, direction=1))  # right points
        elif len(points) > 2:
            if len(points) == 3:
                self.hull.append(points[1])
            else:
                pmax = ConvexHull.pickFurthest(points)
                if ConvexHull.getPartition(points[0], points[-1], pmax) > 0:
                    self.getHull(points=ConvexHull.getDivided(points, direction=0, p1=points[0], pn=pmax)) # points left of p1-pmax
                    self.hull.append(pmax) # pmax
                    self.getHull(points=ConvexHull.getDivided(points, direction=1, p1=points[-1], pn=pmax)) # points right of pn-pmax
                else:
                    self.getHull(points=ConvexHull.getDivided(points, direction=0, p1=points[-1], pn=pmax)) #points left of pn-pmax
                    self.hull.append(pmax) #pmax
                    self.getHull(points=ConvexHull.getDivided(points, direction=1, p1=points[0], pn=pmax)) #points right of p1-pmax


if __name__ == "__main__":
    data = datasets.load_wine()
    # create a DataFrame
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    # visualisasi hasil ConvexHull
    plt.figure(figsize=(10, 6))
    colors = ['b', 'r', 'g']
    plt.title('Wine Alcohol vs Malic Acid')
    plt.xlabel(data.feature_names[0])
    plt.ylabel(data.feature_names[1])
    for i in range(len(data.target_names)):
        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:, [0, 1]].values
        hull = ConvexHull()
        for point in bucket:
            hull.add(point)
        hull.getHull()
        plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
        hx = [point[0] for point in hull.hull]
        hy = [point[1] for point in hull.hull]
        hx.append(hull.hull[0][0])
        hy.append(hull.hull[0][1])
        plt.plot(hx, hy, colors[i])
    plt.legend()
    plt.savefig('c:/Github/Tucil2_STIMA/test/Alcohol.png')
    plt.show()
