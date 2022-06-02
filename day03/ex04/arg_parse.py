import argparse
import os
import os.path


def is_valid_file(arg):
    if not os.path.exists(arg):
        raise argparse.ArgumentTypeError(f"The file {arg} does not exist")
    ext = os.path.splitext(arg)[1][1:]
    if ext != 'csv':
        raise argparse.ArgumentTypeError(f"The file {arg} is not a csv file")
    else:
        return arg


def arguments_parser():
    parser = argparse.ArgumentParser(usage='%(prog)s [--f] filepath [--m]'
                                           ' max_iter [--n] n_centroid',
                                     description='KMeans clustering')
    required_group = parser.add_argument_group(title='Required arguments')
    required_group.add_argument('-f', '--filepath',
                                type=lambda x: is_valid_file(x),
                                help='enter CSV filepath',
                                required=True)
    required_group.add_argument('-m', '--max_iter',
                                type=int,
                                default=20,
                                help='Enter max iterations',
                                # required=True
                                )
    required_group.add_argument('-n', '--n_centroid',
                                type=int,
                                # default=4,
                                help='Chose the number of centroids',
                                # required=True
                                )
    args = parser.parse_args()
    return args
