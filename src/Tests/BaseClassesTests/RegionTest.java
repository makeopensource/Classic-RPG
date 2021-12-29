package Tests.BaseClassesTests;
import BaseClasses.Map;
import BaseClasses.Tile;
import BaseClasses.Region;
import BaseClasses.Position;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class RegionTest {

    @org.junit.jupiter.api.Test
    void createRegion(){
        Tile[][] tileMatrix = new Tile[5][5];
        Region testReg = new Region(tileMatrix, "testRegion");
        for(int i = 0; i < 5; i ++){
            for(int j = 0; j < 5; j ++){
                tileMatrix[i][j] = new Tile(testReg, j,i);
            }
        }

        Position testPos = new Position(testReg, 2, 2);
        assertEquals(2, testReg.getTile(2,3).getPositionX());
        assertEquals(3, testReg.getTile(2,3).getPositionY());
        assertEquals("testRegion", testReg.getName());
        assertEquals(2, testReg.getTile(testPos).getPositionX());
        assertEquals(2, testReg.getTile(testPos).getPositionY());
    }




}

