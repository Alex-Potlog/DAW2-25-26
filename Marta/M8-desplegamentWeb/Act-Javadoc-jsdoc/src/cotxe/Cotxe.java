package cotxe;

/**
 * Classe que genera un cotxe i se l'assigna a un conductor.
 * 
 * @author Marta Llabrés
 * @version 1.0.0
 * @since 1.0.0
 */

public class Cotxe{
    
    private String model;
    private String matricula;
    private String conductor;

    /**
     * Constructor amb el que li donarem un model i una matricula al cotxe.
     * 
     * @param _model        model que li assignarem al cotxe
     * @param _matricula    matrícula que li assignarem al cotxe
     */
    public Cotxe(String model, String matricula) {
        this.model = model;
        this.matricula = matricula;
    }

    /** 
     * Constructor que dóna un conductor al cotxe
     * 
     * @param _conductor conductor que s'associarà al cotxe
     */
    public void assignarConductor (String _conductor){
        this.conductor=conductor;
    }

    /** 
     * Ens retorna el nom del conductor que té el cotxe
     * 
     * @return String el nom del conductor
     */
    public String obtenirConductor(){
        return conductor;
    }

    /**
     * Mostra per pantalla la informació que hem obtingut del cotxe
     */
    public void mostrarInfo() {
        System.out.println(model +", "+matricula+", "+conductor);
    }


}