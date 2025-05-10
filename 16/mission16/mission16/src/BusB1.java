import java.util.Random;

/**
 * Represents the NUS Bus B1.
 */
public class BusB1 extends AbstractBus {

    public BusB1() {
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("B1", null);
        assert pair != null;
        currentStopName = pair.stopName; // assigns to superclass' `stopName`
    }

    /**
     * Moves the bus to next stop and returns the amount of time spent moving. If the bus is already at its final stop,
     * return -1.
     *
     * @return The amount of time spent moving if the bus is not at its final stop; else, -1.
     */
    @Override
    public int moveToNextStop() {
        // TODO: Implement this (Task 2a)
        BusMap.Pair pair = BusMap.getNextStopAndTimeTaken("B1", currentStopName);

        /* pair -> null: final stop reached */
        if(pair == null) {
            return -1;
        }
        else {
            currentStopName = pair.stopName;
            return pair.timeTakenFromPreviousStop;
        }
    }

    // Bus B1 should breakdown with a probability of 0.2
    @Override
    public boolean didBreakdown(Random random) {
        // TODO: Implement this (Task 4a)
        return random.nextDouble() < 0.2;
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b
        return null;
    }

}
