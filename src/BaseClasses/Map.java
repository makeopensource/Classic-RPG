package BaseClasses;
import java.util.*;
public class Map {
    Hashtable<Region,List<Region>> RegionDictionaryLocal;

    public Map(Hashtable<Region,List<Region>> RegionDictionary){
        // Takes (RegionName -> ConnectedRegionList) Exclude self(RegionName) in ConnectedRegion
        RegionDictionaryLocal = RegionDictionary;
    }

    /**
     *
     * @param RegionPrime The Region You are adding to the Map
     * @param ListOfConnectedRegions The List of Regions it is connected to.
     */
    public void AddRegion(Region RegionPrime, List<Region> ListOfConnectedRegions){
        this.RegionDictionaryLocal.put(RegionPrime,ListOfConnectedRegions);
    }

    /**
     *
     * @param RegionName - Takes the region name if it exists and returns a list of Region Names Connected To that Region.
     *                   If the specified region is not found. Return null
     * @return List<String> Of Connected Regions.
     */
    public List<Region> GetListOfConnectedRegion(Region RegionName){
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
}
