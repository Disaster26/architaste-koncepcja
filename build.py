import os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: open(os.path.join(D, f), encoding='utf8').read()

REAL = [
    ('zlote', 'Złote a skromne', 'Mieszkanie'),
    ('medimprove', 'Wnętrze, w którym możesz poczuć się bezpiecznie', 'MEDIMPROVE, gabinet'),
    ('sarny', 'W zgodzie z naturą, sarny za płotem', 'Dom'),
    ('kobiecy', 'Kobiecy perfekcjonizm, bez zbędnych detali', 'Mieszkanie'),
    ('czekolada', 'Tu się robi czekoladę, blat z kamienia daje radę', 'Kuchnia'),
    ('monadi', 'Psychoterapia nie taka straszna', 'MONADI, gabinet'),
    ('dzieci', 'Kolorowo, nietypowo, tu mieszkają dzieci', 'Pokój dziecięcy'),
    ('nela', 'Rodzina 2+2, Nela w drodze', 'Mieszkanie'),
    ('kontrast', 'Potęga kontrastu', 'Sypialnia'),
    ('koma', 'W górach szaleństwa', 'KOMA HOUSE'),
    ('miedzy', 'Między kuchnią a salonem', 'Mieszkanie'),
]
OFERTA = [
    ('p63', 'Mieszkanie', 'Układ, kolory, oświetlenie i meble dla całego mieszkania.'),
    ('salon', 'Dom', 'Wnętrza domu od strefy dziennej po poddasze.'),
    ('p60', 'Kuchnia', 'Zabudowa na wymiar, która ułatwia gotowanie.'),
    ('damsko', 'Łazienka', 'Wygodna i łatwa w utrzymaniu, także na małym metrażu.'),
    ('dom', 'Salon', 'Miejsce dla domowników i gości, z przemyślanym światłem.'),
    ('p62', 'Pokój dziecięcy', 'Wnętrze, które rośnie razem z dzieckiem.'),
    ('biuro', 'Biuro', 'Przestrzeń do pracy dla zespołu i klientów.'),
    ('p59', 'Restauracja i lokal', 'Kawiarnie, restauracje, sklepy i gabinety.'),
]


def img(n, alt, sizes, eager=False):
    return (f'<img src="img/{n}-600.webp" srcset="img/{n}-600.webp 600w, img/{n}-900.webp 900w" '
            f'sizes="{sizes}" width="600" height="450" alt="{alt}" '
            + ('' if eager else 'loading="lazy" ') + 'decoding="async">')


real = '\n'.join(
    f'<li class="kr"><button class="kr-f" type="button" data-full="img/{n}-900.webp" data-cap="{t}">'
    f'{img(n, t, "(min-width:1700px) 440px, (min-width:1280px) 31vw, (min-width:760px) 46vw, 84vw")}</button>'
    f'<p class="kr-t">{t}</p><p class="kr-k">{k}</p></li>' for n, t, k in REAL)
ofe = '\n'.join(
    f'<li class="of"><button class="of-f" type="button" data-full="img/{n}-900.webp" data-cap="{t}">'
    f'{img(n, "Projekt: " + t.lower(), "(min-width:1100px) 25vw, 50vw")}</button>'
    f'<h3>{t}</h3><p>{o}</p></li>' for n, t, o in OFERTA)

html = rd('src.html')
html = (html.replace('{{BADGE_STYLE}}', rd('_badge_style.part'))
            .replace('{{BADGE_LINK}}', rd('_badge_link.part'))
            .replace('{{REAL}}', real).replace('{{OFERTA}}', ofe))
open(os.path.join(D, 'index.html'), 'w', encoding='utf8').write(html)
print('ok', len(html))
