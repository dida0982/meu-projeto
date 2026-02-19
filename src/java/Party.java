import java.awt.*;
import java.awt.event.*;

public class Party {

    public void buildInvite() {
        Frame f = new Frame("Party");
        Label l = new Label("Party at Tim's");
        Button b = new Button("You bet");
        Button c = new Button("Shoot me");
        Panel p = new Panel();

        p.add(l);
        p.add(b);
        p.add(c);

        f.add(p);

        f.setSize(300, 200);
        f.setVisible(true);

        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent we) {
                f.dispose();
            }
        });
    }

    public static void main(String[] args) {
        Party party = new Party();
        party.buildInvite();
    }
}
