package refactoring;

import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;


import static org.junit.Assert.*;

import org.junit.Test;

public class TravessaTest {
	public TravessaTest() {}

	@Test
    public void testCalcularVictoriesVisitants1() {
        int[][] partits1 = {{1,2},{1,2},{2,1}};

        assertEquals(2, Travessa.calcularVictoriesVisitants(partits1));
    }
    
    @Test
    public void testCalcularVictoriesVisitants2() {
        int[][] partits2 = {};
        assertEquals(0,Travessa.calcularVictoriesVisitants(partits2));
        
    }
    
    @Test
    public void testCalcularVictoriesVisitants3() {
        int[][] partits3 = {{2,1},{5,0},{6,2}};
        assertEquals(0, Travessa.calcularVictoriesVisitants(partits3));
        
    }

    @Test
    public void testMitjaGolsPartit1() {
        int[][] partits1 = {{1,2},{2,2},{1,1}};

        assertEquals(6,6,Travessa.mitjaGolsPartit(partits1));
    }
    
    @Test
    public void testMitjaGolsPartit2() {
        int[][] partits2 = {{0,0}};

        assertEquals(0,0,Travessa.mitjaGolsPartit(partits2));
    }
    
    @Test
    public void testMitjaGolsPartit3() {
        int[][] partits3 = {{0,0},{0,0},{0,0}};

        assertEquals(2,2,Travessa.mitjaGolsPartit(partits3));
    }

}
