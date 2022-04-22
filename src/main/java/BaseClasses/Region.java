package BaseClasses;

import Entities.Entity;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Region {
    String regionName;
    Tile[][] regionGrid;
    ArrayList<Entity> entityList;

    //make region later
    public Region(){

    }
    //directly pass in an array
    //tech allows for rows to be different lengths(idk if we want this)
    public Region(Tile[][] inputR, String name){
        this.regionGrid = inputR.clone();
        this.regionName = name;
    }
    //take input from a file to create region
    public Region(String fName){

    }

    public Tile getTile(int x, int y){
        try {
            return regionGrid[y][x];
        }
        catch (Exception e){
            System.out.println("This tile doesnt exist");
            return null;
        }
    }

    public Tile getTile(Position pos){
        try {
            return regionGrid[pos.getY()][pos.getX()];
        }
        catch (Exception e){
            System.out.println("This tile doesnt exist");
            return null;
        }
    }

    public String getName(){
        return regionName;
    }

    public int getWidth(){return this.regionGrid[0].length;}

    public int getHeight(){return this.regionGrid.length;}

    public void addEntity(Entity en){entityList.add(en);}

    //given a tile return the tile of the closest player by direct visible distance.
    //breadth first search
   // public Tile getClosestPlayer(Position P){

   // }

    //given two points find the closest waling path
    /*public ArrayList<Direction> getNearestPath(Position p){
        ArrayList moveset = new ArrayList<>();
        if(!(p.getRegion().equals(this))){
            return moveset;
        }

        return moveset;
    }*/

}