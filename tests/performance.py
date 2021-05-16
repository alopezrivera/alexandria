import timeit
import numpy as np


def yaml_parser():
    v_n = np.arange(1, 1000, 1)
    v_r = np.array(np.zeros(v_n.shape),
                   np.zeros(v_n.shape))
    for n in v_n:
        print(timeit.timeit("yaml.safe_load(open('publication.yaml').read())", setup="import yaml", number=10000))
        print(timeit.timeit("yaml_parser('publication.yaml')", setup="from __main__ import yaml_parser", number=10000))
