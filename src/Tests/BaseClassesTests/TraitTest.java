package Tests.BaseClassesTests;

import BaseClasses.Trait;

import static org.junit.jupiter.api.Assertions.*;

class TraitTest {

    @org.junit.jupiter.api.Test
    void getvalue() {
        Trait<String> trait = new Trait<>("yes");
        assertEquals(trait.getvalue(), "yes");
        Trait<Integer> trait2 = new Trait<>(1);
        assertEquals(trait2.getvalue(), 1);
    }

    @org.junit.jupiter.api.Test
    void setval() {
        Trait<String> trait = new Trait<>("yes");
        trait.setval("no");
        assertEquals(trait.getvalue(), "no");
        Trait<Integer> trait2 = new Trait<>(1);
        trait2.setval(2);
        assertEquals(trait2.getvalue(), 2);
    }
}
