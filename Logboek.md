# Logboek Fruit Catcher | Erhan Citil

In dit bestand ga ik dagelijks bijhouden wat ik heb gedaan voor dit project en of ik tegen problemen ben aangelopen.

## Dag 1: Vooronderzoek

Datum: 14-06-2024

Vandaag heb ik vooronderzoek gedaan naar welke programmeertaal ik wil gebruiken tijdens het bouwen van mijn game. Ik ben tot een besluit gekomen om de taal Python te gebruiken, want ik ben best wel bekend met deze taal aangezien ik ook mijn stage in deze taal heb gelopen. Dankzij deze game development examen zal ik tevens mijn Python skills verder uitbreiden. 

#### **Taken**:
- Onderzoek doen welke taal het meest efficient is om te gebruiken voor mijn game
- Onderzoek doen naar PyGame (Python Library om videospelletjes te bouwen en te runnen in Python)
- Een tutorial gevolgd naar PyGame

Voor de rest ben ik niet tegen problemen aangelopen aangezien ik nog niet echt iets complexs voor elkaar heb gezet. 

## Dag 2: Projectvoorbereiding

Datum: 17-06-2024

Vandaag heb ik de game design document ingevuld, daarin heb ik uitgelegd hoe mijn game er uit zal zien en een timeline en sketch gemaakt. Daarnaast ben ik ook bezig geweest met het verdere onderzoek naar PyGame en naar andere libraries in Python om games mee te runnen. Wellicht dat er een library is die beter past bij de game die ik ga bouwen.

#### **Taken**:
- Game Design Document ingevuld (Game uitleg, timeline en sketch)
- Onderzoek doen naar PyGame en ook naar andere alternatieven

## Dag 3: Basisfunctionaliteiten van de game

Datum: 18-06-2024

Ik heb besloten om voor mijn project in Python versie 3.10 te gaan werken. Dit is de LTS versie van Python. De reden dat ik niet voor een nieuwere Python versie ga is, omdat ik niet te maken wil hebben met libraries die een verdere Python versie niet ondersteunen. Vandaag heb ik een beginnetje gemaakt en een startpagina gemaakt met een play button. De tekst die het bedrijf wilt die staat er in en bedrijfslogo. Als je op play klikt dan krijg je een fruit basket te zien die je naar links en rechts kan bewegen. Morgen zal ik mijn best doen om fruit te laten vallen vanuit de lucht.

#### **Taken**:
- Van start gegaan met het bouwen van mijn game (Begin scherm gemaakt met de functionaliteit dat je de game kan starten door op de button te klikken en daarna zie je een winkelmand die je kan bewegen)
- Gitignore bestand toegevoegd aangezien ik werk met Python en daar komen veel bestanden bij kijken (virtual environment bestanden etc) die ik niet mee gepushed wil hebben.
- README bestand aangemaakt en aangevuld met instructies om alles te installeren en te gebruiken.

Ik liep niet echt tegen een probleem aan, het enige was dat ik niet begreep wat screen.blit deed. Ik las de documentatie maar begreep het alsnog niet, omdat er staat dat de foto's die ik mee geef getekend worden op het scherm. Dit heb ik nagevraagd bij Rob en hij heeft me uitleg gegeven. 

Vanaf morgen ben ik van plan om issues te gaan aanmaken voor de dingen die ik van plan ben om te gaan afronden zodat ik dat ook in mijn commit berichten kan noteren. Dit vind ik zelf heel erg handig.

## Dag 4: Basisfunctionaliteiten van de game

Datum: 19-06-2024

Vandaag heb ik gewerkt aan een aantal dingen. Ik heb vandaag er voor gezorgd dat er fruitstukken (gezonde en halve) uit de lucht vallen. Daarnaast heb ik ook een scoreboard gemaakt waarbij je plus punten krijgt als er fruitstukken in je fruitmand vallen. De functionaliteit dat je min punten krijgt voor halve fruitstukken heb ik nog niet geimplementeerd. Dat staat op de planning om morgen te doen. Tot slot heb ik vandaag gebruik gemaakt van issues en branches, dat vind ik zelf fijner om mee te werken, omdat je dingen van elkaar onderscheid. Daarnaast heb ik ook in plaats van in 1 bestand (main.py) te werken 2 andere bestanden gemaakt. Dit zodat het niet voor chaos zorgt in mijn main.py bestand.

#### **Taken**:
- De basis game functionaliteit toegevoegd 

Vandaag ben ik niet tegen problemen aangelopen.

## Dag 5: Bom en minpunten functionaliteit

Datum: 20-06-2024

Vandaag heb ik gewerkt aan de functionaliteit dat de bom uit de lucht valt en dat het spel eindigt als de bom in de fruitmand valt. Daarnaast heb ik ook de functionaliteit toegevoegd dat je minpunten krijgt als er halve fruitstukken in je fruitmand vallen. Tot slot heb ik wat unit tests geschreven om te valideren dat mijn code correct werkt. Ik ben van plan om GitHub Actions te integreren zodat deze tests automatisch worden uitgevoerd.

#### **Taken**:
- Functionaliteit voor de bom dat de game eindigt
- Functionaliteit voor min punten voor halve fruitstukken
- Bugs gefixt

Vandaag ging wel prima alleen ik had best wel wat moeite met het coderen van de functionaliteit van de bom.

## Dag 6: Spel moeilijker maken en testresultaten

Datum: 24-06-2024

Vandaag ga ik aan de slag met het implementeren van functionaliteiten waardoor het spelletje moeilijker wordt naarmate je het speelt. Zo zullen er bijvoorbeeld meer bommen vallen en de snelheid van de fruitstukken wordt iets sneller. Daarnaast een probleem die ik ondervind die ik heb gevonden toen ik het spelletje ging testen samen met Batuhan en Djafny is dat de kans dat volle fruitstukken en halve fruitstukken vallen niet gelijk zijn. Dus ik ga dat vandaag proberen op te lossen door middel van deze 2 fruitstukken te verdelen in 2 lijsten en gewogen deling te maken. In mijn code bestand zal er dan 50/50 kans zijn tussen deze twee fruiten die er zullen vallen.

#### **Taken**:
- Oplossen van geen gelijkheid van kans bij het vallen van gezonde en ongezonde fruitstukken
- Definieren van de hitbox
- Game die moeilijker wordt naarmate je het speelt

#### Test uitslagen 24 juni 

Batuhan en Djafny hebben mijn spelletje getest en we kwamen er samen achter dat er geen gelijkheid was bij het vallen van de fruitstukken en halve fruitstukken. Daarnaast was de hitbox nog niet goed geconfigureerd. Dit is heel erg vervelend, omdat als er een bom valt naast je fruitmand dan wordt het spelletje beeindigt.