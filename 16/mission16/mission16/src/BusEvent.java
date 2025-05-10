/**
 * Contains information about a bus-related event.
 */
public class BusEvent implements Comparable<BusEvent> {

    public AbstractBus bus;
    public int time;
    public EventType eventType;

    /**
     * Constructs a `BusEvent` with a given bus and time. This constructor (i.e. one that takes in a time and bus) MUST
     * EXIST, though the constructor body can be modified if other instance variables are added subsequently.
     */
    public BusEvent(AbstractBus bus, int time) {
        this.bus = bus;
        this.time = time;
        this.eventType = EventType.OPERATIONAL;
    }

    // Method that compares one `BusEvent` with another to determine the ordering. The BusEvent with an earlier
    // timing, i.e. smaller `time` value should go first.
    @Override
    public int compareTo(BusEvent o) {
        // TODO: Implement this (Task 1a)
        return Integer.compare(this.time, o.time);
    }

    @Override
    public String toString() {
        // You may choose to implement this for Task 3b / Task 4b
        /* Get bus name string */
        String bus = null;
        if (this.bus instanceof BusA1) {
            bus = "A1";
        } else if (this.bus instanceof BusB1) {
            bus = "B1";
        } else if (this.bus instanceof BusC) {
            bus = "C";
        } else if (this.bus instanceof BusD1) {
            bus = "D1";
        }

        /* Get current stop name */
        String stop = this.bus.currentStopName;

        /* Get current time */
        int time = this.time;

        /* OPERATIONAL statement */
        if (this.eventType == EventType.OPERATIONAL) {
            return String.format("%d: Bus %s arrives at %s.", time, bus, stop);
        }
        /* BROKEN_DOWN statement */
        else if(this.eventType == EventType.BROKEN_DOWN) {
            return String.format("%d: Bus %s has broken down at %s.", time, bus, stop);
        }
        /* REPAIRED statement */
        else {
            return String.format("%d: Bus %s has been repaired at %s.", time, bus, stop);
        }
    }

}
