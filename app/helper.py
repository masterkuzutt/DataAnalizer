
def map_index_to_value (index,levels,labels):
    """
    map 2D list of index  with 2D value list.specifically target
    pandas.DataFrame.index
    Args:
        - index:2D list of index 
        - labels:2D list of values colume 1D size should same with index
        - levels:len of 1D on index and labels.
    """
    label_list = []
    for i in range(len(labels)):
        data = []
        for label in labels[i]:
            data.append(levels[i][label])
        label_list.append(data)

    return label_list
