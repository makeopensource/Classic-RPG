package Entities;


import BaseClasses.Position;
import BaseClasses.Direction;

import java.sql.SQLOutput;

enum AttackType {
    straight, // (ie bow) attacks in a straight line for range tiles
    broad, // attacks in the direction facing wth -pi/4 to pi/4
    radial //attacks in a circle with radius range around the player
}


public class Weapon {
    int durabiltiy;
    int damage;
    int range;
    AttackType attackType;

    public Weapon(){
    }

    public Weapon(int dura, int dam, int ran, AttackType atTy){
    }
    //this attack is only valid for a 2D visual game
    public void attack2D(Position p, Direction d) {
        int x = p.getX();
        int y = p.getY();
        int[] dirVec = new int[2]; // direction vector

        //creation of the direction vectors value -- used to simplify later code
        //We look at the regions from the top right as (0,0) -> north is actaully (0,-1)
        if (d == Direction.NORTH) {
            dirVec[0] = 0;
            dirVec[1] = -1;
        } else if (d == Direction.EAST) {
            dirVec[0] = 1;
            dirVec[1] = 0;
        } else if (d == Direction.SOUTH) {
            dirVec[0] = 0;
            dirVec[1] = 1;
        } else if (d == Direction.WEST) {
            dirVec[0] = -1;
            dirVec[1] = 0;
        }
        
        if (attackType == AttackType.straight) {
            for (int i = 1; i <= range; i++) {
                x += dirVec[0];
                y += dirVec[1];
                //attackInTile(x,y)
            }
        }
        else if (attackType == AttackType.broad) {
            for (int i = 1; i <= range; i++) {
                if (dirVec[0] == 0) { // means the attack is east or west
                    for (int j = -1 * i; j < i; j++) {
                       //attackInTile(x+i*dirVec[0] ,y+j)
                    }
                }else { //this attack is north and south
                  for (int j = -1 * i; j < i; j++) {
                       //attackInTile(x+j ,y+i*dirVec[0])
                    }
                }
            }
        }
        else{
            for (int i = -1*range; i <= range; i++){
              for (int j = -1*range; j <= range; j++){
                if (i == 0 && j == 0){
                //attackInTiles(x+i, y+j)
                }
              }
            }
        }
    }
}
