package BaseClassesTests;
import BaseClasses.Map;
import BaseClasses.Tile;
import BaseClasses.Region;

import java.util.*;

import static org.junit.jupiter.api.Assertions.*;

class MapTest {
    @org.junit.jupiter.api.Test
    void createMap(){
        /*
          Creates a test region to handle Specific
         */
        Tile[][] tileMatrix = new Tile[5][5];
        Region testReg = new Region(tileMatrix, "testRegion");
        for(int i = 0; i < 5; i ++){
            for(int j = 0; j < 5; j ++){
                tileMatrix[i][j] = new Tile(testReg, j,i);
            }
        }
        Region testReg2 = new Region(tileMatrix, "testRegion2");
        Region testReg3 = new Region(tileMatrix, "testRegion3");
        Hashtable<Region,List<Region>> testMapHash = new Hashtable<>();
        Map TestMap = new Map(testMapHash);
        TestMap.addRegion(testReg);
        TestMap.addRegion(testReg2);
        TestMap.addRegion(testReg3);
        assertTrue(TestMap.containsKey(testReg2));
        assertTrue(TestMap.containsKey(testReg));
        assertTrue(TestMap.containsKey(testReg3));
        TestMap.addConnectedRegion(testReg,testReg2);
        TestMap.addConnectedRegion(testReg,testReg3);
        List<Region>Comparator = new ArrayList<>(){{add(testReg2);add(testReg3);}};
        for(int i = 0; i< TestMap.getListOfConnectedRegion(testReg).size();i ++){
            assertEquals(TestMap.getListOfConnectedRegion(testReg).get(i),Comparator.get(i));
        }
        Hashtable<Region,List<Region>> testDictonaryGet = TestMap.getRegionDictionary();
        assertTrue(testDictonaryGet.containsKey(testReg2));
        assertTrue(testDictonaryGet.containsKey(testReg));
        assertTrue(testDictonaryGet.containsKey(testReg3));
    }
}