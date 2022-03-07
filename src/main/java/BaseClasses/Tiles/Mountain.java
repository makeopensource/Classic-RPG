package BaseClasses.Tiles;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;

public class Mountain extends Tile {
    public Mountain(){
        this.passable = false;
        this.tileID = 2;
    }

    public Mountain(Region region, int X, int Y){
        pos = new Position(region, X, Y);
    }

    /**
     *
     * @return isPassable - returns if the tile is passage
     */
    public boolean isPassable(){
        return false;
    }
}
