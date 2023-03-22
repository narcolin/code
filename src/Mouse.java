import processing.core.PImage;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.function.Predicate;

public class Mouse extends Actioned implements Move {
    public static final String MOUSE_KEY = "mouse";
    public static final int MOUSE_ANIMATION_PERIOD = 0;
    public static final int MOUSE_ACTION_PERIOD = 1;
    public static final int MOUSE_LIMIT= 1;

    public Mouse(String id, Point p, List<PImage> images, double actionPeriod, double animationPeriod, int resourceLimit) {
        super(id, p, images, actionPeriod, animationPeriod);
    }

    public boolean moveTo(WorldModel world, Entity entity, EventScheduler scheduler) {
        if (this.position.adjacent(entity.position, entity.position)) {
            world.removeEntity(scheduler, entity);
            return true;
        } else {
            Point nextPos = this.nextPosition(world, entity.position);

            if (!this.position.equals(nextPos)) {
                world.moveEntity(scheduler, this, nextPos);
            }
            return false;
        }
    }

    public Point nextPosition(WorldModel world, Point destPos) {
        AStarPathingStrategy pathingStrategy = new AStarPathingStrategy();
        List<Point> path = pathingStrategy.computePath(position, destPos,
                p -> world.withinBounds(p) && !world.isOccupied(p),
                Point::adjacent,
                PathingStrategy.CARDINAL_NEIGHBORS);

        if (path.size() >= 1) {
            return path.get(0);
        } else {
            return position;
        }
    }

    public void executeActivity(WorldModel world, ImageStore imageStore, EventScheduler scheduler) {
        List<Entity> targetEntities = new ArrayList<>();
        targetEntities.add(new Mouse("mouse", position, imageStore.getImageList("cow"), MOUSE_ACTION_PERIOD, MOUSE_ANIMATION_PERIOD, MOUSE_LIMIT));
        Optional<Entity> fullTarget = world.findNearest(position, (Predicate<Entity>) targetEntities);

        if (fullTarget.isEmpty()) {
            transform(world, scheduler, imageStore);
        } else {
            scheduler.scheduleEvent(this, ActivityAction.createActivityAction(this, world, imageStore), actionPeriod);
        }
    }

    public void transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore) {
        Cow cow = (Cow) Cow.createCow(id, position, actionPeriod, animationPeriod, 3, images);

        world.removeEntity(scheduler, this);

        world.addEntity(cow);
        scheduleActions(scheduler, world, imageStore);
    }
    public static Mouse createMouse(String id, Point p, double actionPeriod, double animationPeriod, int resourceLimit, List<PImage> images) {
        return new Mouse(id, p , images, MOUSE_ACTION_PERIOD, MOUSE_ANIMATION_PERIOD, MOUSE_LIMIT);
    }
}