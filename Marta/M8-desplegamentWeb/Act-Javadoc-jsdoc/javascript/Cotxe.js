/**
 * Classe que genera un cotxe i se l'assigna a un conductor.
 *
 * @author Marta Llabrés
 * @class
 */
class Cotxe {

    /**
     * El constructor s'encarrega d'assignar el model i la matrícula del vehicle.
     *
     * @param {string} model
     * @param {string} matricula
     * @constructor
     * @public
     */
    constructor(model, matricula) {
        this.model = model;
        this.matricula = matricula;
    }

    /**
     * Assigna un conductor al cotxe.
     *
     * @param {Conductor} conductor - conductor del cotxe.
     * @public
     */
    afegirConductor(conductor) {
        this.conductor = conductor;
    }

    /**
     * Retorna el conductor actual del cotxe.
     *
     * @returns {Conductor} - conductor del cotxe
     * @public
     */
    obtenirConductor() {
        return this.conductor;
    }

    /**
     * Mostra a la consola la informació del cotxe.
     */
    mostrarInfo() {
        console.log(this.model + ", " + this.matricula + ", " + this.conductor.nom);
    }
}