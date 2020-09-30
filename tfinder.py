from bs4 import BeautifulSoup
import requests, webbrowser, os, time
from colorama import Fore, init

init()

colours = {
    'green': Fore.LIGHTGREEN_EX,
    'darkgreen': Fore.GREEN,
    'cyan': Fore.LIGHTCYAN_EX,
    'red': Fore.LIGHTRED_EX,
    'magenta': Fore.LIGHTMAGENTA_EX,
    'yellow': Fore.LIGHTYELLOW_EX,
    'white': Fore.LIGHTWHITE_EX,
    'darkyellow': Fore.YELLOW
}

logo = """
		 _____   _____ _           _
		|_   _| |  ___(_)_ __   __| | ___ _ __
		  | |   | |_  | | '_ \ / _` |/ _ \ '__|
		  | |_  |  _| | | | | | (_| |  __/ |
		  |_(_) |_|   |_|_| |_|\__,_|\___|_|
 """
credit = '''
     [+] by Cypher               [+] connected with - 1337x.to
----------------------------------------------------------------'''

print(colours['green'] + logo + '\n' + credit)

# checking internet
try:
    requests.get("https://www.google.com")
except:
    print(colours['red'] + "[!] Not Connected to the internet")
    print("[!] Exiting in 5 secs ...")
    time.sleep(5)
    exit()

names, links, seeds, leeches, sizes, times = [], [], [], [], [], []  # userට පෙන්නන්න ඕනේ දේවල් ටික list වලට ගන්නවා

cats = """
[!] These are Catergories 
     (1) Movies
     (2) Games 
     (3) Musics
     (4) Applications """
print(colours['cyan'] + cats)


def details():
    global search, catergory
    print(colours['cyan'])

    catNum = input("[+] Enter Catergory Number : ")
    if catNum == '1':
        catergory = 'Movies'
        search = input(f"[+] Enter Movie Name : ").strip().replace(' ', '+')  # film එකේ නම ගන්නවා
    elif catNum == '2':
        catergory = 'Games'
        search = input(f"[+] Enter Game Name : ").strip().replace(' ', '+')  # game එකේ නම ගන්නවා
    elif catNum == '3':
        catergory = 'Music'
        search = input(f"[+] Enter Song Name : ").strip().replace(' ', '+')  # song එකේ නම ගන්නවා
    elif catNum == '4':
        catergory = 'Apps'
        search = input(f"[+] Enter Application Name : ").strip().replace(' ', '+')  # app එකේ නම ගන්නවා
    elif catNum == "":
        print("[!] Exiting in 3 secs")
        time.sleep(3)
        os.system('exit')
    else:
        print(colours['red'] + "Undefined Catergory !!")
        details()


def find_film(pageNo=1):
    details()
    time.sleep(2)
    print(colours['magenta'] + "\n[+] Request sending........")

    page = requests.get(
        f"https://1337x.to/category-search/{search}/{catergory}/{pageNo}/").text  # site එකට requests එකක් යවනවා
    #     Games
    # Apps
    # Music
    os.system('clear')
    time.sleep(3)
    print(colours['yellow'] + logo + '\n' + credit)

    soup = BeautifulSoup(page, 'html.parser')  # එකෙන් soup එකක් හද ගන්නන්ව

    error = soup.title

    if str(error) == '<title>Error something went wrong.</title>':  # page එකේ title එක මේක නං වෙන්න ඕන දේ
        print(colours['red'] + f'[!] Something went wrong\n[!] Please check you {catergory} name ..')
        print("Exiting in 5 secs ..")
        time.sleep(5)
        exit()

    else:
        hyperlinks = soup.find_all('a')  # <a> tag ඔක්කොම හොයල ඒවා ටික hyperlinks කියාලා list එකකට ගන්නවා

        for i in hyperlinks:  # i hyperlink එකේ තියෙනවා නං

            # hyperlink එකේ එක එක element එක href attribute එක link කියල list එකකට ගන්නවා (<a href='www.google.com'></a> මේකේ www.google.com වගේ)
            link = i.get('href')

            if '/torrent/' in link:  # ඒ ගත්ත links වල /torrent/ කියල තියේද බලනවා torrent link අඳුනගන්න

                # <a> tag එකක href එකේ ඉස්සසෙල්ල ගත්ත torrent කියන එක තියෙන link තියේද බලනවා
                name = soup.find('a', attrs={'href': link})
                names.append(name.text)  # තියෙන ටිකේ tag එක ඇතුලේ තියෙන text එක names list එකට දාගන්නවා
                links.append(
                    f"https://1337x.to{link}")  # හොයා ගත්ත link වලින් torrent එකේ full link එක හද ගෙන එක links වලට දාගන්නවා

        se = soup.find_all('td', attrs={'class': 'seeds'})  # seeds හොයනවා
        le = soup.find_all('td', attrs={'class': 'leeches'})  # leech හොයනවා
        sz = soup.find_all('td', attrs={'class': 'size'})  # size එක හොයනවා
        ti = soup.find_all('td', attrs={'class': 'coll-date'})

        for num in range(len(se)):
            leeches.append(le[num].text)  # හොයා ගත්ත information ටික අදාළ list වලට දාගන්නවා
            seeds.append(se[num].text)
            sizes.append(sz[num].text)
            times.append(ti[num].text)

        # sizes ගන්න කොට seeders ගානත් අන්තිමට එන හින්ද එක අයින් කරන්න මේ කොටස
        for abc in range(len(sizes)):  # sizes length එක abc  තියෙන තුරු
            while True:
                if sizes[abc][-1] == 'B':
                    # sizes list එකේ පලවෙනි element එකේ අන්තිම අකුර ගන්නවා (['abcd','xyz'] ->> මේකේ ගත්තොත් abcd වල 'd' එක)
                    break
                sizes[abc] = sizes[abc][:-1]  # sizes එකේ අදාල element එක අන්තිම අකුර හලලා ගන්නවා

        print(colours['darkyellow'])
        print("================================================")
        print("   [+] These torrent are found [+] ")
        print("================================================\n\n")

        for list in range(len(names)):
            # names list එකේ element ගාන ඉවර වෙනකන් (names,seeds,sizes,leech මේවා ඔක්කොම length එක සමානයි
            # user ට details ටික print කරනවා
            print(colours['white'], [list + 1],
                  colours['cyan'] + names[
                      list] + Fore.CYAN + f" \n\t(  Seeders : {seeds[list]} | Leeches : {leeches[list]} | Size : {sizes[list]} | Time : {times[list]} )\n ")

        def getting_film():
            global iLink  # iLink කියල global variable එකක් හදනවා

            print("----------------------------------------------------------------")
            # film එකට අදාළ number එක ගන්නවා list එකේ තියෙන පිළිවෙලට
            print(colours['yellow'])
            print(
                "[*] Is Your film not in list.. ok type " + colours['green'] + 'next' + colours[
                    'yellow'] + " for see next page")

            print("Enter Number you want to Get : " + colours['green'], end='')
            select = input()

            if select.isdigit():
                select = int(select)

                # ඕනේ torrent එකේ link එකෙන් request එකක් site එකට යවනවා
                torrentReq = requests.get(links[select - 1]).text
                torrentSoup = BeautifulSoup(torrentReq, 'html.parser')  # එක soup එකක් කර ගන්නවා
                torrentLink = torrentSoup.find_all('a')  # එකේ තියෙන ඔක්ක්කොම <a> tag ගන්නවා

                for link2 in torrentLink:
                    lnk = link2.get('href')  # ඒ <a> tag වල තියෙන href වලට අදාල value එක ගන්නවා (url එක )
                    if 'http://itorrents.org/' in lnk:  # ඒවගෙන් itorrents එකේ link ටික පෙරා ගන්නවා
                        iLink = lnk  # ඒවා iLink කියල variable එකට ගන්නවා (ඉස්සෙල්ල හදාගත්ත global එක )

                print(colours['yellow'] + "Torrent Name              -> " + colours['green'] + names[select - 1])
                print(colours['yellow'] + "This is Your torrent link -> " + colours['green'] + iLink)
                time.sleep(2)
                print(colours['white'] + "[+] Browser opening ... Wait until page load ...")

                time.sleep(3)
                os.system(f"termux-open-url {iLink}")  # ඒ link එකෙන් browser එකේ run කරලා torrent file එක download කර ගන්නවා

                print(colours['cyan'] + "\n[+] This program will exit in 10 seconds\n[+] Thank for using")
                time.sleep(10)
                os.system('exit')

            elif select == 'next' or select == 'Next' or select == 'NEXT':
                next_page()
            elif select == '':
                os.system('exit')
            else:
                int(select)  # value error එකක් ගන්න ඕන නිසා

        def next_page():
            print("[+] Page - 2")
            find_film(2)

        if len(names) > 0:  # user දීපු නමින් එක film එකක් හරි තියේද බලනවා
            try:
                getting_film()

            except ValueError:
                print("----------------------------------------------------------")
                print(colours['red'] + "[!] Please enter torrent number")
                getting_film()

            except IndexError:  # පෙන්නන ගාන නැතුව වැඩි ගානක් දුන්නොත්
                print(colours['red'] + f'[!] Not more {catergory}s')
                nxt = input('if you want to search next page type \'next\' : ')
                if nxt == 'next' or nxt == 'Next' or nxt == 'NEXT':
                    next_page()
                else:
                    print(colours['red'] + "[!] OK .. exiting in 5 seconds")
                    time.sleep(5)
                    os.system('exit')


        else:  # names list එකේ එක element එකක් වත් නැත්තම් film එක නැහැනේ
            print(colours['red'] + "[!] Can't find your film")


try:
    find_film()

except ModuleNotFoundError:
    print(colours['red'] + "[!] Required Modules not found !!")

except Exception as e:
    print(colours['red'] + "\n[!] Please connect to internet")
    input()
