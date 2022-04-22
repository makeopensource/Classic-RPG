package BaseClasses;

import Entities.Entity;

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
        return this.y == other.y;
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

    //i have set the actually moving to private so you access it thought the general mathod
    /*
    This uses quite a naive system of just asking the tile itself if it is passable... in the future
    this will be implemented so that the tile is checked in conjunction with the players ability

    also inBounds MUST be first
     */
    private void moveNorth(Entity entity){
        if(isInBounds(this.x, this.y-1) && region.getTile(this.x, this.y-1).isPassable()) {
            region.getTile(x,y).removeEntity(entity);
            this.y = this.y - 1;
            region.getTile(x,y).addEntity(entity);
        }
    }

    private void moveEast(Entity entity){
        if (isInBounds(this.x + 1, this.y) && region.getTile(this.x + 1, this.y).isPassable()) {
            region.getTile(x,y).removeEntity(entity);
            this.x = this.x+1;
            region.getTile(x,y).addEntity(entity);
        }
    }

    private void moveSouth(Entity entity){
        if(isInBounds(this.x, this.y+1) && region.getTile(this.x, this.y+1).isPassable()){
            region.getTile(x,y).removeEntity(entity);
            this.y = this.y + 1;
            region.getTile(x,y).addEntity(entity);
        }
    }

    private void moveWest(Entity entity){
        if(isInBounds(this.x-1, this.y) && region.getTile(this.x-1, this.y).isPassable()) {
            region.getTile(x,y).removeEntity(entity);
            this.x = this.x - 1;
            region.getTile(x,y).removeEntity(entity);
        }
    }

    //honestly the move implementaiton is some of the worst code ive written to this date
    public void move(Entity entity, Direction direction){
        switch(direction){
            case NORTH:
                this.moveNorth(entity);
                break;
            case EAST:
                this.moveEast(entity);
                break;
            case SOUTH:
                this.moveSouth(entity);
                break;
            case WEST:
                this.moveWest(entity);
                break;
            }
    }

    private boolean isInBounds(int x,int y){
        return x >= 0 && y >= 0 && x < this.region.getWidth() && y < this.region.getHeight();
    }

    public Position(Region region, int x, int y){
        this.region = region;
        this.x = x;
        this.y = y;
    }
}