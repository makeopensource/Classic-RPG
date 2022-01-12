package BaseClasses;

import Entities.*;
import java.util.*;
import BaseClasses.Position;
import BaseClasses.Region;

public class Tile {

    public Position pos;

    private ArrayList<Entity> listOfEntities;

    public void setEntities(ArrayList<Entity> entities){
        this.listOfEntities = entities;
    }

    public ArrayList<Entity> getEntities(){
        return this.listOfEntities;
    }

    public Tile(ArrayList<Entity> entities){
        pos = null;
        this.listOfEntities = entities;
    }

    public Tile(){
        pos = null;
        this.listOfEntities = new ArrayList<>();
    }

    public Tile(Region region, int X, int Y){
        pos = new Position(region, X, Y);
        this.listOfEntities = new ArrayList<>();
    }

    public Tile(Position pos_arg){
        pos = pos_arg;
        this.listOfEntities = new ArrayList<>();
    }

    public Tile(Region region, int X, int Y, ArrayList<Entity> entities){
        pos = new Position(region, X, Y);
        this.listOfEntities = entities;
    }

    public Tile(Position pos_arg, ArrayList<Entity> entities){
        pos = pos_arg;
        this.listOfEntities = entities;
    }

    @Override
    public boolean equals(Object o){
        if (this == o) return true;

        if (!(o instanceof Tile)) return false;

        Tile other = (Tile)(o);

        return this.pos == other.pos;
    }

    public void addEntity(Entity nE){
        listOfEntities.add(nE);
    }

    public int getPositionX(){
        return this.pos.getX();
    }

    public int getPositionY(){
        return this.pos.getY();
    }

    public Region getRegion(){
        return this.pos.getRegion();
    }

    public void setPositionX(int x){
        this.pos.setX(x);
    }

    public void setPositionY(int y){
        this.pos.setY(y);
    }

    public void setPositionXY(int x, int y){
        this.pos.setXY(x, y);
    }

    public void setRegion(Region reg){
        this.pos.setRegion(reg);
    }

    public void setPosition(Position pos){
        this.pos = pos;
    }

}