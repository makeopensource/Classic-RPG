package Engine;


import static org.lwjgl.glfw.GLFW.*;

public class GameLoop {
    public static void main(){
        double tick = 0;
        /** This while true can be changed to update when player moves.**/
        while(true){
            //Should we sync this with the system clock? we can use getTime to do this.
            // We would be limited to a strict framerate if we were to do that. Having a tick rate for now is ok.
            /** Put main game loop functions here **/
            // Our game is gunna be too fast if we don't have something slowing it down.
            tick = tick + 1;
            System.out.println(tick);
        }
    }
}
