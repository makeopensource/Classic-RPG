package Entities.Mobiles;

import BaseClasses.Position;
import Entities.Item;
import BaseClasses.Direction;

import java.util.*;

public class Mobile{
    public final List<Position> pathingQueue;
    public Position position;
    public int health;
    public ArrayList<Item> Inventory;


    /**
     * @param startingHealth - Spawning a player with how much health.
     * @param startingInventory - Spawning a player with a specified inventory
     * @param startingPosition - Spawing a player with a specified position
     */
    public Mobile(int startingHealth, ArrayList<Item> startingInventory, Position startingPosition){
        this.health = startingHealth;
        this.Inventory = startingInventory;
        this.position = startingPosition;
        this.pathingQueue= new ArrayList<>();//need to have this to please intellij
    }

    /**
     * Constructor for Mobile, that takes a list of Position that acts as a queue for where the enemy wishes to travel,
     * these position will be traced using a BFS method.
     * @param Pathing - The list of Positions that will be traveled in a queue like system.
     */
    public Mobile(List<Position> Pathing){
        this.pathingQueue = Pathing;
    }
    /**
     * Default constructor for Mobile. Will make an empty list to a pathingQueue.
     */
    public Mobile(){
        this.pathingQueue = new ArrayList<>();
    }

    /**
     * Adds a Position to the pathingQueue.
     * @param AddedPosition - A Position added to the pathing Queue. THIS WILL BE ADDED TO THE TAIL END.
     */
    public void add(Position AddedPosition){
        this.pathingQueue.add(AddedPosition);
    }


    /**
     * Calls move for the mobiles position(that class actually does the work
     * @param direction - ENUM direction
     */
    public void move(Direction direction){
        this.position.move(direction);
    }

    /**
     * Calls move for the mobiles position(that class actually does the work
     * @return - Position object of the player
     */
    public Position getPosition(){
        return this.position;
    }

}
