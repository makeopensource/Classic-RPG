package Entities.Mobiles;

import BaseClasses.Position;

import java.util.*;

public class Mobile{
    private final List<Position> pathingQueue;

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
        this.pathingQueue = Collections.emptyList();
    }
}
