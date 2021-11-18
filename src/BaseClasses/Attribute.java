package BaseClasses;

public class Attribute<T> {

    private T attributeVal;

    public Attribute(T attributesValue){
        this.attributeVal = attributesValue;
    }

    public T getValue(){
        return this.attributeVal;
    }

    public void setValue(T newValue){
        this.attributeVal = newValue;
    }

}
