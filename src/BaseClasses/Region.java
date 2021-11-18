package BaseClasses;

import java.lang.reflect.Array;
import java.util.ArrayList;
import BaseClasses.Tile;

public class Region {
    String nodeName;
    Tile[][] regionGrid;

    //make region later
    public Region(){

    }
    //directly pass in an array
    //tech allows for rows to be different lengths(idk if we want this)
    public Region(Tile[][] inputR){
        this.regionGrid = inputR.clone();
    }
    //take input from a file to create region
    public Region(String fName){

    }

    public Tile getTile(int x, int y){
        return regionGrid[y][x];
    }

}