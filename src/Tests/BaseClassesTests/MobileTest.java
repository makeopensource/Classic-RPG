package Tests.BaseClassesTests;
import BaseClasses.Position;
import BaseClasses.Region;
import Entities.Mobiles.*;

import java.util.ArrayList;
import java.util.Collections;

import static org.junit.jupiter.api.Assertions.*;
public class MobileTest {
    @org.junit.jupiter.api.Test
    void createMobile(){
        //Programmers Note: Mobile should also take an entity that has the ability to move.
        // This has not been developed yet.
        // TODO Make Mobile take an entity in its constructor.
        // Unless mobile is an entity itself?
        Mobile TestMobile = new Mobile();
        assertEquals(TestMobile.pathingQueue, Collections.emptyList());
        TestMobile.add(new Position(new Region(),0,0));
        assertNotEquals(TestMobile.pathingQueue,Collections.emptyList());
    }
}
