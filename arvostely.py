kaikki = 201
ylaraja = kaikki * 0.9  # 90 % oikeuttaa tasan arvosanaan 5
alaraja = kaikki * 0.25  # 25 % tehtävistä oikeuttaa arvosanaan 1

arvosanapisteet = (ylaraja - alaraja) / 4

print('Arvosteluasteikko:')
for arvosana in (1, 2, 3, 4, 5):
    pisteet = alaraja + (arvosana-1) * arvosanapisteet
    print(f'Arvosana {arvosana}: {round(pisteet)} pistettä')


minimi = 25     # 25 %
maksimi = 100   # 100 %


def laske_arvosana(pisteet: int) -> float:
    if pisteet >= minimi:
        return 1 + 4 * (pisteet - minimi) / (maksimi - minimi)
    else:
        return 0


for i in range(0, 101):
    arvosana = laske_arvosana(i)
    print(f'{i:3} %: {round(laske_arvosana(i), 2)}  ({round(arvosana)})')

tilasto = {arvosana: [] for arvosana in (0, 1, 2, 3, 4, 5)}

for pisteet in range(0, 101):
    arvosana = round(laske_arvosana(pisteet))
    tilasto[arvosana] += [pisteet]

for arvosana, pistelista in tilasto.items():
    print(f'{min(pistelista):2} - {max(pistelista):3} %: {arvosana}')
