package BaseClasses;

public class Trait <T> {

    private T traitVal;

    public Trait(T traitValue){
        this.traitVal = traitValue;
    }

    public T getValue(){
        return this.traitVal;
    }

    public void setValue(T newValue){
        this.traitVal = newValue;
    }

}
