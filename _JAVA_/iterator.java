
import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

public class iterator {
    public static void main(String[] args) {
        int[] num = {12,2,3,4,5,6}; 
        ArrayList<Integer> m = new ArrayList<>();
       
        for(int i : num) m.add(i);
        Iterator<Integer> n = m.iterator();
        while (n.hasNext()) System.out.println(n.next());
        LinkedList<Integer> L = new LinkedList<>();
        for (int j  : num) L.add(j);
        System.out.println(L);
            
        

    }
}
