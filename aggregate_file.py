#!/usr/bin/env python3

import os

def merge_sorted_files(files):
    open_files = [open(f, 'r') for f in files]
    lines = [f.readline().strip() for f in open_files]
    aggregated_content = []

    while any(lines):
        smallest = min(line for line in lines if line)
        smallest_index = lines.index(smallest)
        aggregated_content.append(smallest)
        lines[smallest_index] = open_files[smallest_index].readline().strip()

    for f in open_files:
        f.close()

    return '\n'.join(aggregated_content)

def aggregate_txt_files_in_floor_folders(train_folder):
    for dirpath, _, filenames in os.walk(train_folder):
        txt_files = [os.path.join(dirpath, fname) for fname in filenames if fname.endswith('.txt')]
        
        # If this directory contains .txt files, it's considered a floor_folder
        if txt_files:
            aggregated_content = merge_sorted_files(txt_files)
        
            with open(os.path.join(dirpath, 'aggregated.txt'), 'w') as out_file:
                out_file.write(aggregated_content)

root_folder = "/Users/lina/Desktop/ba-implementation/"
train_folder = os.path.join(root_folder, "train")
aggregate_txt_files_in_floor_folders(train_folder)