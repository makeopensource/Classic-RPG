import java.util.*;

public class Tile {

    private ArrayList<Entities> ListofEntities;

    public void setEntities(ArrayList<Entities> entities){
        this.ListofEntities = entities;
    }

    public ArrayList<Entities> getEntities(){
        return this.ListofEntities;
    }


    public Tile(ArrayList<Entities> entities){
        this.ListofEntities = entities;
    }

    public Tile(){
        this.ListofEntities = new ArrayList<Entities>();
    }

}