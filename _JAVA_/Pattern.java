class Pattern{
    public static void main(String[] args) {
        for (int i =1 ; i <=5; i++) {
            for (int j = 1; j <=5; j++) {
                System.out.print(" * ");
            }
            System.out.println("");
        }
        
        
        
        for (int i = 1; i <6 ; i++) {
            for (int j = 1; j <=i ; j++) {
                System.out.print(" * ");
            }
             System.out.println("");
             
        }

        for (int i=1 ; i<=5;i++){
            for (int j = i; j <=4; j++) {
                System.out.print(" & ");
            }
            System.out.println("");
        }

        for (int i = 1; i <= 6; i++) {
            for (int k = i; k <6; k++) {
                
                System.out.print("  ");
            }
            for (int h = 1; h <=i; h++) {
                System.out.print("* ");
            }
            for (int h = 1; h < i; h++) {
                System.out.print("* ");
            }
            
            System.out.println("  ");
        }


        for (int i = 1; i <=6; i++) {
            for (int l = 1; l<=i ; l++) {
                System.out.print("  ");
            }
            for (int u = i; u <=6; u++) {
                System.out.print("* ");
            }
            for (int u = i; u < 6; u++) {
                System.out.print("* ");
            }
            System.out.println("  ");
        }

       




    }
}