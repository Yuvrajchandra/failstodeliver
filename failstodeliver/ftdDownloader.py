from io import BytesIO
from zipfile import ZipFile
import urllib.request
from bs4 import BeautifulSoup
import requests
import re
import csv




def append_data(file_name, list_of_elem):

    with open(file_name, 'a+', newline='') as write_obj:
        writer = csv.writer(write_obj)
        writer.writerows(list_of_elem)




def download_csv():
        DOMAIN = "https://www.sec.gov"
        FAILS_TO_DELIVER_URL = "https://www.sec.gov/data/foiadocsfailsdatahtm"
        req = requests.get(FAILS_TO_DELIVER_URL)
        soup = BeautifulSoup(req.content, 'html.parser')
        a_list = soup.find_all('a', href=re.compile("^/files/data/"))
        a_list_2 = soup.find_all('a', href=re.compile("^/files/node/add/"))

        for a_item in a_list:

            a_link = a_item.get('href', None)
            file_url = DOMAIN + a_link
            url = urllib.request.urlopen(file_url)

            with ZipFile(BytesIO(url.read())) as my_zip_file:
                for contained_file in my_zip_file.namelist():
                    temp_file_name = contained_file.split('.')
                    file_name = temp_file_name[0] + ".csv"
                    print(file_name)
                    data = []

                    for line in my_zip_file.open(contained_file).readlines():
                        line=line.decode('ISO-8859-1')
                        row = line.split('|')
                        data.append(row)

                    del data[-1]
                    del data[-1]

                    append_data(file_name,data)

        for a_item in a_list_2:

            a_link = a_item.get('href', None)
            file_url = DOMAIN + a_link
            url = urllib.request.urlopen(file_url)

            with ZipFile(BytesIO(url.read())) as my_zip_file:
                for contained_file in my_zip_file.namelist():
                    temp_file_name = contained_file.split('.')
                    file_name = temp_file_name[0] + ".csv"
                    print(file_name)
                    data = []

                    for line in my_zip_file.open(contained_file).readlines():
                        line=line.decode('ISO-8859-1')
                        row = line.split('|')
                        data.append(row)

                    del data[-1]
                    del data[-1]

                    append_data(file_name,data)



if __name__ == '__main__':
    download_csv()
