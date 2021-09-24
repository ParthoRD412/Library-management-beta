public class newfile
{
int	p=5;	 	        
	  void recur(int p){ 

 	if(p==0) 

 	 	System.out.println("DONE");  
 	 		else{ 

 	 	System.out.println("HI !"+ p); 

 	 	recur(--p); 

 	 	System.out.println(" " + p); 

 	} 

} 


	public static void main(String[] args) {
        newfile ob=new newfile();
        ob.recur(5);
	}
}