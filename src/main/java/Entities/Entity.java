package Entities;

import BaseClasses.Direction;
import BaseClasses.Position;
import BaseClasses.Region;

public class Entity {

    private Position position;

    //Constructor for using reference (equipped/held items)
    public Entity(Position position){
        this.position = position;
    }

    public Entity(Region region, int x, int y){
        this.position = new Position(region, x, y);
        this.position.getRegion().addEntity(this);
        this.position.getRegion().getTile(position).addEntity(this);
    }

    public Position getPosition(){
        return position;
    }

    public void setPosition(Position position){
        //Important that the address doesn't change but the values do
        this.position.getRegion().getTile(position).removeEntity(this);
        this.position.set(position);
        this.position.getRegion().addEntity(this);
        this.position.getRegion().getTile(position).addEntity(this);
    }

    public void setPosition(int x, int y){
        this.position.getRegion().getTile(position).removeEntity(this);
        this.position.setXY(x, y);
        this.position.getRegion().getTile(position).addEntity(this);
    }


    /**
     * Calls move for the mobiles position(that class actually does the work
     * @param direction - ENUM direction
     */
    public void move(Direction direction){
        position.move(this, direction);
    }

}