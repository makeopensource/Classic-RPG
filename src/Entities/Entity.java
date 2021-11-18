package Entities;

import BaseClasses.Position;
import BaseClasses.Region;

public class Entity {

    private Position position;

    public Position getPosition(){
        return position;
    }

    public void setPosition(Position position){
        //Important that the address doesn't change but the values do
        this.position.set(position);
    }

    public void setPosition(int x, int y){
        this.position.setXY(x, y);
    }

    //Constructor for using reference (equipped/held items)
    public Entity(Position position){   
        this.position = position;
    }

    public Entity(Region region, int x, int y){
        this.position = new Position(region, x, y);
    }


}