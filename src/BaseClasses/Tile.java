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
        this.listOfEntities = entities;
    }

    public Tile(){
        this.listOfEntities = new ArrayList<>();
    }

    public Tile(Region region, int X, int Y){
        pos = new Position(region, X, Y);
    }

    public Tile(Region region, Position pos_arg){
        pos = pos_arg;
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

}