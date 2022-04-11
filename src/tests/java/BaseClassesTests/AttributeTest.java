package BaseClassesTests;

import BaseClasses.Attribute;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;


class AttributeTest {

    @Test
    void getValueTest() {
        Attribute<String> attribute = new Attribute<>("yes");
        assertEquals(attribute.getValue(), "yes");
        Attribute<Integer> attribute2 = new Attribute<>(1);
        assertEquals(attribute2.getValue(), 1);
    }

    @Test
    void setValueTest() {
        Attribute<String> attribute = new Attribute<>("yes");
        attribute.setValue("no");
        assertEquals(attribute.getValue(), "no");
        Attribute<Integer> attribute2 = new Attribute<>(1);
        attribute2.setValue(2);
        assertEquals(attribute2.getValue(), 2);

    }
}
