package Entities.Mobiles;

import BaseClasses.Position;

import java.util.*;

public class Mobile{
    private final List<Position> pathingQueue;
    public Mobile(List<Position> Pathing){
        this.pathingQueue = Pathing;
    }
    /**
     * Default constructor for Mobile.
     */
    public Mobile(){
        this.pathingQueue = Collections.emptyList();
    }
}
