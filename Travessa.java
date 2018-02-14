public class Travessa {
	static final int maximPartits=15;
	
	public static void main(String[] args) {
		int[][] partits = new int[maximPartits][2];
    		partits=generarPartits(maximPartits);
		System.out.println("Els partits jugats són "+pintaJornada(partits));
		System.out.println("Ha hagut "+calcularVictoriesVisitants(partits)+" victòries visitants ");
	}
	
	
	private static int[][] generarPartits(int numeroPartits){
    		int [][] matriu = new int[numeroPartits][2];
    		for(int p=0;p<numeroPartits;p++){
			matriu[p][0]=(int) (Math.random()*4);
			matriu[p][1]=(int) (Math.random()*4);
		}
		return matriu;
	}	
		
	private static String pintaJornada(int[][] partits){
		String cadena="{";
		for(int p=0;p<partits.length-2;p++){
			cadena+="{"+partits[p][0]+",";
			cadena+=partits[p][1]+"},";
		}
		cadena+="{"+partits[partits.length-1][0]+",";
		cadena+=partits[partits.length-1][1]+"}}";
		return cadena;
	}
	
    	private static int calcularVictoriesVisitants(int[][] partits){
		int victories=0;
		for(int p=0;p<partits.length;p++){
			if(partits[p][0]<=partits[p][1]){
			    victories++;
			}
		}	
		return victories;
    	}	
}
