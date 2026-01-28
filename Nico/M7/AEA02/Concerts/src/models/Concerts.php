<?php
require_once __DIR__ . '/DBAbstractModel.php';

class Concerts extends DBAbstractModel
{
    private $id_concert;
    private $grup;
    private $ciutat;
    private $sala;
    private $data;
    private $hora;

    public function __construct()
    {
        $this->db_name = "concerts_db";
    }

    // Obtenir tots els concerts
    public function selectAll()
    {
        $this->query = "SELECT * FROM concerts ORDER BY data ASC";
        $this->get_results_from_query();
        return $this->rows;
    }

    // Obtenir un concert per ID
    public function select($id = null)
    {
        if ($id) {
            $this->query = "SELECT * FROM concerts WHERE id_concert = " . intval($id);
            $this->get_results_from_query();
            return isset($this->rows[0]) ? $this->rows[0] : null;
        }
        return null;
    }

    // Cercar concerts per grup
    public function selectByGrup($grup)
    {
        $this->query = "SELECT * FROM concerts WHERE grup LIKE '%" . $this->escapeString($grup) . "%' ORDER BY data ASC";
        $this->get_results_from_query();
        return $this->rows;
    }

    // Cercar concerts entre dues dates
    public function selectByDates($dataInici, $dataFi)
    {
        $this->query = "SELECT * FROM concerts WHERE data BETWEEN '" . $this->escapeString($dataInici) . "' AND '" . $this->escapeString($dataFi) . "' ORDER BY data ASC";
        $this->get_results_from_query();
        return $this->rows;
    }

    // Inserir un nou concert
    public function insert($dades = null)
    {
        if ($dades) {
            $this->query = "INSERT INTO concerts (grup, ciutat, sala, data, hora) VALUES (
                '" . $this->escapeString($dades['grup']) . "',
                '" . $this->escapeString($dades['ciutat']) . "',
                '" . $this->escapeString($dades['sala']) . "',
                '" . $this->escapeString($dades['data']) . "',
                '" . $this->escapeString($dades['hora']) . "'
            )";
            $this->execute_single_query();
            return true;
        }
        return false;
    }

    // Actualitzar el lloc (sala) d'un concert
    public function update($id = null, $sala = null)
    {
        if ($id && $sala) {
            $this->query = "UPDATE concerts SET sala = '" . $this->escapeString($sala) . "' WHERE id_concert = " . intval($id);
            $this->execute_single_query();
            return true;
        }
        return false;
    }

    // Eliminar un concert
    public function delete($id = null)
    {
        if ($id) {
            $this->query = "DELETE FROM concerts WHERE id_concert = " . intval($id);
            $this->execute_single_query();
            return true;
        }
        return false;
    }

    // Escapar strings per evitar SQL injection
    private function escapeString($str)
    {
        return addslashes($str);
    }
}
