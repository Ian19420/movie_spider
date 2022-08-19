import requests, bs4, re, os

destDir = 'images'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)

url = "https://movies.yahoo.com.tw/movie_thisweek.html"
moviehtml = requests.get(url)
soup = bs4.BeautifulSoup(moviehtml.text, "lxml")

num = 0
list_ = soup.find("ul", class_ = "release_list")
items = list_.find_all("li")
for item in items:
    cname = item.find('div', class_ = 'release_movie_name').a.text.strip()
    ename = item.find('div', class_ = 'en').a.text.strip()
    r_time = item.find("div", class_ = "release_movie_time").text
    pattern = r"\d{4}-\d\d-\d\d"
    time = re.findall(pattern, r_time)
    level = item.find('div', 'leveltext').span.text.strip()
    txt = item.find('div', 'release_text').text.strip()

    img_tap = item.find("img", class_ = "lazy-load")
    photo_url = img_tap["data-src"]
    picture = requests.get(photo_url)
    with open(os.path.join(destDir, cname) + ".jpg", "wb") as f:
        for diskStorage in picture.iter_content(10240):
            f.write(diskStorage)

    num += 1
    print('新片編號 : ', num)
    print('中文片名 : ', cname)
    print('英文片名 : ', ename)
    print("圖片網址 ： ", photo_url)
    print('期待度 : ', level)
    print("內容摘要 ： ", txt)

    print("上映日期 ： ", time[0])
    print()




