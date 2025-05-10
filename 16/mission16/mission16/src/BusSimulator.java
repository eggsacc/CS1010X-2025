import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Random;
import java.util.Scanner;

/**
 * `BusSimulator` drives event simulation, i.e. both event processing and generation.
 */
public class BusSimulator {

    // Priority queue of events for the simulator to process.
    private final Queue<BusEvent> eventQueue = new PriorityQueue<>();

    // Pseudorandom number generator - DO NOT MODIFY THE SEED VALUE OF 999.
    private final Random random = new Random(999);

    /**
     * Constructs a `BusSimulator` with an event queue populated using the `busEvents` given.
     *
     * @param busEvents Events to populate the event queue with.
     */
    public BusSimulator(List<BusEvent> busEvents) {
        eventQueue.addAll(busEvents);
    }

    /**
     * Prints some simple status information about the simulator.
     */
    public void printStatus() {
        System.out.println("Bus simulator is ready!");
        System.out.println("There are a total of " + eventQueue.size() + " events.");
    }

    /**
     * Runs the simulator until the event queue has been emptied.
     */
    public void run() {
        // TODO: Implement this (Task 3b)
        while(!eventQueue.isEmpty()) {
            BusEvent event = eventQueue.poll();
            System.out.println(event.toString());
            int time = event.bus.moveToNextStop();
            if(time != -1) {
                BusEvent new_event = new BusEvent(event.bus, event.time + time);
                eventQueue.offer(new_event);
            }
            else {
                continue;
            }
        }
    }

    /**
     * Runs the simulator with a probability of bus breakdowns until the event queue has been emptied.
     * <p>
     * Uses the `random` initialised on top in `BusSimulator` for pseudorandom number generation.
     */
    public void runWithBreakdowns() {
        // TODO: Implement this (Task 4b)
        while(!eventQueue.isEmpty()) {
            BusEvent event = eventQueue.poll();
            System.out.println(event.toString());

            /* Event type: operational */
            if(event.eventType == EventType.OPERATIONAL) {
                /* Check for random breakdown */
                boolean breakdown = event.bus.didBreakdown(this.random);
                /* Bus broke down; generate breakdown event */
                if(breakdown) {
                    BusEvent breakdown_event = new BusEvent(event.bus, event.time + 1);
                    breakdown_event.eventType = EventType.BROKEN_DOWN;
                    eventQueue.offer(breakdown_event);
                }
                /* No breakdown; continue to next stop */
                else {
                    int time = event.bus.moveToNextStop();
                    if(time != -1) {
                        BusEvent new_event = new BusEvent(event.bus, event.time + time);
                        eventQueue.offer(new_event);
                    }
                }
            }
            /* Event type: broken down */
            else if(event.eventType == EventType.BROKEN_DOWN) {
                /* Generate repaired event 10 minutes later */
                BusEvent repair_event = new BusEvent(event.bus, event.time + 10);
                repair_event.eventType = EventType.REPAIRED;
                eventQueue.offer(repair_event);
            }
            /* Event type: repaired */
            else {
                int time = event.bus.moveToNextStop();
                /* Go to next stop */
                if(time != -1) {
                    BusEvent new_event = new BusEvent(event.bus, event.time + time);
                    new_event.eventType = EventType.OPERATIONAL;
                    eventQueue.offer(new_event);
                }
            }
        }
    }

    /**
     * Entry point to this program.
     */
    public static void main(String[] args) {
        List<BusEvent> busEvents = readBusEvents();
        BusSimulator simulator = new BusSimulator(busEvents);
        simulator.printStatus();
        simulator.runWithBreakdowns();
    }

    /**
     * Reads in input from the console and produces a list of `BusEvent`s. This method has been provided for you.
     *
     * @return List of `BusEvent`s.
     */
    public static List<BusEvent> readBusEvents() {
        Scanner sc = new Scanner(System.in);
        int numBuses = sc.nextInt();
        sc.nextLine();
        List<BusEvent> busEvents = new ArrayList<>();

        for (int i = 0; i < numBuses; i++) {
            String[] busLine = sc.nextLine().split(" ");
            AbstractBus bus;

            // NOTE: Do read up on switch statements if you're unsure of what they do!
            switch (busLine[0]) {
            case "A1":
                bus = new BusA1();
                break;
            case "B1":
                bus = new BusB1();
                break;
            case "C":
                bus = new BusC();
                break;
            case "D1":
                bus = new BusD1();
                break;
            default:
                continue;
            }

            BusEvent busEvent = new BusEvent(bus, Integer.parseInt(busLine[1]));
            busEvents.add(busEvent);
        }

        return busEvents;
    }
}
