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
    }

    public Position getPosition(){
        return position;
    }

    public void setPosition(Position position){
        //Important that the address doesn't change but the values do
        this.position.set(position);
        this.position.getRegion().addEntity(this);
    }

    public void setPosition(int x, int y){
        this.position.setXY(x, y);
    }



    /**
     * Calls move for the mobiles position(that class actually does the work
     * @param direction - ENUM direction
     */
    public void move(Direction direction){
        position.move(this, direction);
    }


}