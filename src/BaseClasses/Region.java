package BaseClasses;

import java.lang.reflect.Array;
import java.util.ArrayList;
import BaseClasses.Tile;

public class Region {
    String nodeName;
    ArrayList<ArrayList<Tile>> regionGrid = new ArrayList<ArrayList<Tile>>();

    //make region later
    public Region(){

    }
    //directly pass in an array
    //tech allows for rows to be different lengths(idk if we want this)
    public Region(Tile[][] inputR){
        ArrayList<Tile> buffRow = new ArrayList<Tile>();
        for(int i = 0; i < inputR.length; i ++){
            buffRow.clear();
            for(int j = 0; j < inputR[i].length; j++){
                buffRow.add(inputR[i][j]);
            }
            this.regionGrid.add(buffRow);
        }
    }
    //take input from a file to create region
    public Region(String fName){

    }

    public Tile getTile(int x, int y){
        return regionGrid.get(y).get(x);
    }

}