package BaseClasses;

import java.lang.reflect.Array;
import java.util.ArrayList;
import BaseClasses.Tile;

public class Region {
    String nodeName;
    ArrayList<String> subSectionNames = new ArrayList<String>();
    String matrixName;
    Tile[][] tileMatrix;

    public Region(String matrixName, String nodeName, int matrixRows, int matrixCols){
        this.nodeName = nodeName;
        this.matrixName = matrixName;
        this.tileMatrix = new Tile[matrixRows][matrixCols];
    }
    public void setTileMatrix(Tile[][] tileMatrix){
        this.tileMatrix = tileMatrix;
    }
    public Tile[][] getTileMatrix(){
        return this.tileMatrix;
    }
    public Tile getTile(int row, int col) {
        try {

            return this.tileMatrix[row][col];
        }catch (Exception e){}
        return null;

    }
}
