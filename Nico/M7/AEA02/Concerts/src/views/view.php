<?php

class View
{
    private $templatePath;

    public function __construct()
    {
        $this->templatePath = __DIR__ . '/templates/';
    }

    public function render($template, $data = [])
    {
        $templateFile = $this->templatePath . $template . '.html';

        if (!file_exists($templateFile)) {
            return "Error: Plantilla no trobada";
        }

        $content = file_get_contents($templateFile);

        // Substituir les variables a la plantilla
        foreach ($data as $key => $value) {
            if (is_array($value)) {
                continue;
            }
            $content = str_replace('{{' . $key . '}}', $value, $content);
        }

        // Processar la llista de concerts
        if (isset($data['concerts']) && is_array($data['concerts'])) {
            $content = $this->renderConcerts($content, $data['concerts']);
        }

        // Processar el formulari d'edició
        if (isset($data['concert'])) {
            $content = $this->renderEditForm($content, $data['concert']);
        }

        return $content;
    }

    private function renderConcerts($content, $concerts)
    {
        $concertsHtml = '';

        if (empty($concerts)) {
            $concertsHtml = '<tr><td colspan="6" style="text-align:center;">No s\'han trobat concerts</td></tr>';
        } else {
            foreach ($concerts as $concert) {
                $concertsHtml .= '<tr>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['id_concert']) . '</td>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['grup']) . '</td>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['ciutat']) . '</td>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['sala']) . '</td>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['data']) . '</td>';
                $concertsHtml .= '<td>' . htmlspecialchars($concert['hora']) . '</td>';
                $concertsHtml .= '</tr>';
            }
        }

        return str_replace('{{concerts_list}}', $concertsHtml, $content);
    }

    private function renderEditForm($content, $concert)
    {
        foreach ($concert as $key => $value) {
            $content = str_replace('{{concert_' . $key . '}}', htmlspecialchars($value), $content);
        }
        return $content;
    }
}
