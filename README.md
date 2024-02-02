# Duomenų analitika ir Python programavimas
Baigiamasis projektas 

Darbo autorius: Giedrius Leskevičius.

Projekto tema: Futbolo žaidėjų atlygio analizė.

Projekto tikslas: Išanalizuoti, kas įtakoja žaidėjo atlygį.

Panaudotos bibliotekos: requests, pandas, matplotlib, silenium, BeautifulSoup

### _main.py_

Pagrindinis failas, kuriame yra visų grafikų funkcijų kvietimai (call).


### _GetPlayers.py_

Duomenys apie žaidėjus gauti iš puslapio https://www.fifacm.com/players.\
Sukurta funkcija get_players()


### _ChartLikes.py_

zaidejai pagal populiaruma ('Likes').\
Funkcija: populiarumas()
![zaideju_likes](https://github.com/litpost/PythonStudies/assets/19422665/41dc6b27-12c2-4423-8010-85faa2515ca8)


### _ChartWageAge.py_

Užmokesčio ir kainos priklausomybė nuo amžiaus.\
Funkcija: amzius_kaina_DU()
![KainaAtlygis](https://github.com/litpost/PythonStudies/assets/19422665/effa035d-ba0b-4801-b79c-db7ebe57533a)


### _ChartSkills.py_

Įgūdžių priklausomybė nuo amžiaus.\
Funkcija: igudziai(amzius_nuo,amzius_iki)
![zaideju_igudziai](https://github.com/litpost/PythonStudies/assets/19422665/67434e4a-c836-4f10-bddd-cd6af7cd532d)



### _ChartHeight.py_

Zaidėjų pasiskirstymas pagal ūgį.\
Funkcija: zaideju_ugis()
![zaideju_ugis](https://github.com/litpost/PythonStudies/assets/19422665/52fff719-b38d-4a27-8dde-2f58eab41e41)



### _ChartHeightSkills.py_

Žaidėjų įgūdžiai pagal ūgio grupes.\
Funkcija: zaideju_ugis_igudziai()
![zaideju_igudziai_ugio_grupe](https://github.com/litpost/PythonStudies/assets/19422665/8bf913a1-ee3f-46e3-a380-e29efde5b181)


## Išvados
Pirmas grafikas "Populiarumas" atspindi visuomenės nuomonę, kuri ne visada sutampa su profesionalų nuomone. Matome, kad pirmoje vietoje Erling Haaland, o žinomas žaidėjas Messi tik trečioje, todėl ši informacija neparodo tikrųjų žaidėjo kompetencijų.

Kainos ir atlygio grafike matome, kad su metais žaidėjai netenka atlygio bei už jį klubai pasiruošę mokėti mažiau. Tačiau yra išimčių, kas matoma ties 33 ir 34 metų amžiumi. Šiame amžiuje šiuo atveju turime keleta žaidėjų su gerais įgūdžiais. Tą galime stebėti trečiame grafike. Jie aukštai vertinami ir jiems mokamas geras atlygis.

Paskutiniai du grafikai pateikia žaidėjų ūgį. Čia galime daryti išvadą, kad nors dauguma žaidėjų yra aukštaūgiai, daugiausia įgūdžių turi vidutinio ūgio žaidėjai nuo 170 cm iki 179 cm.

Bendra išvada: Atlygį daugiausia įtakoja žaidęjo amžius ir įgūdžiai.



