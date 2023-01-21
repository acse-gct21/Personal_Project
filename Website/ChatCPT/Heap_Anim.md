# Heap Animation

This repository contains an animation of the heap sorting algorithm.

## Running the Animation

1. Clone the repository:

'''git clone https://github.com/acse-gct21/Personal_Project.git'''

2. Install the required dependencies

''' pip install -r requirements.txt

# Heap Algorithm

A heap is a special type of binary tree that satisfies the heap property. The heap property states that the value of each node must be greater than or equal to the values of its children (for a max-heap) or less than or equal to the values of its children (for a min-heap).

Heap algorithms are a group of algorithms that operate on heaps. The most common heap algorithm is heap sort, which is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements.

# Goal of the Animation

The goal of the animation is to visualize the process of heap sort. Heap sort is an efficient sorting algorithm that uses a binary heap data structure to sort elements. The animation shows the steps of the algorithm, starting with an unsorted array and ending with a sorted array. The animation highlights the value that is about to be swapped before it is swapped, making it easier to understand the algorithm.

# Things That Can Be Improved

Speed: Depending on the size of the heap and the complexity of the visualization, generating a new image for each frame of the animation can be slow. Reusing the same figure, graph, and animation object can help speed up the animation.

Layout algorithm: NetworkX provides several different layout algorithms for positioning nodes in a graph. Some algorithms, such as the spring layout, can be slower than others. By experimenting with different layout algorithms, you may be able to find one that is faster for your specific use case.

Heap implementation: If the heap sort algorithm is the bottleneck of your code, you may want to consider implementing a more efficient heap, such as a Fibonacci heap or a pairing heap.

Graph drawing library: NetworkX uses Matplotlib for drawing graphs, which can be slow for large or complex graphs. There are other libraries, such as Plotly or Pyvis, which can be faster for certain use cases.

Animation: Instead of creating a gif, the animation can be made interactive and can be shown in real-time.

Please let me know if you have any other questions or if you need any other information to be added in the README file.