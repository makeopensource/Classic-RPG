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
        //here we need to compare the actual contents of the file so this assert is invalid.
        /**
         * Anything below this is tests for a Map Object
         */
        Region testReg2 = new Region(tileMatrix, "testRegion2");
        Region testReg3 = new Region(tileMatrix, "testRegion3");
        Hashtable<Region,List<Region>> testMapHash = new Hashtable<>();
        Map TestMap = new Map(testMapHash);
        TestMap.addRegion(testReg);
        TestMap.addRegion(testReg2);
        TestMap.addRegion(testReg3);
        assertTrue(TestMap.contains(testReg2));
        assertTrue(TestMap.contains(testReg));
        assertTrue(TestMap.contains(testReg3));
        TestMap.addConnectedRegion(testReg,testReg2);
        TestMap.addConnectedRegion(testReg,testReg3);
        List<Region>Comparator = new ArrayList<>(){{add(testReg2);add(testReg3);}};
        for(int i = 0; i< TestMap.getListOfConnectedRegion(testReg).size();i ++){
            assertEquals(TestMap.getListOfConnectedRegion(testReg).get(i),Comparator.get(i));
        }
    }




}

