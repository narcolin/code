import java.util.List;
import java.util.LinkedList;
import java.util.*;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.Collections;
import java.util.PriorityQueue;

class AStarPathingStrategy implements PathingStrategy
{
    public List<Point> computePath(Point start, Point end,
                                   Predicate<Point> canPassThrough,
                                   BiPredicate<Point, Point> withinReach,
                                   Function<Point, Stream<Point>> potentialNeighbors)
    {
        List<Point> p = new LinkedList<>();
        PriorityQueue<Node> openQueue = new PriorityQueue<>();
        HashMap<Point, Node> openHash = new HashMap<>();
        HashMap<Point, Node> closed = new HashMap<>();

        Node node1 = new Node(start, 0);
        node1.setH(computeHelper(start, end));
        node1.setF(node1.getH());

        openQueue.add(node1);
        openHash.put(start, node1);

        while(!openQueue.isEmpty()){
            Node current = openQueue.peek();
            if (withinReach.test(current.getLocation(), end)){
                while (current.getPrevious() != null){
                    p.add(current.getLocation());
                    current = current.getPrevious();
                }
                Collections.reverse(p);
                return p;
            }
            List<Point> neighbors = potentialNeighbors.apply(current.getLocation())
                    .filter(canPassThrough).collect(Collectors.toList());
            for (Point point : neighbors){
                if (!closed.containsKey(point)){
                    double g = 1 + current.getG();
                    Node node2 = new Node(point, g);
                    if (openHash.containsKey(point)){
                        if (openHash.get(point).getG() > g){
                            node2.setPrevNode(current);
                            node2.setF(node2.getG() + node2.getH());
                            openQueue.remove(openHash.get(point));
                            openHash.remove(point);
                            openHash.put(point, node2);
                            openQueue.add(node2);
                        }
                    }
                    else{
                        node2.setH(computeHelper(point, end));
                        node2.setF(node2.getG() + node2.getH());
                        node2.setPrevNode(current);
                        if (openHash.containsKey(point)){
                            openQueue.remove(openHash.get(point));
                            openHash.remove(point);
                        }
                        openHash.put(point, node2);
                        openQueue.add(node2);
                    }
                }
            }
            openQueue.remove(current);
            closed.put(current.getLocation(), current);
        }
        return p;
    }
    public double computeHelper(Point start, Point end){
        return Math.hypot(start.getX() - end.getX(), start.getY() - end.getY());
    }
}