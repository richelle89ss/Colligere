import java.util.Stack;

/**
 * This implements Queue using two Stacks.
 *
 * Big O Runtime:
 *      insert(): O(1)
 *      remove(): O(1) amortized
 *      isEmpty(): O(1)
 *
 * A queue data structure functions the same as a real world queue.
 * The elements that are added first are the first to be removed.
 * New elements are added to the back/rear of the queue.
 *
 *
 */
class QueueWithStack {

    // Stack to keep track of elements inserted into the queue
    private Stack inStack;
    // Stack to keep track of elements to be removed next in queue
    private Stack outStack;

    /**
	 * Constructor
	 */
    public QueueWithStack() {
        this.inStack = new Stack();
        this.outStack = new Stack();
    }

    /**
     * Inserts an element at the rear of the queue
     *
     * @param x element to be added
     */
    public void insert(Object x) {
        // Insert element into inStack
        this.inStack.push(x);
    }

    /**
     * Remove an element from the front of the queue
     *
     * @return the new front of the queue
     */
    public Object remove() {
        if(this.outStack.isEmpty()) {
            // Move all elements from inStack to outStack (preserving the order)
            while(!this.inStack.isEmpty()) {
                this.outStack.push( this.inStack.pop() );
            }
        }
        return this.outStack.pop();
    }

    /**
     * Returns true if the queue is empty
     *
     * @return true if the queue is empty
     */
    public boolean isEmpty() {
        return (this.inStack.isEmpty() && this.outStack.isEmpty());
    }

}

/**
 * This class is the example for the Queue class
 *
 */
public class QueueUsingTwoStacks {

    /**
     * Main method
     *
     * @param args Command line arguments
     */
    public static void main(String args[]){
        QueueWithStack myQueue = new QueueWithStack();
        myQueue.insert(1);
        // instack: [(top) 1]
        // outStack: []
        myQueue.insert(2);
        // instack: [(top) 2, 1]
        // outStack: []
        myQueue.insert(3);
        // instack: [(top) 3, 2, 1]
        // outStack: []
        myQueue.insert(4);
        // instack: [(top) 4, 3, 2, 1]
        // outStack: []

        System.out.println(myQueue.isEmpty()); //Will print false

        System.out.println(myQueue.remove()); //Will print 1
        // instack: []
        // outStack: [(top) 2, 3, 4]

        myQueue.insert(5);
        // instack: [(top) 5]
        // outStack: [(top) 2, 3, 4]

        myQueue.remove();
        // instack: [(top) 5]
        // outStack: [(top) 3, 4]
        myQueue.remove();
        // instack: [(top) 5]
        // outStack: [(top) 4]
        myQueue.remove();
        // instack: [(top) 5]
        // outStack: []
        myQueue.remove();
        // instack: []
        // outStack: []

        System.out.println(myQueue.isEmpty()); //Will print true
	    
	    //End of code

    }
}
