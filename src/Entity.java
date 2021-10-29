public class Entity {
    private Position position;

    //Constructor for using reference (equipped/held items)
    public Entity(Position position)
    {   
        this.position = position;
    }

    //Constructor for just being on the map
    public Entity(Region region, int x, int y)
    {
        this.position = new Position(region, x, y);
    }

    public Position getPosition()
    {
        return position;
    }

    public void setPosition(Position position)
    {
        //Important that the address doesn't change but the values do
        this.position.set(position);
    }
}
