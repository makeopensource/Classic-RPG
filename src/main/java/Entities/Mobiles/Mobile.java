package Entities.Mobiles;

import BaseClasses.Position;
import Entities.Entity;
import Entities.Item;
import BaseClasses.Direction;

import java.util.*;

public class Mobile extends Entity {
    public int health;
    public ArrayList<Item> Inventory;

    /** Default mobile constructor, yes it does nothing.**/
    public Mobile(){
        this.pathingQueue = null;
        this.position = null;
        this.health = 0;
        this.Inventory = null;
    }


    /**
     * @param startingHealth - Spawning a player with how much health.
     * @param startingInventory - Spawning a player with a specified inventory
     * @param startingPosition - Spawing a player with a specified position
     */
    public Mobile(int startingHealth, ArrayList<Item> startingInventory, Position startingPosition){
        super(startingPosition);
        this.health = startingHealth;
        this.Inventory = startingInventory;
    }



    /**
     * Calls move for the mobiles position(that class actually does the work
     * @return - Position object of the player
     */
    public Position getPosition(){
        return super.getPosition();
    }

    public void update(){

    }

}
