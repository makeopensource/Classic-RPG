class Traits <T> {
    private T traitval;

    public Traits(T traitvalue){
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
        Traits<String> trait = new Traits<>("yes");
        System.out.println(trait.getvalue());
        trait.setval("no");
        System.out.println(trait.getvalue());
    }
}
