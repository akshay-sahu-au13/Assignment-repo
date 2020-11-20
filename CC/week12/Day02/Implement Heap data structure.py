## Implememntation of Heap:

def heapify(idx):

    global heap
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left >= len(heap) and right >= len(heap):
        return

    max_idx = idx

    if left < len(heap) and heap[left] > heap[max_idx]:
        max_idx = left

    if right < len(heap) and heap[right] > heap[max_idx]:
        max_idx = right

    if idx != max_idx:
        heap[max_idx],heap[idx] = heap[idx],heap[max_idx]
        heapify(max_idx)

def Pop_element():
    global heap
    heap[0],heap[-1] = heap[-1],heap[0]
    x = heap[-1]
    heap = heap[:-1]
    heapify(0)
    return x

def heap_sort():
    global heap
    while len(heap) != 0:
        print(Pop_element(), end = " ")

def build_heap():
    global heap

    for i in range(len(heap)-1,-1,-1):
        heapify(i)

if __name__ == "__main__":
    print("Enter the elements seperated by space: ",end = "")
    heap = list(map(int,input().split()))
    print("Before: ",heap)
    build_heap()
    print("After: ",heap)
    print("The Popped element is: ",Pop_element())
    print("After popping:", heap)
    print("The sorted array is: ",end = "")
    heap_sort()

