package BaseClasses.Tiles;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;

public class Mountain extends Tile {


    public Mountain(Region region, int x, int y){
        super(region, x, y);

    }

    /**
     *
     * @return isPassable - returns if the tile is passage
     */
    public boolean isPassable(){
        return false;
    }

    public boolean isVisible(){
        return false;
    }
}
