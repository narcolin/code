public final class Event {
    private Action action;
    private double time;
    private Entity entity;

    public Event(Action action, double time, Entity entity) {
        this.action = action;
        this.time = time;
        this.entity = entity;
    }

    public Entity getEntity() {
        return entity;
    }

    public Action getAction() {
        return action;
    }

    public double getTime() {
        return time;
    }
}