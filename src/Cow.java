import processing.core.PImage;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.function.BiPredicate;
import java.util.function.Predicate;
public class Cow extends Actioned implements Move{
    public static final int COW_NUM_PROPERTIES = 3;
    public static final String COW_KEY = "cow";
    public static final int COW_ANIMATION_PERIOD = 2;
    public static final int COW_ACTION_PERIOD = 3;
    public static final int COW_LIMIT = 2;
    public Cow(String id, Point p, List<PImage> images, double actionPeriod, double animationPeriod, int resourceLimit){
        super(id, p, images, actionPeriod, animationPeriod);
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler) {
        Optional<Entity> cowTarget = world.findNearest(this.getPosition(), ((entity -> entity instanceof Tree))); //new ArrayList<>(List.of(EntityKind.STUMP)));

        if (cowTarget.isPresent()) {
            Point tgtPos = cowTarget.get().getPosition();

            if (this.moveTo(world, cowTarget.get(), scheduler)) {

                Mouse mouse = new Mouse("mouse", tgtPos, imageStore.getImageList("cow"), Mouse.MOUSE_ACTION_PERIOD, Mouse.MOUSE_ANIMATION_PERIOD, Mouse.MOUSE_LIMIT);

                world.addEntity(mouse);
                mouse.scheduleActions(scheduler, world, imageStore);
            }
        }
    }
    public boolean moveTo(WorldModel world, Entity target, EventScheduler scheduler) {
        if (Point.adjacent(this.getPosition(), target.getPosition())) {
            world.removeEntity(scheduler, target);
            return true;
        } else {
            Point nextPos = nextPosition(world, (target).getPosition());

            if (!this.getPosition().equals(nextPos)) {
                world.moveEntity(scheduler, this, nextPos);
            }
            return false;
        }
    }

    public Point nextPosition(WorldModel world, Point destPos) {
        AStarPathingStrategy pathingStrategy = new AStarPathingStrategy();
        List<Point> path = pathingStrategy.computePath(position, destPos,
                p -> world.withinBounds(p) && (!world.isOccupied(p) || ((world.isOccupied(p)) && (world.getOccupancyCell(p) instanceof Stump))),
                Point::adjacent,
                PathingStrategy.CARDINAL_NEIGHBORS);
        if (path.isEmpty()) {
            return position;
        }
        Point nextPos = path.get(0);
        if (world.isOccupied(nextPos) && !(world.getOccupancyCell(nextPos) instanceof Stump)) {
            return position;
        }
        return nextPos;
    }
    public static Entity createCow(String id, Point p, double actionPeriod, double animationPeriod, int resourceLimit, List<PImage> images) {
        return new Cow(id, p , images, COW_ACTION_PERIOD, COW_ANIMATION_PERIOD, COW_LIMIT);
    }
}