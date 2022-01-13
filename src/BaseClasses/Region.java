package BaseClasses;

public class Region {
    String regionName;
    Tile[][] regionGrid;

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
        return regionGrid[y][x];
    }

    public Tile getTile(Position pos){
        return regionGrid[pos.getY()][pos.getX()];
    }

    public String getName(){
        return regionName;
    }

    public void printRegion(){
    for (Tile[] row : regionGrid) {
      for (Tile tile: row){
        print(String(tile.getTileType))
      }
      printLn()
    }

    }

}