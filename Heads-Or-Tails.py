#Write your code below this line 👇
#Hint: Remember to import the random module first. 
importer  au hasard

# un numéro de graine signifie que nous donnons la fonction aléatoire
# un point à partir duquel commencer manuellement
test_seed  =  int ( input ( "Créer un numéro de départ : " ))
aléatoire . graine ( test_seed )

# la variable randomSide fait référence à une pièce ayant deux faces
côté aléatoire  =  aléatoire . aléatoire ( 0 , 1 )
si  randomSide  ==  1 :
    imprimer ( "Têtes" )
sinon :
    imprimer ( "Tails" )







