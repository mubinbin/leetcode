import java.util.*;

public class CheckMag {

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {

        // List<String> magList = Arrays.asList(magazine);
        // above will create a fix size list, which cannot use remove.
        
        Arrays.sort(magazine);
        Arrays.sort(note);
        
        int i =0;
        int j =0;
        
        while(i < magazine.length){
            if( magazine[i].equals(note[j])){
                i++;
                j++;
                if(j == note.length){
                    System.out.print("Yes");
                    return;
                }
            }else{
                i++;
            }
        }
        System.out.print("No");
        return;
    }

    public static void main(String[] args) {

        String[] magazine = {"give", "me", "one", "grand", "today", "night"};
        String[] note = {"give", "one", "grand", "today"};

        checkMagazine(magazine, note);
    }
}