#######################################################
Projet : Simulation de Phishing (Jeu concours de Noël Erborian)
#######################################################

--- Présentation ---
Ce projet est une preuve de concept réalisée dans un cadre pédagogique. Il simule une campagne de phishing complète (email -> formulaire -> exfiltration) pour démontrer les risques de l'ingénierie sociale.

--- Structure du Projet ---
mail_erborian.html : L'email de phishing initial (vecteur d'attaque). Il imite la direction artistique du site officiel d'Erborian.

formulaire.html : La page de capture de données. De même, il imite la direction artistique du site officiel d'Erborian.

capture.php : Le script serveur qui intercepte et enregistre les données.

merci.html : Page de confirmation pour la victime (leurre). Renvoie sur la page d'accueil du site original.

base_donnees_victimes.csv : Fichier généré contenant les données exfiltrées recueillies.

--- Installation & Test (Localhost) ---
Pour que le script PHP fonctionne, un serveur local est nécessaire :

Copier le dossier du projet dans le répertoire htdocs (XAMPP) ou www (WAMP).

Lancer le module Apache depuis le panneau de contrôle de votre serveur local.

Accéder au formulaire via l'URL : http://localhost/projet_srie_NinaPerret/mail_erborian.html.

Cliquer sur le bouton "Réclamer mon prix" dans le formulaire. Remplir le formulaire et valider.

Vérifier l'exfiltration dans le fichier base_donnees_victimes.csv créé automatiquement.

--- Disclaimer ---
Ce projet est exclusivement éducatif. L'usage de ce code à des fins malveillantes est strictement interdit. L'auteur décline toute responsabilité en cas de détournement frauduleux de ces outils. Aucune donnée réelle n'a été collectée durant le développement.
