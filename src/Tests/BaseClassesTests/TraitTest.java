package Tests.BaseClassesTests;

import BaseClasses.Trait;

import static org.junit.jupiter.api.Assertions.*;

class TraitTest {

    @org.junit.jupiter.api.Test
    void getValue() {
        Trait<String> trait = new Trait<>("yes");
        assertEquals(trait.getValue(), "yes");
        Trait<Integer> trait2 = new Trait<>(1);
        assertEquals(trait2.getValue(), 1);
    }

    @org.junit.jupiter.api.Test
    void setValue() {
        Trait<String> trait = new Trait<>("yes");
        trait.setValue("no");
        assertEquals(trait.getValue(), "no");
        Trait<Integer> trait2 = new Trait<>(1);
        trait2.setValue(2);
        assertEquals(trait2.getValue(), 2);
    }
}
