package BaseClasses;

class Trait <T> {
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

class TraitTest {
    public static void main(String[] args){
        Trait<String> trait = new Trait<>("yes");
        System.out.println(trait.getvalue());
        trait.setval("no");
        System.out.println(trait.getvalue());
    }
}
