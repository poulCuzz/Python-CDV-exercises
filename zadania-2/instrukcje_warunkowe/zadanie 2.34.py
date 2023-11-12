# !!!kod nie dziala po wklejeniu tekstu z enterami!!!
import re
text = input("Wklej poniżej swoją pracę: " + "\n")
finalString = re.sub(r'\s', '', text)
print(f"Tekst posiada {len(finalString)} znaków")
if len(finalString) < 500:
    print("Tekst niezgodny z wymogami")
else:
    print("Tekst zgodny z wymogami")


