package Entities.Mobiles;

import BaseClasses.Direction;
import BaseClasses.Position;
import BaseClasses.Region;
import BaseClasses.Tile;
import Entities.Item;

import java.util.ArrayList;

public class Enemy extends Mobile{
    public int viewDistance;

    public Enemy(int startingHealth, ArrayList<Item> startingInventory, Position startingPosition, int viewDistance){
        super(startingHealth, startingInventory, startingPosition);
        this.viewDistance = viewDistance;
    }




    public void update(){

    }

}
