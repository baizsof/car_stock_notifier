import hasznaltauto_lib
import chache_lib
import smtplib

BASE_URL = "https://www.hasznaltauto.hu"
URL = BASE_URL + "/talalatilista/PDNH2VC3WLNDADG5RML5AIIJJ7Z5STTH7LBRMMXCIYCOGF3DHOMUWGHWL3MQTPIOUXGQ6QUSR6HI4ZADV4VH5554FA4ZGEFQWVHMAAL3WYTV7QMZD5IKHOSBC5WHELJZAM2U6PCMVE6QMVHANIWUYTC5ODDF4I7QDFORXTWKIX5FFQUKGPWFYPJ3PZ4BPCFHDO7C5NXFW5RLX67TVUTV4Z7QQMARL2QLHDOSK2GORL2EWFK3OBQD4BBI4HPSJFFRKNINNPEJCGGSGOSUM4GHMFS6HQKTSC6XCBE56Q2DDTMP5SAXWOEP2CMXAALZR6RCMVHNIEPF7ZVOZF36SMXRGIDXY3TA7I3YBZ62PAUP2UVSEOOJXB66L4O5XPJXRBSCDKOIIWRU3FSHNZFVBUVJLXCTLYINPTS7KC6UYED3NIOME45WZM4MCYXRK52JZ33UR2MEVUMLGADSHJKPWRGCCSE5OU5PGRQUIHZMKDIZPF3LJBLAN3ILEPPQCW7YWUPAGQQ4UHHNOW2MXUK6IW5SFG4AROKLJHH6SRWP6SG4IAU3RWXQH7CDEQ5MT2EGIL47QBRSLQRLNAIGONBNXLHE2KQRJKK7RP6ET2BYZQWRLJMFTU7GNGEDZSUMY4ZOGMOVED5J2QUP3GEZZ6PKD5NGYMXG3OGPSLVBSK5DI3UFPKYDEISSSV55VBDY4U2QJSEXTWJK354DUTVSA477TIZ6D3KJPTHG4BTZKGQQZTTK5NVTQKUYDWFDKVCHBNXEJ3VG5MTJLUEQ37A3RGFIV6I47LCCXK3OQ6RRJBVW47I6EPI5CX27ZD35NWFTOW3J3IOQGIIANGQ37L5GIXILJLHRQ3OGC6GN5DZP55RRYIF5HE76YR5H2GCDRVOHN74JFGO6"


def get_new_cars(current_cars, cached_cars):
    new_cars = []
    counter = 0
    for current_car in current_cars:
        if current_car not in cached_cars:
            new_cars.append(current_car)
        else:
            counter += 1
    print(counter)

    return new_cars


def make_new_cars_links(new_cars_ids):
    links = []
    for new_car_id in new_cars_ids:
        new_url = '{}/{}'.format(BASE_URL, new_car_id)
        links.append(new_url)

    return links


def send_new_cars_links(links):
    try:
        print('logging in')
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.debuglevel(2)
        server.starttls()
        print('sending')
        server.ehlo()
        server.login("makospite12@gmail.com","00112200")
        server.sendmail("makospite12@gmail.com", "izsofcsaba@gmail.com", links)
        print('sent')
        server.close()
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")


def main():
    current_cars = hasznaltauto_lib.parse_cars(URL)
    cached_cars = chache_lib.load_cars()
    new_cars = get_new_cars(current_cars, cached_cars)

    if new_cars.__len__() != 0:
        new_cars_links = make_new_cars_links(new_cars)
        try:
            send_new_cars_links(new_cars_links)
        except:
            print("error found during mail transfer")
            exit(1)
        chache_lib.write_cars(current_cars)



if __name__ == '__main__':
    main()
