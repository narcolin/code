public class Node implements Comparable<Node> {

    private Point location;
    private double g;
    private double h;
    private double f;
    private Node previous;

    public Node(Point location, double g){
        this.location = location;
    }

    public void setH(double h) {
        this.h = h;
    }

    public void setF(double f) {
        this.f = f;
    }

    public void setPrevNode(Node previous){
        this.previous = previous;
    }

    public double getG(){
        return g;
    }

    public double getH(){
        return h;
    }

    public Node getPrevious(){
        return previous;
    }

    public Point getLocation(){
        return location;
    }

    @Override
    public int compareTo(Node n){
        if (f < n.f){
            return -1;
        }
        else if(f > n.f){
            return 1;
        }
        return 0;
    }

}