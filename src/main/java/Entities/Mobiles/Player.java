package Entities.Mobiles;
import Entities.Item;
import java.util.*;

public class Player extends Mobile {
   public int health;
   public ArrayList<Item> Inventory;
    /**
     * @param startingHealth - Spawning a player with how much health.
     */
    public Player(int startingHealth){
        this.health = startingHealth;
        this.Inventory = new ArrayList<>();
    }
    public Player(int startingHealth, ArrayList<Item> startingInventory){
        this.health = startingHealth;
        this.Inventory = startingInventory;
    }
}
