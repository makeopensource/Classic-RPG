package Entities.Mobiles;

import BaseClasses.Position;
import Entities.Item;

import java.util.ArrayList;

public class NPC extends Mobile{
    ArrayList<Position> pathingQueue;

    public NPC(int startingHealth, ArrayList<Item> startingInventory, Position startingPosition, ArrayList<Position> pQueue){
        super(startingHealth, startingInventory, startingPosition);
        this.pathingQueue = pQueue;
    }

    /**
     * Adds a Position to the pathingQueue.
     * @param AddedPosition - A Position added to the pathing Queue. THIS WILL BE ADDED TO THE TAIL END.
     */
    public void addPositionToQueue(Position AddedPosition){
        this.pathingQueue.add(AddedPosition);
    }
}
