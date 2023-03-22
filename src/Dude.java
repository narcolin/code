// Done
// DudeFull
// DudeNotFull

import processing.core.PImage;
import java.util.List;
import java.util.function.BiPredicate;
import java.util.function.Predicate;

public abstract class Dude extends Actioned implements Move{
    protected int resourceLimit;
    protected int resourceCount;
    public int getResourceCount() {
        return resourceCount;
    }
    public int getResourceLimit() {
        return resourceLimit;
    }
    public void setResourceCount(int resourceCount) {
        this.resourceCount = resourceCount;
    }
    public static final String DUDE_KEY = "dude";
    public static final int DUDE_ACTION_PERIOD = 0;
    public static final int DUDE_ANIMATION_PERIOD = 1;
    public static final int DUDE_LIMIT = 2;
    public static final int DUDE_NUM_PROPERTIES = 3;

    public Dude(String id, Point position, List<PImage> images, int resourceLimit, int resourceCount, double actionPeriod, double animationPeriod) {
        super(id, position, images, actionPeriod, animationPeriod);
    }

    public Point nextPosition(WorldModel world, Point destPos) {
        PathingStrategy p = new AStarPathingStrategy();
        Predicate<Point> pred = x -> !world.isOccupied(x) && world.withinBounds(x);
        BiPredicate<Point, Point> biPred = (x, y) -> Point.adjacent(x, y);

        List<Point> points = p.computePath(super.getPosition(), destPos, pred, biPred, PathingStrategy.CARDINAL_NEIGHBORS);

        if (points.size() == 0){
            return super.getPosition();
        }
        return points.get(0);

//        int horiz = Integer.signum(destPos.getX() - this.getPosition().getX());
//        Point newPos = new Point(this.getPosition().getX() + horiz, this.getPosition().getY());
//
//        if (horiz == 0 || world.isOccupied(newPos) && (!(world.getOccupancyCell(newPos) instanceof Stump))) {
//            int vert = Integer.signum(destPos.getY() - this.getPosition().getY());
//            newPos = new Point(this.getPosition().getX(), this.getPosition().getY() + vert);
//
//            if (vert == 0 || world.isOccupied(newPos) && (!(world.getOccupancyCell(newPos) instanceof Stump))) {
//                newPos = this.getPosition();
//            }
//        }
//        return newPos;
    }

    public abstract boolean transform(WorldModel world, EventScheduler scheduler, ImageStore imageStore);

    public abstract boolean moveTo(WorldModel world, Entity target, EventScheduler scheduler);
}