package BaseClasses.Tiles;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;

public class Water extends Tile {
    public Water(){
        this.passable = false;
        this.tileID = 3;
    }

    public Water(Region region, int X, int Y){
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
