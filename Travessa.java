public class Travessa {
	static final int maximPartits=15;
	
	public static void main(String[] args) {
		int[][] partits = new int[maximPartits][2];
    	partits=generarPartits();
		System.out.println("Els partits jugats són "+pintaJornada(partits));
		System.out.println("Ha hagut "+calcularVictoriesVisitants(partits)+" victòries visitants ");
	}
	
	
	private static int[][] generarPartits(){
    int [][] matriu = new int[maximPartits][2];
    for(int p=0;p<maximPartits;p++){
			matriu[p][0]=(int) (Math.random()*4);
			matriu[p][1]=(int) (Math.random()*4);
		}
		return matriu;
	}	
		
	private static String pintaJornada(int[][] matriu){
		String cadena="{";
		for(int p=0;p<maximPartits-1;p++){
			cadena+="{"+matriu[p][0]+",";
			cadena+=matriu[p][1]+"},";
		}
		cadena+="{"+matriu[maximPartits-1][0]+",";
		cadena+=matriu[maximPartits-1][1]+"}}";
		return cadena;
	}
	
    private static int calcularVictoriesVisitants(int[][] matriu){
		int victories=0;
		for(int p=0;p<maximPartits-1;p++){
			if(matriu[p][0]<matriu[p][1]){
			    victories++;
			}
		}	
		return victories;
    }	
}