import dlib
from skimage import io, transform
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob
import openface
import pickle
import os
import sys
import argparse
import time
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder