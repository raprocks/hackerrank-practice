def print_rangoli(size):
    alphabets = [chr(i) for i in range(97, 123)]
    height = (size*2) - 1

    # mid label
    mid_label = []
    for i in range(size-1, 0, -1):
        mid_label.append(alphabets[i])
    for i in range(0, size):
        mid_label.append(alphabets[i])
    mid_label = '-'.join(mid_label)
    width = len(mid_label)
    labels = []
    # top label
    for i in range(height//2):
        curr_label = '-'
        curr_label_list = []
        for char_idx in range(size-1, size-1-i, -1):
            curr_label_list.append(alphabets[char_idx])
        for char_idx in range(size-1-i, size, 1):
            curr_label_list.append(alphabets[char_idx])
        curr_label = curr_label.join(curr_label_list)
        curr_label = curr_label.center(width, '-')
        labels.append(curr_label)
    # make a copy for bottom part and reverse it
    labels_copy = labels.copy()
    labels_copy.reverse()

    labels.append(mid_label)
    labels = labels + labels_copy

    print('\n'.join(labels))
