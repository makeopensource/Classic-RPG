package BaseClassesTests;
import BaseClasses.Position;
import BaseClasses.Region;
import Entities.Entity;
import Entities.Item;
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
        /*
        Mobile TestMobile = new Mobile(5,new ArrayList<Item>(),new Position(new Region(),5,5));
        assertEquals(TestMobile.pathingQueue, Collections.emptyList());
        TestMobile.addPositionToQueue(new Position(new Region(),0,0));
        assertNotEquals(TestMobile.pathingQueue,Collections.emptyList());
        */
    }
}
