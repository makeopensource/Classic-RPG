package BaseClasses;

public class Position {
    
    private Region region;
    private int x, y;

    @Override
    public boolean equals(Object o){
        if (this == o) return true;
       
        if (!(o instanceof Position)) return false;

        Position other = (Position)(o);

        if (this.region != other.region) return false;
        if (this.x != other.x) return false;
        if (this.y != other.y) return false;
       
        return true;
    }

    public void set(Position position){
        this.region = position.region;
        this.x = position.x;
        this.y = position.y;
    }

    public void setRegion(Region region){
        this.region = region;
    }

    public Region getRegion(){
        return region;
    }

    public void setX(int x){
        this.x = x;
    }

    public int getX(){
        return x;
    }

    public void setY(int y){
        this.y = y;
    }

    public int getY(){
        return y;
    }

    public void setXY(int x, int y){
        this.x = x;
        this.y = y;
    }

    public Position(Region region, int x, int y){
        this.region = region;
        this.x = x;
        this.y = y;
    }
}