package BaseClassesTests;

import BaseClasses.Attribute;

import static org.junit.jupiter.api.Assertions.*;

class AttributeTest {

    @org.junit.jupiter.api.Test
    void getValue() {
        Attribute<String> attribute = new Attribute<>("yes");
        assertEquals(attribute.getValue(), "yes");
        Attribute<Integer> attribute2 = new Attribute<>(1);
        assertEquals(attribute2.getValue(), 1);
    }

    @org.junit.jupiter.api.Test
    void setValue() {
        Attribute<String> attribute = new Attribute<>("yes");
        attribute.setValue("no");
        assertEquals(attribute.getValue(), "no");
        Attribute<Integer> attribute2 = new Attribute<>(1);
        attribute2.setValue(2);
        assertEquals(attribute2.getValue(), 2);

    }
}
