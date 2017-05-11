#!/usr/bin/env python3
import sys
import datetime
import time
from functools import cmp_to_key
from random import Random

TGT = sys.argv[1]
NOW = datetime.datetime.now()

import feedparser

def forbiddenMeta(meta):
    for w in ('satire', 'quiz'):
        if w in meta:
            return True
    return False

def get_default(name, feedurl):
    feed = feedparser.parse(feedurl)
    print("fetch "+feedurl)
    home_url = getattr(feed.feed, 'link', feedurl)
    name = '<a href="%s" class="meta">%s</a>' % (home_url, name)
    afternoon = (NOW.hour >= 12)
    for e in feed.entries:
        if not hasattr(e, 'published_parsed'):
            continue
        if not e.published_parsed:
            continue
        dt = datetime.datetime.fromtimestamp(time.mktime(e.published_parsed))
        dt_diff = NOW - dt
        if dt_diff.days > 0:
            continue # skip news older than 24h
        if afternoon and dt.day != NOW.day:
            continue # skip yesterday's news
        tags = ""
        if hasattr(e, 'tags'):
            tags += ' ' + ', '.join(i['term'] for i in e.tags)
        if forbiddenMeta(tags.lower()):
            continue
        title = getattr(e, 'title', '–')
        link = getattr(e, 'link', '')
        value = valueItem((e.link, title, name, dt, tags))
        yield e.link, title, name, dt, tags, value

def valueItem(item):
    value = 0
    # Value title content
    title = item[1].lower()
    for w in ('lidl', 'aldi', 'karlsruhe', 'snowden'):
        if w in title:
            value += 31
    for w in ('datenschutz', 'netzpol', 'amnesty', 'ceta', 'aleppo', 'wikipedia', 'eugh', 'maidan', 'nafta', 'nato', 'uno', 'krankenkasse', 'vg-wort', 'guantanamo', 'fukushima', 'bitcoin', 'lammert'):
        if w in title:
            value += 21
    for w in ('türkei', 'putin', 'hochschule', 'urteil', 'verdi', 'apple', 'google', 'microsoft', 'ibm', 'iwf', 'ezb', 'griechenland', 'volksbegehren', 'brexit', 'airbus', 'pentagon', 'energiewende', 'windkraft', 'lindner', 'paragraf', 'ditib', 'nobelpreis', 'armutsgrenze', 'bundesbank', 'betriebsrat', 'sparkurs', 'bundesrat', 'shinzō', 'libyen', 'mogherini', 'indexfond', 'orbán', 'panama-papers', 'juncker', 'netanyahu', 'deutsche bank', 'cyber-sicherheit', 'yellen', 'windenergie', 'maizière'):
        if w in title:
            value += 15
    for w in ('nsu', 'korruption', 'siedlung', 'steinmeier', 'überwachung', 'fracking', 'android', 'bundesverwaltungsgericht', 'bundesnetzagentur', 'nationalpark', 'syri', 'winterkorn', 'piëch', 'afghan', 'erdoğan', 'böhmermann', 'wissenschaft', 'endlager', 'palästin', 'nahost', 'tsipras', 'rente', 'unternehmenssteuer', 'wilders', 'krankenversicherung', 'gesetz', 'klimaschutz', 'jong-un', 'trudeau', 'BND', 'drohnen', 'peugeot', 'opel', 'orbán', 'reisepass'):
        if w in title:
            value += 9
    for w in ('afd', 'usa', 'trump', 'minister', 'bundestag', 'wahl', 'e-sport', 'gentechnik', 'merkel', 'amazon', 'ebay', 'paypal', 'altmaier', 'schäuble', 'grexit', 'ukraine', 'agrar', 'portugal', 'sanktionen', 'samsung', 'gysi', 'lagarde', 'vorratsspeicherung', 'norovirus', 'unilever', 'patientenakte', 'bannon', 'telefónica', 'sudan', 'unicef', 'fintech', 'salafis', 'sufis', 'exportüberschuss', 'telekom', 'passwort', 'bertelsmann', 'kindergeld', 'martin schulz'):
        if w in title:
            value += 7
    for w in ('ddos', 'berlin', 'china', 'bundespolizei', 'russland', 'japan', 'lebensversicherung', 'präsident', 'facebook', 'anschlag', 'europa', 'deutsch', 'immobilie', 'whatsapp', 'google', 'mcmaster', 'leistungsschutzrecht', 'bafin', 'le pen'):
        if w in title:
            value += 2
    for w in ('experte', 'deepmind', 'gauland', 'bundeswehr', 'delfin', 'foto', 'generation', 'vorwürfe', 'unmut', 'übersicht', 'paukenschlag', 'dax', 'mord', 'hollywood', 'kampf', 'oscar', 'homöopath'):
        if w in title:
            value -= 1
    for w in ('film', 'wunder', 'unisex', 'tweet', 'top ten', 'fantasi', 'sexuell', 'vögel', 'fußball', 'dfb', 'wahrheit', 'manager', 'salat', 'voodoo', 'berlinale', 'portal', 'theater', 'schmutzig', 'killer', 'kolumne', '?', 'skandal', 'cowboy', 'essay', 'kritik', 'münchen', 'selfie', 'mode', 'terror', 'emotion', 'viral', 'nachruf', 'sonneborn', 'seehofer', 'kokain', 'marx', 'junkie', 'ikone', 'egoismus', 'karikatur', 'promi', 'schock', 'kreissäge', 'valentinstag', 'nackt', 'könnte', 'bizarr', 'spiel', 'stur', 'gefährlich', 'hinweise', 'meinung', 'goethe', 'schiller', 'karneval', 'fasnacht', 'fastnacht', 'fasching', 'pizza', 'hölle', 'damokles', 'teambuilding', 'doping', 'knigge'):
        if w in title:
            value -= 8
    for w in ('kunst', 'mies', 'bayern', 'horror', 'brutal', 'compact', 'protz', 'social', 'wollmilch', 'olympia', 'kommentar', '+++', 'schicksal', 'billig', 'troll', 'hashtag', 'betrunken', 'lügendetektor', 'thriller', 'mutig', 'spektakulär', 'krass', 'checkliste', '!', 'zombie', 'willkommen', 'elfmeter', 'spiegel tv', 'video', 'sex', 'ficken', 'saufen', 'schonungslos', 'trumpismus', 'crazy', 'kamikaze', 'buchtipp', 'verkackt', 'playboy', 'gastbeitrag', 'shitstorm', 'wäre', 'abgemagert', 'einhorn'):
        if w in title:
            value -= 19
    if len(title) < 15:
        value -= 23
    if len(title) < 30:
        value -= 10
    if len(title) < 40:
        value -= 4
    # Value sources
    source = item[2]
    for w in ('NP', 'Correctiv'):
        if w in source:
            value += 3
    for w in ('ZEIT', 'NZZ', 'HB', 'FAZ', 'SZ'):
        if w in source:
            value += 2
    for w in ('SpOn', 'Konj'):
        if w in source:
            value += 1
    for w in ('Taz', 'Compact'):
        if w in source:
            value -= 1
    for w in ('RT',):
        if w in source:
            value -= 2
    # Value tags
    tags = item[4].lower()
    for w in ('mode', 'video', 'bundesliga'):
        if w in tags:
            value -= 27
    return value

def get_All():
    all = list()
    all.extend(get_default('ZEIT', 'http://newsfeed.zeit.de/index'))
    all.extend(get_default('SpOn', 'http://www.spiegel.de/index.rss'))
    all.extend(get_default('FAZ', 'http://www.faz.net/rss/aktuell/'))
    all.extend(get_default('SZ', 'http://rss.sueddeutsche.de/rss/Topthemen'))
    all.extend(get_default('Heise', 'https://www.heise.de/newsticker/heise-top-atom.xml'))
    all.extend(get_default('Taz', 'https://www.taz.de/!p4608;rss/'))
    all.extend(get_default('Focus', 'http://rss.focus.de/'))
    all.extend(get_default('RT', 'https://deutsch.rt.com/feeds/news/'))
    all.extend(get_default('TP', 'https://www.heise.de/tp/news-atom.xml'))
    all.extend(get_default('HB', 'http://www.handelsblatt.com/contentexport/feed/top-themen/'))
    all.extend(get_default('Compact', 'https://www.compact-online.de/feed/'))
    all.extend(get_default('Correctiv', 'https://correctiv.org/artikel/feeds/'))
    all.extend(get_default('NP', 'https://netzpolitik.org/feed/'))
    all.extend(get_default('WU', 'http://www.wahlumfrage.de/feed/'))
    all.extend(get_default('Carta', 'https://feeds2.feedburner.com/carta-homepage-rss'))
    all.extend(get_default('BG', 'https://feeds.feedburner.com/BerlinerGazette'))
    all.extend(get_default('Konj', 'https://www.konjunktion.info/feed/'))
    all.extend(get_default('NZZ', 'https://www.nzz.ch/international.rss'))
    all.extend(get_default('Freitag', 'https://www.freitag.de/politik/@@RSS'))
    all.extend(get_default('Cicero', 'http://cicero.de/rss.xml'))
    all.extend(get_default('WiWo', 'http://www.wiwo.de/contentexport/feed/rss/schlagzeilen'))
    all.extend(get_default('NDS', 'http://www.nachdenkseiten.de/?feed=atom'))
    #all.extend(get_default('DF', 'http://www.deutschlandfunk.de/die-nachrichten.353.de.rss'))
    #all.extend(get_default('ParsToday', 'http://parstoday.com/de/rss'))
    rng = Random(42)
    rng.shuffle(all)
    def mycmp(a, b):
        va = a[5]
        vb = b[5]
        if va > vb: return -1
        if va < vb: return  1
        da = a[2]
        db = b[2]
        if da > db: return -1
        if da < db: return  1
        return 0
    all.sort(key=cmp_to_key(mycmp))
    return all

def generate(fh):
    fh.write("""
    <!DOCTYPE html>
    <html><head><title>TextNews {NOW}</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta http-equiv="refresh" content="2000">
    <style>
    html, body {{ font-family: sans-serif; font-size: 99%; }}
    a.meta {{ color: inherit; }}
    h1 {{ font-weight:normal; }}
    p.fresh time {{ background-color: #d74; color: #ffc; padding: 0 2px; }}
    p.yesterday a:link {{ color: #333; }}
    .value {{ color: #ccc; }}
    </style>
    </head><body>
    <h1 style="font-size:80%">Text<b>News</b> {NOW}</h1>
    """.format(NOW=NOW.isoformat().replace("T", " ")[:-10]))

    for link, title, src, dt, tags, value in get_All():
        css_classes = list()
        if ((NOW - dt).seconds) < (2 * 60 * 60) and NOW > dt:
            css_classes.append('fresh')
        if (NOW.day != dt.day):
            css_classes.append('yesterday')
        dt = dt.isoformat()
        dt = '<time datetime="%s">%s</time>' % (dt, dt.replace("T", " ")[11:-3])
        if css_classes:
            fh.write('<p class="%s">' % (' '.join(css_classes)))
        else:
            fh.write('<p>')
        if link:
            fh.write('<a href="%s">%s</a>' % (link, title))
        else:
            fh.write('<a>%s</a>' % (title,))
        fh.write(' %s %s %s <span class="value">%s</span></p>' % (src, dt, tags, value))

    fh.write('<p>Deutsche Nachrichten als reiner Text. <a href="https://github.com/qznc/textnews">Code auf GitHub</a>.</p>')
    fh.write("</body></html>")

with open(TGT, "w") as fh:
    generate(fh)
