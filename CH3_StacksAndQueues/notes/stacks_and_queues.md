## Chapter 3: Stacks and Queues:
---
3.1) Describe how you could use a single array to implement three stacks.

_A capacity can be specified for the stacks to be implemented. Then an array can be initialized with the size of 3 times the capacity. From there, the array can have methods implemented on it to target a specific stacks internally and then perform operations on it._

3.2) How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop, and min should all operate in O(1) time.

_Review the python file stack_w_min.py_

3.3) Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely star
     a new stack when the previous stack exceeds some threshold. Implements a data structure SetOfStacks that mimics this.
     SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity.
     SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack (that is, pop() should return the same values
     as it would if there is just a single stack). Implement a function popAt(int index) which performs a pop operation on a specific substack.

_Review the Java project called SetOfStacks_

3.4) Implement a MyQueue class which implements a queue using two stacks.

_You could utilize two stacks where the initial stack could push items in order to the second stack. Essentially this would reverse the order allowing us to get a FIFO representation from the two LIFO stacks, effectively giving us a queue._

3.5) Write a program to sort a stack such that the smallest items are on the top. You can use an additional temporary stack.
     But, you may not copy element into any other data structure (like an array). The stack supports the following operations:
     push, pop, peek, and isEmpty.

_You could use a secondary stack to do this. Essentially peeking the top of the sorted stack and the original stack. If the value from the original stack is less, pop the item and put it on the sorted stack. Else, pop both items and push them in min-first order onto the sorted stack._

3.6) An animal shelter, which holds only dogs and cats, operates on a strictly "first in, first out" basis. People must either adopt
     the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they can select
     whether they would prefer a dog or a cat and they will receive the oldest animal of that type.
     They cannot select which specific animal they would like. Create the data structures to maintain this system and implement
     operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in LinkedList data structure.

_This could be implemented by creating two queues. One would store dogs and the other cats. The oldest animals (in terms of arrival time) would be the first items to remove from each queue. So for dequeing any, you could grab the oldest cat and dog and give the oldest of the two._
_If they choose a specific type of animal, you would just dequeue from the queue matching the animal type and return it._
