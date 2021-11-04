package BaseClasses;

import Entities.*;
import java.util.*;

public class Tile {

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

}