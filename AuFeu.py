import pyDatalog.pyDatalog as pdl
import easygui as easy


fieldValueEtat = easy.multenterbox("", "SOS", ["votre nom: ", "Le lieu où se trouve la victime: ", "Le nombre de victimes :",
                                               "L’état de la ou des victime(s) :",
                                               "Les obstacles potentiels pour le transport des victimes \n(escaliers, arbres renversés, rochers, etc.) :"])

fieldValueSigne = easy.multenterbox("Signes ou symptômes", "SOS", ["Décrivez et localisez les symptômes de la victime aux ambulanciers.",
                                                 "Quantifiez la douleur en demandant à la victime de la mesurer sur une échelle de 0 à 10\n (0 représentant l'absence de douleur et 10 représentant une douleur insupportable).",
                                                 "Qualifiez la douleur (coup de couteau, lourdeur, coup de poing, brûlure,\n localisée, étendue, pulsée, etc.)."])

fieldValueAllergie = easy.multenterbox("Allergie", "SOS", ["Demandez à la victime si elle est allergique à certains médicaments ou aliments"])
fieldValueMedicament = easy.multenterbox("Medicament", "SOS", ["Demandez à la victime si elle prend des médicaments et, si oui, lesquels"])
fieldValueMedical = easy.multenterbox("Passé médical", "SOS", ["Interrogez la victime sur ses problèmes de santé et sur son historique médical\n (diabète, asthme ou antécédents familiaux d'AVC ou d'arrêt cardiaque)",
                                                                "Rentre-t-elle d’un voyage ? Depuis moins de 3 semaines ?"])
fieldValueLaunch = easy.multenterbox("Lunch", "SOS", ["Demandez à la victime quelle était l’heure de son dernier repas, \nla quantité ingérée ainsi que ce qu’elle a mangé."])
fieldValueEvenement = easy.multenterbox("Evenement Declancheur", "SOS", ["Demandez à la victime ce qui s’est passé au \nmoment de l'accident et ce qu'elle faisait à ce moment précis."])