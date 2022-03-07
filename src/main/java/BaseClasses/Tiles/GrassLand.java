package BaseClasses.Tiles;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;

public class GrassLand extends Tile {
    public GrassLand(){
        this.passable = true;
        this.tileID = 1;
    }

    public GrassLand(Region region, int X, int Y){
        pos = new Position(region, X, Y);
    }
    /**
     *
     * @return isPassable - returns if the tile is passage
     */
    public boolean isPassable(){
        return true;
    }
}
