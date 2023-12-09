
import queue

my_priority_queue = queue.PriorityQueue()

element_to_add = (3, "kalluru")
my_priority_queue.put(element_to_add)

popped_element = my_priority_queue.get()

print("Original Priority Queue: ", list(my_priority_queue.queue))
print("Element Added: ", element_to_add)
print("Popped Element: ", popped_element)
