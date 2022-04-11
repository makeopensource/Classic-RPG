package BaseClassesTests;

import BaseClasses.Tile;
import BaseClasses.Region;
import BaseClasses.Position;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

class RegionTest {

    @Test
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
    @Test
    void mapTestPrint(){
        Tile[][] tileMatrix = new Tile[5][5];
        Region testReg = new Region(tileMatrix, "testRegion");
        for(int j = 0; j<5; j++){
            for(int i = 0; i < 5; i++){
                tileMatrix[i][j] = new Tile(testReg,i,j);
            }
        }
        for(int row = 0; row<5;row++){
            for(int column = 0; column<5;column++){
                if(column < 4){System.out.print(tileMatrix[column][row].tileID+",");}
                else{System.out.print(tileMatrix[column][row].tileID);}
            }
            System.out.println();
        }
    }
}

