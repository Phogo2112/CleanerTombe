from django.shortcuts import render
from django.shortcuts import render



def index_tarif(request):
    tombe = get_tombe_list()
    return render(request, "tarif/index.html", {'tombe': tombe})

# Create your views here.




    
def get_tombe_list(request):
    tombe=[
        {'id': 1, 'name': 'Tombe simple', 'image': 'css/photo_tombe_simple.png'},
        {'id': 2, 'name': 'Cavurne', 'image': 'css/cavurne.png'},
        {'id': 3, 'name': 'Columbarium', 'image': 'css/photo_columbarium_fleuris.png'},
        {'id': 4, 'name': 'Jardin de souvenir', 'image': 'css/jardin_de_souvenir.png'},
        {'id': 5, 'name': 'Monument paysager', 'image': 'css/monument_paysager.png'},
        {'id': 6, 'name': 'Stèle cénotaphe', 'image': 'css/stèle_cénotaphe.png'},
        {'id': 7, 'name': 'Tombe pleine terre', 'image': 'css/tombe_en_pleine_terre.png'},
        {'id': 8, 'name':'néttoyage spéciaux', 'image':'css/nettoyage_ornement.png'},
    ]
    return render(request,'tarif/index.html' , {'index_tarif' : tombe})
        

def article_tarif(request, numero_tarif):
    prix_tombe_simple = [
        {
            'id': 1, 
            'name': 'Néttoyage sans fleurissement', 
            'prix': '60€',
            'mention1' : '🌿 une évaluation complète de l\'état de la tombe est réalisée.',
            'mention2' : '🌿 Retrait des feuilles mortes, déchets et autres débris végétaux',
            'mention3' : '🌿 Un nettoyage en profondeur de la pierre tombale avec le respects des matériaux (granite, marbre, pierre naturelle)',
            'mention4' : '🌿 Élimination de la mousse et des algues',
            'mention5' : '🌿 Nettoyage en profondeur des inscriptions sur la pierre tombale, (gravures, noms, dates, etc.)',
            'mention6' : '🌿 Après néttoyage, une verification finales est faite afin de voir si la tombe est en ordres et propres ',
            'mention7' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
            'id': 3, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '90€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Néttoyage complets de la dalle et de la stèle.',
            'mention2' : '🌿 vérification et enlèvement des mousse et des herbes sur le pourtour de la dalle.',
            'mention3' : '🌿 dépose des nouvelles fleurs',
            'mention4' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
            'id': 3, 
            'name': 'Dépôt de fleurs sans nettoyage', 
            'prix': '45€',
            'mention1' : '🌿 nettoyage rapide de la dalle a l\'eaux claire.',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pot de fleurs sur le monuments.',
            'mention3' : '🌿 mise en valeur des fleurs et des ornements.',
            'mention4' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
            'id': 4, 
            'name': 'Nettoyage et entretien végétal', 
            'prix': '70€',
            'devis' : 'Pour un remplacement de plantes, un ajout de paillage ou un ajout de plantes ça se fera sur devis.',
            'mention1' : '🌿 Enlèvement des mousse des mauvaises herbes et des feuilles mortes',
            'mention2' : '🌿 Un entretien des plantes déjà présentes et effectuées, taille et arrosage.',
            'mention3' :'🌿 Nettoyage complet de la dalle et de la stèle avec du savon doux.',
            'mention4' : '🌿 Rinçage de la dalle et de la stèle puis un séchage avec un chiffon doux est effectué. ',
            'mention5' : '🌿 Nivellement de terrain Peut-être effectué si besoin.',
            'mention6' : '📷 une photo avant et après l\'intervention sera effectuée.',
            
        },
        {
           'id': 5, 
            'name': 'Le néttoyage des ornements sont en suppléments', 
            'prix': 'suppléments',
            'devis': 'ce sera sur devis avec le nombre et le types d\'ornement existant sur le monuments.',
            'mention1' : '🌿 néttoyage complets de tout les ornements avec des produits biodégradable et non corrosifs pour préserver les ',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            
        },   
    ]
    # finit
    prix_cavurne = [
        {
            'id' : 1 , 
            'name' : 'Néttoyage sans fleurissement',
            'prix' : '40€',
            'mention1' : '🌿 Néttoyage complets de la dalle et de la stèle.',
            'mention2' : '🌿 Déserbage et suppressions de la mousse.',
            'mention3' : '🌿 Arrosage et entretien des plantes déja présents.',
            'mention4' : '🌿 après le rinçage on essuie les trace de nettoyage à l\'aide de chiffons doux ou microfibre',
            'mention4' : '🌿 Après néttoyage, une verification finales est faite afin de voir si le cavurne est en ordres et propres. ',
            'mention5' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {   'id': 2, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '70€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Néttoyage complets de la dalle et de la stèle.',
            'mention2' : '🌿 Déserbage et suppressions de la mousse.',
            'mention3' : '🌿 Dépose des nouvelle fleurs',
            'mention4' : '🌿 Arrosage et entretien des plantes déja présents.',
            'mention5' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
            'id': 3,
            'name': 'fleurissement',
            'prix': '35€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Rinçage de la dalle',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            'mention3' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
           'id': 4, 
            'name': 'les ornements', 
            'prix': 'suppléments',
            'devis': 'ce sera sur devis avec le nombre et le types d\'ornement existant sur le monuments.',
            'mention1' : '🌿 néttoyage complets de tout les ornements avec des produits biodégradable et non corrosifs pour préserver les ',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            
        },   
    ]
    prix_columbarium=[
        {
            'id' : 1 ,
            'name' : 'Néttoyage sans fleurissement',
            'prix' : '40€',
            'mention1' : '🌿 une évaluation complète de l\'état du columbarium est réalisée.',
            'mention2' : '🌿 Nettoyage complet de la dalle et de la stèle avec du savon doux .',
            'mention3' : '🌿 Nettoyage en profondeur des inscriptions sur la pierre tombale, (gravures, noms, dates, etc.)',
            'mention4' : '🌿 rinçage a l\'eau claire et essuyer avec un chiffon ou microfibre.',
            'mention5' : '🌿 Après néttoyage, une verification finales est faite afin de voir si le columbarium est en ordres et propres. ',
            'mention6' : '📷 une photo avant et après l\'intervention',
        },
        {   'id': 2, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '70€',
            'devis': 'Pour un choix personnalisé des fleurs, ce sera sur devis.',
            'mention1' : '🌿 Néttoyage complets de la dalle et de la stèle.',
            'mention2' : '🌿 Néttoyage de la dalle',
            'mention3' : '🌿 dépose des nouvelle fleurs.',
            'mention4' : '📷 une photo avant et après l\'intervention',
        },
        {
            'id': 3, 
            'name': 'fleurissement', 
            'prix': '35€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Rinçage de la dalle',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            'mention4' : '📷 une photo avant et après l\'intervention',
        },
        {
           'id': 4, 
            'name': 'les ornements', 
            'prix': 'suppléments',
            'devis': 'ce sera sur devis avec le nombre et le types d\'ornement existant sur le monuments.',
            'mention1' : '🌿 néttoyage complets de tout les ornements avec des produits biodégradable et non corrosifs pour préserver les ornements',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            
        },   
    ]
    prix_cenotaphe =[
        {
            'id': 1,
            'name' : 'nettoyage simple',
            'prix' : '60€',
            'mention1' : '🌿 une évaluation complète de l\'état de la tombe est réalisée.',
            'mention2' : '🌿 Retrait des feuilles mortes, déchets et autres débris végétaux',
            'mention3' : '🌿 Un nettoyage en profondeur de la pierre tombale avec le respects des matériaux (granite, marbre, pierre naturelle)',
            'mention4' : '🌿 Élimination de la mousse et des algues',
            'mention5' : '🌿 Nettoyage en profondeur des inscriptions sur la pierre tombale, (gravures, noms, dates, etc.)',
            'mention6' : '🌿 Après néttoyage, une verification finales est faite afin de voir si la tombe est en ordres et propres ',
            'mention7' : '📷 une photo avant et après l\'intervention sera effectuée.',

        },
        {
            'id': 2, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '90€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 une évaluation complète de l\'état de la tombe est réalisée.',
            'mention2' : '🌿 Retrait des feuilles mortes, déchets et autres débris végétaux',
            'mention3' : '🌿 Un nettoyage en profondeur de la pierre tombale avec le respects des matériaux (granite, marbre, pierre naturelle)',
            'mention4' : '🌿 Élimination de la mousse et des algues',
            'mention5' : '🌿 Nettoyage en profondeur des inscriptions sur la pierre tombale, (gravures, noms, dates, etc.)',
            'mention6' : '🌿 Après néttoyage, une verification finales est faite afin de voir si la tombe est en ordres et propres. ',
            'mention8' : '🌿 Dépose des nouvelles fleurs.',
            'mention7' : '📷 une photo avant et après l\'intervention sera effectuée.',

        },
        {
            'id': 3, 
            'name': 'fleurissement', 
            'prix': '35€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Rinçage de la dalle',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            'mention4' : '📷 une photo avant et après l\'intervention',
        },
        
    ]
    
    prix_tombe_plaine_terre = [
        {
            "id" :1,
            'name': 'Entretien simple',
            'prix': '50€',
            'mention1' : '🌿 Néttoyage de la stèle, déserbages des mauvaises herbes et des déchets existants.',
            'mention2' : '🌿 Entretien des plantes existante.',
            'mention3' : '🌿 renivellement du terrain en cas d\'affaissement.',
            'mention4' : '📷 photo avant et après l\'intervention',
        },
        {
            'id': 2, 
            'name': 'fleurissement', 
            'prix': '35€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Rinçage de la dalle',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            
        },
        {
            'id': 3, 
            'name': 'Ajouts ou remplacement des fleurs ou des galets etc...',
            'prix': 'suppléments',
            'devis' : 'veuillez regarder la page suppléments pour accéder au tarif et me contacter ultérieurements.',
            'mention1' : '🌿 Remplacement des galets',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            'mention3' : '🌿 Nettoyage des ornements comme plaque funéraire, fleurs artificielles etc...',
            'mention4' : '📷 photo avant et après l\'intervention',
        },
    ]
    prix_monument_paysager = [
        {
            "id" :1,
            'name': 'Entretien simple',
            'prix': '70€',
            'mention1' : '🌿 Une évaluation complète de l\'état de la tombe est réalisée.',
            'mention2' : '🌿 Nettoyage de la stèle, enlèvement des mauvaises herbes et des déchets existants.',
            'mention3' : '🌿 Entretien des plantes existante.',
            'mention4' : '🌿 renivellement du terrain en cas d\'affaissement.',
            'mention5' : '📷 photo avant et après l\'intervention', 
        },
        {
            'id': 2, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '110€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Une évaluation complète de l\'état de la tombe est réalisée.',
            'mention2' : '🌿 Retrait des feuilles mortes, déchets et autres débris végétaux',
            'mention3' : '🌿 Un nettoyage en profondeur de la pierre tombale avec le respects des matériaux (granite, marbre, pierre naturelle)',
            'mention4' : '🌿 Élimination de la mousse et des algues',
            'mention5' : '🌿 Nettoyage en profondeur des inscriptions sur la pierre tombale, (gravures, noms, dates, etc.)',
            'mention6' : '🌿 Après néttoyage, une verification finales est faite afin de voir si la tombe est en ordres et propres. ',
            'mention7' : '🌿 Dépose des nouvelles fleurs.',
            'mention8' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
           'id': 3, 
            'name': 'remplacements de galets gravier ou autre...', 
            'prix': 'suppléments',
            'devis': 'Le remplacement ou l\'ajout des ornements spéciaux se fera sur devis.',
            'mention1' : '🌿 néttoyage complets de tout les ornements avec des produits biodégradable et non corrosifs pour préserver les ornements',
            'mention2' : '🌿 Dépose des fleurs, plantation de fleurs de saison ou la pose d\'un pots de fleurs sur le monuments.',
            'mention3' : '🌿 Ajout ou remplacement de galets ou terreaux.'
        },

    ]
    prix_jardin_souvenir =[
        {
            "id" :1,
            'name': 'Entretien simple',
            'prix': '50€',
            'mention1' : '🌿 Nettoyage de la stèle avec du savons doux, enlèvement des mauvaises herbes et des déchets existants.',
            'mention2' : '🌿 Entretien des plantes existante.',
            'mention4' : '📷 photo avant et après l\'intervention', 
        },
        {
            'id': 2, 
            'name': 'Néttoyage avec fleurissement', 
            'prix': '110€',
            'devis': 'Pour un choix personnalisé des fleurs, cela ce fera sur devis.',
            'mention1' : '🌿 Une évaluation complète de l\'état du monument est faites.',
            'mention2' : '🌿 Retrait des feuilles mortes, déchets et autres débris végétaux',
            'mention3' : '🌿 Un nettoyage en profondeur de la pierre tombale avec le respects des matériaux (granite, marbre, pierre naturelle)',
            'mention5' : '🌿 Nettoyage en profondeur des inscriptions, (gravures, noms, dates, etc.)',
            'mention6' : '🌿 Après néttoyage, une verification finales est faite afin de voir si le monumetns est en ordres et propres. ',
            'mention7' : '🌿 Dépose des nouvelles fleurs.',
            'mention8' : '📷 une photo avant et après l\'intervention sera effectuée.',
        },
        {
            'id': 3, 
            'name': 'remplacements de galets gravier ou autre...', 
            'prix': 'suppléments',
            'devis': 'Le remplacement ou l\'ajout des ornements spéciaux se fera sur devis.',
            'mention1' : '🌿 ajout ou changement des galets disposés au sol.',
            'mention2' : '🌿 néttoyage des ornements',
        },
    ]
    prix_speciale =[
        {
            'id': 1,
            'name': 'nettoyage avec produit anti-mousse.',
            'prix': '+20€',
            'mention1' : '🌿 Utilisation de produits anti-mousse bon pour l\'environnement.',
            'mention2' : '🌿 Déposer le produit sur la surface à traiter.',
            'mention3' : '🌿 Laisser le produit agir en fonction des recommandations du fabricant.',
            'mention4' : '🌿 Rincer et sécher avec de l\'eau claire et un chiffon doux.',
        },
        {
            'id': 2,
            'name': 'Rechampissage des lettres sur stèle et ornements.',
            'prix': '+2.50€',
            'explication' :'( par lettre )',
            'mention1': '🌿 Nettoyage et enlèvement total des anciennes lettres existante.',
            'mention2': '🖌️ Pose de la peinture dorée.',
            'mention3': '🖌️ Vernire la peinture pour une meilleur teneur dans le temps ', 
            'but':'✨ La pose de ce vernis sert a protégées des UV,de l’humidité,de la poussière,des mousses,de la pollution,des frottements et des pluies acides',
        },
        {
            'id': 3, 
            'name': 'Remplacement de plantes enterrées.',
            'prix': '+40€',
            'explication' :'( par plantes )',
            'mention1': '🌿 Enlèvements de l\'ancienne plante.',
            'mention2':'🌿 Mise en place de la nouvelle plante.',
            'mention3': '🌿 Remise a niveaux du terrain et enlèvement des feuille morte et déchets existant.',
        },
        {
            'id': 4, 
            'name': 'Remplacement des galets, cailloux, copaux de bois,etc...',
            'prix': 'Sur devis',
            'mention1': '🌿 Enlèvements des anciens galets, cailloux ou autre.',
            'mention2':'🌿 Mise en place des nouveaux galets.',
            'mention3': '🌿 Renivellement du terrain avec les nouveaux galets.',
        },
        {
            'id': 5, 
            'name': 'Nettoyage des ornement',
            'prix': '+2€ (par ornement)',
            'mention1': '🌿 Nettoyage avec savons doux, rinçage de chaque ornement.',
            'mention2': '🌿 Séchez avec chiffon ou micro-fibre.',
            'mention3': '🌿 Repositionnement des ornements.',
        },
        ]
    return render(request, f"tarif/tarif{numero_tarif}.html", {
        'prix_tombe_simple': prix_tombe_simple,
        'prix_cavurne': prix_cavurne,
        'prix_columbarium': prix_columbarium,
        'prix_cenotaphe': prix_cenotaphe,
        'prix_monument_paysager': prix_monument_paysager,
        'prix_tombe_plaine_terre': prix_tombe_plaine_terre,
        'prix_jardin_souvenir': prix_jardin_souvenir,
        'prix_speciale' :prix_speciale,
    })

