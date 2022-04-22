package BaseClassesTests;

import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;
import Entities.Entity;
import Entities.Item;
import Entities.Mobiles.Enemy;
import Entities.Mobiles.Mobile;
import Entities.Mobiles.Player;

import java.util.ArrayList;
import java.util.Collection;

import static org.junit.jupiter.api.Assertions.assertEquals;

class TileTest {

    @org.junit.jupiter.api.Test
    void position() {
        /*
        Region testRegion1 = new Region();
        Position testPosition1 = new Position(testRegion1, 1, 2);
        Tile testTile1 = new Tile(testPosition1);
        Tile testTile2 = new Tile(testRegion1, 3, 4);

        assertEquals(testTile1.getPositionX(), 1);
        assertEquals(testTile1.getPositionY(), 2);
        assertEquals(testTile1.getRegion(), testRegion1);
        assertEquals(testTile2.getPositionX(), 3);
        assertEquals(testTile2.getPositionY(), 4);
        assertEquals(testTile2.getRegion(), testRegion1);

        Region testRegion2 = new Region();
        Position testPosition2 = new Position(testRegion2, 5, 6);
        testTile1.setPosition(testPosition2);
        testTile2.setPositionX(7);
        testTile2.setPositionY(8);
        testTile2.setRegion(testRegion2);

        assertEquals(testTile1.getPositionX(), 5);
        assertEquals(testTile1.getPositionY(), 6);
        assertEquals(testTile1.getRegion(), testRegion2);
        assertEquals(testTile2.getPositionX(), 7);
        assertEquals(testTile2.getPositionY(), 8);
        assertEquals(testTile2.getRegion(), testRegion2);

        testTile1.setPositionXY(9, 10);
        assertEquals(testTile1.getPositionX(), 9);
        assertE
        */

    }

    @org.junit.jupiter.api.Test
    void entities() {
        //TODO entity tests
    }

    @org.junit.jupiter.api.Test
    void hasMethods() {
        //Someone can rewrite this
    }

}
