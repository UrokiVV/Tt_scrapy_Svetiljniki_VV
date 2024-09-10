import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    category_obj = "/category/krovati-i-matrasy"
    # category_obj = "/category/svet"


    site_name = "https://www.divan.ru"
    start_urls = [ site_name + category_obj]

    def parse(self, response):
        file_name = "Result_KrovatiMatrasy_sep13.csv"


        all_obj = response.css('div._Ud0k')
        data = []
        i_obj1 = 0
        for obj1 in all_obj:
            i_obj1 +=1
            name = obj1.css('div.lsooF  div.wYUX2  a.ui-GPFV8  span::text').get(),
            price = obj1.css('div.lsooF  div.wYUX2  div.q5Uds span.ui-LD-ZU::text').get(),
            url = obj1.css('div._Ud0k div.Gb9dg a.ui-GPFV8 div.Pk6w8 img').css('img').xpath('@src').extract()[0]

            name_data = ";" + str(name) + ";"
            name_data = name_data.replace(";('", "").replace("',);", "")
            price_data = ";" + str(price) + ";"
            price_data = price_data.replace(";('", "").replace("',);", "").replace(" ", "")

            line_obj1 = [name_data, price_data, url]
            data.append(line_obj1)
            if i_obj1 <= 3:
                print(f"\ni_svet={i_obj1}")
                print(line_obj1)
                print("\n")
            yield {
                 'name': name,
                 'price': price,
                 'url': url
            }
        print("Result:")
        print(data[0])
        print(data[1])
        print(data[2])

        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Наименование', 'Цена', 'ссылка на фотографию'])
            writer.writerows(data)
