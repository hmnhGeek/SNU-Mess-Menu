import bs4, requests
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')

def messMenu():

    url = "http://messmenu.snu.in/messMenu.php"
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text)

    print "DH-1"
    counter = 0
    curr_index = 0

    for td in soup.findAll('td'):

        p = td.findAll('p', attrs = {'style':'margin:0px 0px 2px;'})

        if p == [] and counter == 0:
            counter = 1
        elif p == [] and counter == 1:
            print "DH-2"

        for i in range(len(p)):
            print p[i].text
        print '--------------------------------'

messMenu()
