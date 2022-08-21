import requests, bs4, re, os

destDir = 'images'
if os.path.exists(destDir) == False:
    os.mkdir(destDir)

url = "https://movies.yahoo.com.tw/movie_thisweek.html"
moviehtml = requests.get(url)
soup = bs4.BeautifulSoup(moviehtml.text, "lxml")

num = 0
items = soup.find_all('div', 'release_info')
for item in items:
    cname = item.find('div', class_ = 'release_movie_name').a.text.strip()
    ename = item.find('div', class_ = 'en').a.text.strip()

    r_time = item.find("div", class_ = "release_movie_time").text
    pattern = r"\d{4}-\d\d-\d\d"
    time = re.findall(pattern, r_time)

    level = item.find('div', 'leveltext').span.text.strip()
    txt = item.find('div', 'release_text').text.strip()

    photo_url = item.find_previous_sibling('div', class_ = 'release_foto').a.img["data-src"]
    photo = requests.get(photo_url)
    with open(os.path.join(destDir, cname) + ".jpg", "wb") as f:
        for diskStorage in photo.iter_content(10240):
            f.write(diskStorage)
    forecast = item.find("a", class_ = "btn_s_vedio gabtn")
    if forecast == None:
        forecast_url = "暫無"
    else:
        forecast_url = forecast["href"]


    num += 1
    print('新片編號 : ', num)
    print('中文片名 : ', cname)
    print('英文片名 : ', ename)
    print("上映日期 ： ", time[0])
    print("圖片網址 ： ", photo_url)
    print('期待度 : ', level)
    print("內容摘要 ： ", txt)
    print("預告片 : ", forecast_url)
    print()




