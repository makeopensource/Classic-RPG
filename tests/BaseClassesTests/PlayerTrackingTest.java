package BaseClassesTests;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;
import BaseClasses.Tiles.GrassLand;
import BaseClasses.Tiles.Mountain;
import Entities.Item;
import Entities.Mobiles.Enemy;
import Entities.Mobiles.Mobile;

import java.util.ArrayList;

class PlayerTrackingTest {

    @org.junit.jupiter.api.Test
    void getRegionList() {
        Tile[][] tileMatrix = new Tile[4][5];
        Region testReg = new Region(tileMatrix, "impassableTileRegion");

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 5; j++) {
                tileMatrix[i][j] = new GrassLand(testReg, i, j);
            }
        }

        // creates
        /*
         * GGGGG
         * GGGGG
         * GGGGG
         * GGGGG
         * */
        Mobile george = new Mobile(10, new ArrayList<Item>(), new Position(testReg, 0, 3));
        Enemy john = new Enemy(10, new ArrayList<Item>(), new Position(testReg, 0, 0), 5);
    }
}
