champs="bolet Boletus_edulis Bolet_Satan Bolet_à_chair_jaune Boletus_badius Bolet_blafard"
for champ in $champs
do
    echo importation de $champ
    curl "https://fr.wikipedia.org/w/index.php?title=${champ}&action=raw" > PAGES/$champ
done
