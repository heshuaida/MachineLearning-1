import cv2

from Zhihu.NN.Util import DataUtil
from NN.Basic.Networks import *
from CvDTree.CvDTree import *


def cv2_example():
    pass


def visualize_nn():
    x, y = DataUtil.gen_spin()
    nn = NNDist()
    nn.add("ReLU", (x.shape[1], 24))
    nn.add("ReLU", (24,))
    nn.add("Softmax", (y.shape[1],))
    nn.fit(x, y, epoch=1000, draw_detailed_network=True)


def visualize_tree():
    data, x, y = [], [], []
    with open("../CvDTree/data.txt", "r") as _file:
        for _line in _file:
            data.append(_line.split(","))
    np.random.shuffle(data)
    for _line in data:
        y.append(_line.pop(0))
        x.append(list(map(lambda c: c.strip(), _line)))
    x, y = np.array(x), np.array(y)

    _tree = C45Tree()
    _tree.fit(x, y)
    _tree.draw()

if __name__ == '__main__':
    cv2_example()
    visualize_nn()
    visualize_tree()
