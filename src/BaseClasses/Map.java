package BaseClasses;
import java.util.*;
public class Map {
    Hashtable<Region, List<Region>> RegionDictionaryLocal;
    private List<Region> emptyList = new ArrayList<>();
    public Map(Hashtable<Region,List<Region>> RegionDictionary){
        // Takes (RegionName -> ConnectedRegionList) Exclude self(RegionName) in ConnectedRegion
        RegionDictionaryLocal = RegionDictionary;
    }

    /**
     *
     * @param RegionPrime The Region You are adding to the Map
     * @param ListOfConnectedRegions The List of Regions it is connected to.
     *
     */
    public void addRegion(Region RegionPrime, List<Region> ListOfConnectedRegions){
        this.RegionDictionaryLocal.put(RegionPrime,ListOfConnectedRegions);
    }

    /**
     * Overloaded version of above add Region, Except if the user does not wish to add a list of connected
     * regions, they can do that through the use of the function addConnnectedRegion
     * @param RegionPrime
     */
    public void addRegion(Region RegionPrime){
        this.addRegion(RegionPrime,this.emptyList);
    }

    /**
     *
     * @param RegionName - Takes the region name if it exists and returns a list of Region Names Connected To that Region.
     *                   If the specified region is not found. Return null
     * @return List<String> Of Connected Regions.
     */
    public List<Region> getListOfConnectedRegion(Region RegionName){
        if(this.RegionDictionaryLocal.contains(RegionName)){
            return this.RegionDictionaryLocal.get(RegionName);
        }
        else{return null;}
    }

    /**
     *
     * @return The entire RegionDictionary.
     */
    public Hashtable<Region, List<Region>> getRegionDictionary() {
        return this.RegionDictionaryLocal;
    }

    /**
     *
     * @param RegionName - Takes in the name of a specific region that you wish to connect a region to.
     * @param RegionToAdd - Takes the name of the region you wish to connect to RegionName
     */
    public void addConnectedRegion(Region RegionName, Region RegionToAdd){
        if(this.RegionDictionaryLocal.contains(RegionName)){
               this.RegionDictionaryLocal.get(RegionName).add(RegionToAdd);
        }
    }

    /**
     *
     * @param RegionName - A Region Object.
     * @return True if the HashTable contains the Value
     *
     */
    public boolean contains(Region RegionName){
        return this.RegionDictionaryLocal.contains(RegionName);
    }
    /**
     * Programmers Note: I am realizing now after making all of this i could have simply used inheritance from a HashTable
     * and simply overloaded the values. This would have made programming this a lot more simpler. If anyone would like to fix this.
     * Please be my guest.
     */
}
