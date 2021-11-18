package Tests.BaseClassesTests;
import BaseClasses.Tile;
import BaseClasses.Region;
import static org.junit.jupiter.api.Assertions.*;

class RegionTest {

    @org.junit.jupiter.api.Test
    void createRegion(){
        Tile[][] tileMatrix = new Tile[5][5];
        for(int i = 0; i < 5; i ++){
            for(int j = 0; j < 5; j ++){
                tileMatrix[i][j] = new Tile(j,i);
            }
        }
        Region testReg = new Region(tileMatrix);

        assertEquals(3, testReg.getTile(2,3).getPositionX());
        assertEquals(4, testReg.getTile(2,3).getPositionY());
        //here we need to compare the actual contents of the file so this assert is invalid.

    }




}

