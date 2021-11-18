package BaseClasses;

public class Attribute<T> {

    private T traitVal;

    public Attribute(T traitValue){
        this.traitVal = traitValue;
    }

    public T getValue(){
        return this.traitVal;
    }

    public void setValue(T newValue){
        this.traitVal = newValue;
    }

}
