package BaseClasses;

import Entities.*;
import java.util.*;

public class Tile {

    int positionX, positionY;

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

    public Tile(int X, int Y){
        this.positionX = X;
        this.positionY = Y;
    }

    public int getPositionX(){
        return this.positionX;
    }
    public int getPositionY(){
        return this.positionY;
    }



}