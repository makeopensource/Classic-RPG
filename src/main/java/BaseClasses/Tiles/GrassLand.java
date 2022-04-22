package BaseClasses.Tiles;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;

public class GrassLand extends Tile {


    public GrassLand(Region region, int x, int y){
        super(region, x, y);
    }
    /**
     *
     * @return isPassable - returns if the tile is passage
     */
    public boolean isPassable(){
        return true;
    }

    public boolean isVisible(){
        return true;
    }
}
