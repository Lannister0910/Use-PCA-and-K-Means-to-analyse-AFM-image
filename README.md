# Use-PCA-and-K-Means-to-analyse-AFM-image
1.整体程序运行需要加载pycroscopy库和pyUSID库，可以通过Anaconda进行加载，或者登陆官网按照参考步骤进行加载https://pycroscopy.github.io/pycroscopy/.

one.The overall program operation needs to load the pycroscopy library and the pyUSID library, which can be loaded by Anaconda, or log in to the official website and follow the steps to load https://pycroscopy.github.io/pycroscopy/

2.这个项目包含一个PCA的简单程序、一个K-Means的简单程序、原子力显微镜压电激发响应的原始HDF5数据文件、使用PCA，K-Means对原子力显微镜压电激发响应的处理程序.

two.This project contains a simple program of PCA, a simple program of K-Means, the original HDF5 data file of piezoelectric excitation response of atomic force microscope, and the processing procedure of piezoelectric excitation response of atomic force microscope using PCA and K-Means.

3.使用者需要更改原子力显微镜压电激发响应的原始HDF5数据文件的引用路径.

three.The user needs to change the reference path of the original HDF5 data file for the piezoelectric excitation response of the AFM.

4.由于每次运行程序都会把PCA和K-Means运行后的结果重新存入原子力显微镜压电激发响应的原始HDF5数据文件中，所欲注意多备份几个原子力显微镜压电激发响应的原始HDF5数据文件.

four.Since each running program will re-store the results of PCA and K-Means after running into the original HDF5 data file of the piezoelectric excitation response of the atomic force microscope, it is necessary to pay attention to the original HDF5 data file of the piezoelectric excitation response of several atomic force microscopes. .
