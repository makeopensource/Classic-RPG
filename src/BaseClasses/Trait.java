package BaseClasses;

public class Trait <T> {
    private T traitval;

    public Trait(T traitvalue){
        this.traitval = traitvalue;
    }

    public T getvalue(){
        return this.traitval;
    }

    public void setval(T newvalue){
        this.traitval = newvalue;
    }

}
