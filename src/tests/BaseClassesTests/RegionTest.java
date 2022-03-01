package BaseClassesTests;
import BaseClasses.Direction;
import BaseClasses.Tile;
import BaseClasses.Region;
import BaseClasses.Position;
import BaseClasses.Tiles.*;
import Entities.Item;
import Entities.Mobiles.Mobile;


import java.util.ArrayList;

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
    @org.junit.jupiter.api.Test
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
    @org.junit.jupiter.api.Test
    void impassableTile(){
        Tile[][] tileMatrix = new Tile[4][5];
        Region testReg = new Region(tileMatrix, "impassableTileRegion");

        for(int i = 0; i < 4; i++){
            for(int j = 0; j<5; j++){
                if( (i==2 && j==0) || (i==0 && j==1) || (i==3 && j==2)) {
                    tileMatrix[i][j] = new Mountain(testReg,i,j);
                }else{
                    tileMatrix[i][j] = new GrassLand(testReg,i,j);
                }
            }
        }
        // creates
        /*
        * GMGGG
        * GGGGG
        * MGGGG
        * GGMGG
        * */
        Mobile george = new Mobile(10, new ArrayList<Item>(),new Position(testReg,0,3));
        //Test: region.getWidth & region.getHeight
        assert(testReg.getWidth()==5);
        assert(testReg.getHeight()==4);

        //does start position work
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==3);

        //does moving into a wall work
        george.move(Direction.NORTH);
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==3);

        //does moving off the region work
        george.move(Direction.SOUTH);
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==3);

        //actually moving
        george.move(Direction.EAST);
        assert(george.getPosition().getX()==1);
        assert(george.getPosition().getY()==3);

        //moving into a wall going east
        george.move(Direction.EAST);
        assert(george.getPosition().getX()==1);
        assert(george.getPosition().getY()==3);

        //actually moving:north edition
        george.move(Direction.NORTH);
        assert(george.getPosition().getX()==1);
        assert(george.getPosition().getY()==2);

        //actually moving: north edition(run it back)
        george.move(Direction.NORTH);
        assert(george.getPosition().getX()==1);
        assert(george.getPosition().getY()==1);

        george.move(Direction.WEST);
        george.move(Direction.WEST);
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==1);

        george.move(Direction.NORTH);
        george.move(Direction.NORTH);
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==0);

        george.move(Direction.EAST);
        george.move(Direction.EAST);
        george.move(Direction.EAST);
        george.move(Direction.EAST);
        george.move(Direction.EAST);
        george.move(Direction.EAST);
        assert(george.getPosition().getX()==0);
        assert(george.getPosition().getY()==0);





    }
}

