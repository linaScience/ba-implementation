#!/usr/bin/env python3
import os
import csv
from collections import Counter

def count_files(directory):
    count = 0
    for site, floor, files in os.walk(directory):
        count += len(files)
    return count

def find_directory_with_most_files(train_dir):
    max_count = 0
    max_site = ""
    max_directory = ""
    floor_counts = {}  # Dictionary to store floor counts for each site

    for site in os.listdir(train_dir):
        site_path = os.path.join(train_dir, site)
        if not os.path.isdir(site_path):
            continue

        floor_count = 0  # Initialize the floor count for each site

        for floor in os.listdir(site_path):
            if floor != "F1_filtered" and floor != "F1_csv":
                directory_path = os.path.join(site_path, floor)
                if not os.path.isdir(directory_path):
                    continue

                floor_count += 1  # Increment the floor count for the current site

                file_count = count_files(directory_path)
                if file_count > max_count:
                    max_count = file_count
                    max_site = site
                    max_directory = floor

        floor_counts[site] = floor_count  # Store the floor count for the current site

    return max_site, max_directory, max_count, floor_counts

def calculate_average_floor_count(floor_counts):
    total_floors = sum(floor_counts.values())
    num_sites = len(floor_counts)
    average_floor_count = total_floors / num_sites
    return average_floor_count

def get_min_max_floor_counts(floor_counts):
    min_floor_count = min(floor_counts.values())
    max_floor_count = max(floor_counts.values())
    return min_floor_count, max_floor_count

def calculate_median_floor_count(floor_counts):
    sorted_floor_counts = sorted(floor_counts.values())
    num_sites = len(sorted_floor_counts)
    middle_index = num_sites // 2

    if num_sites % 2 == 0:
        median_floor_count = (sorted_floor_counts[middle_index - 1] + sorted_floor_counts[middle_index]) / 2
    else:
        median_floor_count = sorted_floor_counts[middle_index]

    return median_floor_count

def calculate_files_per_floor(train_dir):
    files_per_floor = []  # List to store the number of files per floor

    for site in os.listdir(train_dir):
        site_path = os.path.join(train_dir, site)
        if not os.path.isdir(site_path):
            continue

        for floor in os.listdir(site_path):
            if floor != "F1_filtered" and floor != "F1_csv":
                directory_path = os.path.join(site_path, floor)
                if not os.path.isdir(directory_path):
                    continue

                file_count = count_files(directory_path)
                files_per_floor.append(file_count)

    return files_per_floor

def calculate_median(data):
    sorted_data = sorted(data)
    num_items = len(sorted_data)
    middle_index = num_items // 2

    if num_items % 2 == 0:
        median_value = (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
    else:
        median_value = sorted_data[middle_index]

    return median_value

def find_smallest_files(directory, num_files=5):
    smallest_files = []
    smallest_sizes = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":
                continue

            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if "F1_filtered" in file_path:
                continue

            if len(smallest_files) < num_files:
                smallest_files.append(file_path)
                smallest_sizes.append(file_size)
            else:
                # Sort the smallest_files and smallest_sizes in ascending order based on file size
                sorted_indices = sorted(range(len(smallest_sizes)), key=lambda k: smallest_sizes[k])
                smallest_files = [smallest_files[i] for i in sorted_indices]
                smallest_sizes = [smallest_sizes[i] for i in sorted_indices]

                # Check if the current file is smaller than the largest among the smallest files
                if file_size < smallest_sizes[-1]:
                    smallest_files[-1] = file_path
                    smallest_sizes[-1] = file_size

    return smallest_files, smallest_sizes

def find_biggest_files(directory, num_files=5):
    biggest_files = []
    biggest_sizes = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file == ".DS_Store":  # Exclude .DS_Store files
                continue

            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)

            if "F1_filtered" in file_path:
                continue

            if len(biggest_files) < num_files:
                biggest_files.append(file_path)
                biggest_sizes.append(file_size)
            else:
                sorted_indices = sorted(range(len(biggest_sizes)), key=lambda k: biggest_sizes[k], reverse=True)
                biggest_files = [biggest_files[i] for i in sorted_indices]
                biggest_sizes = [biggest_sizes[i] for i in sorted_indices]

                if file_size > biggest_sizes[-1]:
                    biggest_files[-1] = file_path
                    biggest_sizes[-1] = file_size

    return biggest_files, biggest_sizes

train_directory = "/Users/lina/Desktop/ba-implementation/train/"
max_site, max_directory, max_count, floor_counts = find_directory_with_most_files(train_directory)

average_floor_count = calculate_average_floor_count(floor_counts)
min_floor_count, max_floor_count = get_min_max_floor_counts(floor_counts)
median_floor_count = calculate_median_floor_count(floor_counts)

files_per_floor = calculate_files_per_floor(train_directory)
average_files_per_floor = sum(files_per_floor) / len(files_per_floor)
min_files_per_floor = min(files_per_floor)
max_files_per_floor = max(files_per_floor)
median_files_per_floor = calculate_median(files_per_floor)

smallest_file, smallest_size = find_smallest_files(train_directory)
biggest_file, biggest_size = find_biggest_files(train_directory)

print(f"Site with most files: {max_site}, Directory: {max_directory}, File Count: {max_count}")
print(f"Average floor count: {average_floor_count}")
print(f"Minimum floor count: {min_floor_count}")
print(f"Maximum floor count: {max_floor_count}")
print(f"Median floor count: {median_floor_count}")
print(f"Average files per floor: {average_files_per_floor}")
print(f"Minimum files per floor: {min_files_per_floor}")
print(f"Maximum files per floor: {max_files_per_floor}")
print(f"Median files per floor: {median_files_per_floor}")
print(f"Smallest file: {smallest_file}, Size: {smallest_size} bytes")
print(f"Biggest file: {biggest_file}, Size: {biggest_size} bytes")