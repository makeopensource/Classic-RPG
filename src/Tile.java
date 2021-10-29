import java.util.*;

public class Tile {

    private ArrayList<Entity> ListofEntities;

    public void setEntities(ArrayList<Entity> entities){
        this.ListofEntities = entities;
    }

    public ArrayList<Entity> getEntities(){
        return this.ListofEntities;
    }


    public Tile(ArrayList<Entity> entities){
        this.ListofEntities = entities;
    }

    public Tile(){
        this.ListofEntities = new ArrayList<Entity>();
    }

}