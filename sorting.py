import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Sorting algorithms
def bubble_sort(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
                swapped = True
                yield data

def selection_sort(data):
    n = len(data)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[i], data[min_index] = data[min_index], data[i]
            yield data

def insertion_sort(data):
    n = len(data)
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            yield data
        data[j + 1] = key
        yield data

# Function to generate random data and sort it based on the selected algorithm
def sort_data(algorithm):
    data = np.random.randint(1, 100, size=20)  # Random data for sorting
    if algorithm == 'Bubble Sort':
        sort_animation(data, bubble_sort, "Bubble")
    elif algorithm == 'Selection Sort':
        sort_animation(data, selection_sort, "Selection")
    elif algorithm == 'Insertion Sort':
        sort_animation(data, insertion_sort, "Insertion")

# Function to visualize sorting animation
def sort_animation(data, sort_algorithm, algorithm_name):
    generator = sort_algorithm(data.copy())
    fig, ax = plt.subplots()
    ax.set_title(f"{algorithm_name} Sort")

    bar_rects = ax.bar(range(len(data)), data, align="edge")

    iteration = [0]
    def update_fig(data, rects, iteration):
        for rect, val in zip(rects, data):
            rect.set_height(val)
        iteration[0] += 1
        ax.set_title(f"{algorithm_name} Sort - Iteration {iteration[0]}")

    anim = animation.FuncAnimation(fig, update_fig, frames=generator, fargs=(bar_rects, iteration), repeat=False)
    plt.show()

# Create GUI
root = tk.Tk()
root.title("Sorting Algorithm Visualization")

# Function to handle button click
def button_click(algorithm):
    sort_data(algorithm)

# Create buttons for each sorting algorithm
algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
for algorithm in algorithms:
    button = tk.Button(root, text=algorithm, command=lambda alg=algorithm: button_click(alg))
    button.pack(pady=20)
    

root.mainloop()
