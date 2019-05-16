from Compsci_II.Lectures.week2.queue import Queue

# or use QueueADT_v1

A48_waiting_list = Queue()

# John tries to register for A48 but no room is available. so he goes to the waiting list
A48_waiting_list.enqueue("John")
print(A48_waiting_list._queue)

# Jane tries to register for A48 but no room is available. so she goes to the waiting list
A48_waiting_list.enqueue("Jane")
print(A48_waiting_list._queue)

# Rose tries to register for A48 but no room is available. so she goes to the waiting list
A48_waiting_list.enqueue("Rose")
print(A48_waiting_list._queue)
print(A48_waiting_list.size())

# How many people are in the Queue
print("The number of people in the queue is " + str(A48_waiting_list.size()))

# somebody who didn't passed A08, was removed from the course so one room is avialable
# FIFO rule, lets John register for the course and then remove him from the queue

# who is in front of the queue?
print(A48_waiting_list.front())
A48_waiting_list.dequeue()
print(A48_waiting_list._queue)

# two more rooms are avialble
A48_waiting_list.dequeue()
A48_waiting_list.dequeue()
print(A48_waiting_list._queue)

# This would raise an exception becuase the queue is empty
# A48_waiting_list.dequeue()

if A48_waiting_list.is_empty:
    print("Nobody is in the waitinig list")
else:
    A48_waiting_list.dequeue()
