package setofstacks;

import java.util.ArrayList;
import java.util.Stack;

public class SetOfStacks {
    private int capacity;
    public ArrayList<Stack<Integer>> stacks;

    public SetOfStacks(int capacity) {
        this.capacity = capacity;
        this.stacks = new ArrayList<Stack<Integer>>();
    }

    public Stack<Integer> getLastStack() {
        if (this.stacks.size() == 0) {
            Stack<Integer> initStack = new Stack<Integer>();
            this.stacks.add(initStack);
            return initStack;
        } else {
            return this.stacks.get(this.stacks.size() - 1);
        }
    }

    public void push(int item) {
        Stack<Integer> lastStack = this.getLastStack();
        if (lastStack.size() < capacity) {
            lastStack.push(item);
        } else {
            Stack<Integer> newStack = new Stack<Integer>();
            newStack.push(item);
            this.stacks.add(newStack);
        }
    }

    public int pop() {
        Stack<Integer> lastStack = this.getLastStack();
        int popNum = lastStack.pop();
        if (lastStack.size() == 0) {
            this.stacks.remove(this.stacks.size() - 1);
        }
        return popNum;
    }
}
