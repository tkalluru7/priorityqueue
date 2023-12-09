import queue
my_queue = queue.Queue()

element_to_add = 4233345
my_queue.put(element_to_add)

popped_element = my_queue.get()

print("Original Queue: ", list(my_queue.queue))
print("Element Added: ", element_to_add)
print("Popped Element: ", popped_element)
