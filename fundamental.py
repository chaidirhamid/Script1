# print('Halo');

# -------------------------------------------------------------#
# nama = 'Andi';
# print(nama);

# -------------------------------------------------------------#
# usia = 22;
# usia = 32;
# print(usia);

# jomblo = True;
# print(jomblo);

# -------------------------------------------------------------#
# nama = input("what is your name? :");
# print(nama);

# -------------------------------------------------------------#
# nama = input("Nama kamu? ")
# umur = input("Umur kamu? ")
# kelamin = input("Jenis kelamin kamu? ")
# pekerjaan = input("Pekerjaan kamu? ")

# print("nama : " + nama);
# print("umur : " + umur);
# print("kelamin : " + kelamin);
# print("pekerjaan : " + pekerjaan);

# -------------------------------------------------------------#
# usiaAndi = 20;
# usiaBudi = 40;

# print(usiaAndi * usiaBudi);
# print(usiaAndi / usiaBudi);
# print(usiaAndi + usiaBudi);
# print(usiaAndi - usiaBudi);
# print(usiaAndi % usiaBudi);
# print(usiaBudi **2);

# -------------------------------------------------------------#
# import math

# print(math.pi);
# print(math.fabs(-4.7));
# print(math.pow(8,2));
# print(math.sqrt(64));

# -------------------------------------------------------------#
# import math

# print(round(4.7));
# print(round(4.4));
# print(math.floor(4.7));
# print(math.ceil(4.4));

# -------------------------------------------------------------#
# x = 'Halo Dunia';

# print(len(x));
# print(x.index('Dunia'));
# print(x.split(' '));
# print(x.lower());
# print(x.upper());
# print(x.capitalize());

# -------------------------------------------------------------#
# singleQuotes = 'single quotes';
# doubleQuotes = "double quotes";
# combineQuotes = "wrap lot's of other quotes";

# print(singleQuotes);
# print(doubleQuotes);
# print(combineQuotes);

# -------------------------------------------------------------#
# word =  "I'm Baron, nice to meet you"

# print(word[1]);
# print(word[2:]);
# print(word[:4]);
# print(word[2:5]);
# print(word[:]);
# print(word[-8:]);

# -------------------------------------------------------------#
# angka1 = input("Masukkan Angka 1: ");
# angka2 = input("Masukkan Angka 2: ");

# print(angka1 + angka2);
# print(int(angka1) + int(angka2));

# angka1 = float(angka1);
# angka2 = float(angka2);

# print(angka1 + angka2);

# -------------------------------------------------------------#
# usia = 22;
# nama = 'Andi';

# print(usia + usia);
# print(nama + ' ' + nama);
# print(nama + ' ' + str(usia));

# -------------------------------------------------------------#
# MODUL 1
# Problem #1
# import math

# x = 4;
# y = 3;
# z = 2;

# w = (x+y*z)/(x*y);
# print(math.pow(w,z));

# -------------------------------------------------------------#
# Problem #2
# x = input('Silahkan masukkan angka berapapun: ');
# y = (int(x))**2;
# print("Kuadrat dari " + x + ' = ' + str(y));

# -------------------------------------------------------------#
# Problem #3
# import math

# jumlah_hari = 485;
# sisa_hari = jumlah_hari;
# tahun = math.floor(sisa_hari/360);
# sisa_hari -= tahun*360;
# bulan = math.floor(sisa_hari/30);
# sisa_hari -= bulan*30;
# minggu = math.floor(sisa_hari/7);
# sisa_hari -= minggu*7;
# hari = sisa_hari;
# print(str(tahun) + " tahun " + str(bulan) + " bulan " + str(minggu) + " minggu " + str(hari) + " hari ");

# -------------------------------------------------------------#
# # Problem #4
# jumlah_usia = input('Jumlah usia Andi dan Budi: ');
# ratio_usia = input('Ratio usia Andi dan Budi: ');

# usiaAndi = int(jumlah_usia) / (1 + float(ratio_usia));
# usiaBudi = int(jumlah_usia) - usiaAndi;
# print('Usia Andi dan Budi 2 tahun lagi masing-masing adalah ' + str(int(usiaAndi + 2)) + ' dan ' + str(int(usiaBudi + 2)));

# -------------------------------------------------------------#
# Problem #5

# x = input('Masukkan kata atau kalimat: ');
# y = input('Masukkan karakter yang ingin dicari: ')

# z = len(x.split(y)) - 1;

# # bisa juga z = x.count(y)

# print('Jumlah karakter ' + y + ' adalah sebanyak ' + str(z));

# -------------------------------------------------------------#
# Problem #6

# import math

# s = int(input('Masukkan jarak mobil A dan B (km): '));
# va = int(input('Kecepatan mobil A (km/jam): '));
# vb = int(input('Kecepatan mobil B (km/jam): '));
# t_start = int(input('Waktu A dan B mulai berjalan: '));

# t = s / (va + vb) * 60;
# sisa_menit = t;
# jam = math.floor(sisa_menit/60);
# sisa_menit -= jam*60;

# print('Mobil A dan B akan bertabrakan pukul ' + str(t_start + jam) + ' lewat ' + str(int(sisa_menit)) + ' menit');

# -------------------------------------------------------------#
# usiaAndi = 40;

# usiaAndi *= 2;
# print(usiaAndi);
# usiaAndi /= 2;
# print(usiaAndi);
# usiaAndi += 2;
# print(usiaAndi);
# usiaAndi -= 2;
# print(usiaAndi);
# usiaAndi %= 2;
# print(usiaAndi);

# -------------------------------------------------------------#
# x = 5;
# y = '5';

# print(x == y);
# print(x > int(y));
# print(x >= int(y));
# print(x < int(y));
# print(x <= int(y));

# -------------------------------------------------------------#
# x = 5;
# y = '5';
# z = 6;

# print(x == int(y) and int(y) < z);
# print(x == int(y) or int(y) < z);
# print(not(x == int(y)) or int(y) < z);

# -------------------------------------------------------------#
# nilai = 40;

# if (nilai > 80): 
#     print('Excellent!');
# elif (nilai >=60 and nilai <= 80): 
#     print('Good Job!');
# else: 
#     print("Don't give up!");

# -------------------------------------------------------------#
# jomblo = True;

# if (jomblo): 
#     print('masih jomblo');
# else:
#     print('udah taken!');


# -------------------------------------------------------------#
# MODUL 2
# Problem #1
# x = int(input('Masukkan angka: '));
# y = x % 2;

# if (y == 0):
#     print('Angka ' + str(x) + ' tergolong bilangan GENAP');
# else:
#     print('Angka ' + str(x) + ' tergolong bilangan GANJIL');


# -------------------------------------------------------------#
# Problem #2
# massa = input('Masukkan berat badan (kg): ');
# tinggi = input('Masukkan tinggi badan (cm): ');

# imt = int(massa) / ((int(tinggi)/100) ** 2);

# print('Massa ' + massa + ' kg' + ' & ' + 'tinggi ' + str(int(tinggi)/100) + ' m');
# print('IMT ' + str(imt))

# if (imt < 18.5):
#     print('Berat badan kurang');
# elif (imt < 24.9):
#     print('Berat badan ideal');
# elif(imt < 29.9):
#     print('Berat badan berlebih');
# elif(imt < 39.9):
#     print('Berat badan sangat berlebih');
# else:
#     print('Obesitas');


# -------------------------------------------------------------#
# angka = 1;
# while (angka <= 10):
#     print(angka);
#     angka += 1;


# -------------------------------------------------------------#
# listItem = list(range(1,11,2));
# print(listItem);

# for item in range(1,11,2):
#     print(item);


# -------------------------------------------------------------#
# y = 'Nomor urut';

# for item in range(0,21,2):
#     print(y + str(item));


# -------------------------------------------------------------#
# z = '';
# for item in range(0,5):
#     z += '*'

# print(z);


# -------------------------------------------------------------#
# z = '';
# for item in range(0,5):
#     z += '* \n'

# print(z);


# -------------------------------------------------------------#
# z = '';
# for item in range(0,5):
#     for item1 in range(0,5):
#         z += '*';
#     z += '\n';

# print(z);


# -------------------------------------------------------------#
# z = '';
# for item in range(0,5):
#     for item1 in range(0,item+1):
#         z += '*';
#     z += '\n';

# print(z);


# -------------------------------------------------------------#
# MODUL 3
# Problem #1
# z = '';
# for item in range(0,5):
#     for item1 in range(0,5-item):
#         z += ' * ';
#     z += '\n';

# print(z);

# -------------------------------------------------------------#
# Problem #2
# z = '';
# for item in range(0,9):
#     if item <= 4:
#         for item1 in range(0,5-item):
#             z += ' * ';
#         z += '\n';
#     else:
#         for item1 in range(0,item-3):
#             z += ' * ';
#         z += '\n';

# print(z);

# -------------------------------------------------------------#
# Problem #3
# z = '';
# for item in range(1,11):
#     for item1 in range(0,10-item):
#         z += '   ';
#     z += '  *' * (2*item - 1);
#     z += '\n';

# print(z);

# -------------------------------------------------------------#
# Problem #4
# z = '';
# for item in range(1,12):
#     for item1 in range(0,20-(2*item-1)):
#         z += '  *';
#     z += '\n';
#     z += '   ' *item; 
   
# print(z);

# -------------------------------------------------------------#
# Problem #5
# z = '';
# for item in range(1,6):
#     for item1 in range(0,5-item):
#         z += '   ';
#     z += '  *' * (2*item - 1);
#     z += '\n';
    
# for item in range(1,6):
#     for item1 in range(0,10-(2*item-1)):
#         z += '  *';
#     z += '\n';
#     z += '   ' *item;     
# print(z);

# -------------------------------------------------------------#
# def contoh():
#     print('Halo Dunia!');

# contoh();

# -------------------------------------------------------------#
# def contoh():
#     print(x + y);

# x = 10;
# y = 50;

# contoh();

# -------------------------------------------------------------#
# def namaku(nama):
#     print(nama + ' Susilo');

# namaku('Adi');
# namaku('Budi');
# namaku('Caca');
# namaku('Dedi');

# -------------------------------------------------------------#
# def data(x,y):
#     print(x + ' lahir tahun ' + y);

# data('Adi','1990');
# data('Budi','1991');

# -------------------------------------------------------------#
# def total(x,y):
#     z = x + y;
#     return z;

# print(total(4,5));
## print(z); local variable dalam function total

# -------------------------------------------------------------#
# def kali(x):
#     if (x < 2):
#         return 1;
#     else:
#         return (x * tiga());

# def tiga():
#     return 3;

# print(kali(5));

# -------------------------------------------------------------#
# def kali(angka1 = 5, angka2 = 2):
#     return angka1 * angka2;

# print(kali(angka2 = 4));

# -------------------------------------------------------------#
# def kali(angka1 = 5, angka2 = 2):
#     return angka1 * angka2;

# -------------------------------------------------------------#
# mobil = ['Alya','Xenia','Avanza'];

# print(mobil);
# print(mobil[0]);
# print(mobil[2]);

# -------------------------------------------------------------#
# buah = ['Jeruk','Nanas','Apel'];

# for item in buah:
#     print(item);

# -------------------------------------------------------------#
# buah = ['Jeruk','Nanas','Apel','Mangga'];

# print(buah[1:]);
# print(buah[:3]);
# print(buah[2:4]);
# print(buah[:]);

# -------------------------------------------------------------#
# buah = ['Jeruk','Nanas','Apel','Mangga'];

# buah[1] = 'Kelapa';
# print(buah);

# -------------------------------------------------------------#
# buah = ['Jeruk','Nanas','Apel','Mangga'];

# buah.append('Kelapa');
# print(buah);
# buah.pop();
# buah.pop();
# print(buah);


# -------------------------------------------------------------#
# MODUL 4
# Problem #1

# def sort(x):
#     for i in range(0,6):
#         for j in range(0,6):
#             if x[i] < x[j]:
#                 z = x[i];
#                 x[i] = x[j];
#                 x[j] = z;

# x1 = input('Masukkan angka ke-1: ');
# x2 = input('Masukkan angka ke-2: ');
# x3 = input('Masukkan angka ke-3: ');
# x4 = input('Masukkan angka ke-4: ');
# x5 = input('Masukkan angka ke-5: ');
# x6 = input('Masukkan angka ke-6: ');

# x = [int(x1), int(x2), int(x3), int(x4), int(x5), int(x6)];

# print('Array sebelum diurutkan: ');
# print(x);

# sort(x);
        
# print('Array setelah diurutkan: ');
# print(x);


# -------------------------------------------------------------#
# Problem #2

# def sort(x):
#     for i in range(0,6):
#         for j in range(0,6):
#             if x[i] < x[j]:
#                 z = x[i]
#                 x[i] = x[j]
#                 x[j] = z;

# x1 = input('Masukkan angka ke-1: ');
# x2 = input('Masukkan angka ke-2: ');
# x3 = input('Masukkan angka ke-3: ');
# x4 = input('Masukkan angka ke-4: ');
# x5 = input('Masukkan angka ke-5: ');
# x6 = input('Masukkan angka ke-6: ');

# x = [int(x1), int(x2), int(x3), int(x4), int(x5), int(x6)];

# sort(x);
        
# print('Nilai minimum adalah: ');
# print(x[0]);
# print('Nilai maksimum adalah: ');
# print(x[5]);

# -------------------------------------------------------------#
# d = {"key1" : "item1", "key2" : "item2", "kucing" : [3, "jerapah"]};
# print(d["key1"]);
# print(d["key2"]);
# print(d["kucing"]);
# print(d["kucing"][1]);

# -------------------------------------------------------------#
# d = {"key1" : {"key2" : "item2"}, "kucing" : [3, "jerapah"]};
# print(d["key1"]);
# print(d["key1"]["key2"]);
# print(d["kucing"]);
# print(d["kucing"][1]);

# -------------------------------------------------------------#
# t = (1, [0, "test"], {"a1" : True});
# print(t[2]["a1"]);
# print(t[1][1]);
# t[1][1] = "akan";
# print(t[1][1]);
# t[1] = "mark";
# print(t[1]);

# -------------------------------------------------------------#
# t = (1, [0, "test"], {"a1" : True}, (0,{"test" : 5}, 2));

# print(t[3][1]["test"]);

# -------------------------------------------------------------#
# s = {1, 3, 1, 2, 2, 3};

# print(s);
# print(list(s)[2]);

# -------------------------------------------------------------#
# x = ['Merdeka', 'Hello', 'Hellos', 'Sohib', 'Kari ayam'];

# uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
# lowercase = 'abcdefghijklmnopqrstuvwxyz';

# word = 'Merdeka';
# new_word = '';
# for i in word:
#     char = i;
#     if i in uppercase:
#         idx = uppercase.index(i);
#         char = lowercase[idx];
#     new_word += char;
# print(new_word);

# -------------------------------------------------------------#
# def word_changer(word):
#     uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
#     lowercase = 'abcdefghijklmnopqrstuvwxyz';

#     new_word = '';
#     for i in word:
#         char = i;
#         if i in uppercase:
#             idx = uppercase.index(i);
#             char = lowercase[idx];
            
#         new_word += char;
    
#     return new_word;

# words = ['Merdeka','Hello','Hellos','Sohib','Kari ayam'];
# hasil = [word_changer(word) for word in words];
# search = input('Search: ');
# search = word_changer(search);

# result = list(filter(lambda num: search in num, hasil)); 

# idx = [hasil.index(i) for i in result];
# final = [words[i] for i in idx];
# print(final);


# -------------------------------------------------------------#
# def FizzBuzz(num):
#     for i in range(1,num+1):
#         if (i % 15 == 0):
#             print('FizzBuzz');
#         elif (i % 3 == 0):
#             print('Fizz');
#         elif (i % 5 == 0):
#             print('Buzz');
#         else:
#             print(i);

# FizzBuzz(20);

# -------------------------------------------------------------#

# def fibo(urut):
#     listData = [1,1];
#     for i in range(2,urut):
#         listData.append(listData[i-2]+listData[i-1]);
#     return listData[urut-1];

# print(fibo(8));


# -------------------------------------------------------------#

# def fibo(urut):
#     listData = [1,1,1];
#     for i in range(2,urut):
#         listData.append(listData[i-2]+listData[i]);
#     return listData;

# print(fibo(15));

# -------------------------------------------------------------#

# import math

# def reverseList(theList):
#     for i in range(0,math.floor(len(theList)/2)):
#         tempList = theList[i];
#         theList[i] = theList[len(theList) - 1 - i];
#         theList[len(theList) - 1 - i] = tempList;
    
#     return theList;

# print(reverseList([1,2,3,4,5,6,7,8]));


# -------------------------------------------------------------#
# import math

# def reverseList(theList):
#     if (len(theList) % 2 == 0):
#         for i in range(0,int(len(theList)/2)):
#             tempList = theList[i];
#             theList[i] = theList[int(len(theList) / 2) + i];
#             theList[int(len(theList) / 2) + i] = tempList;
#     else:
#         for i in range(0,math.floor(len(theList)/2)):
#             tempList = theList[i];
#             theList[i] = theList[math.floor(len(theList) / 2) + i + 1];
#             theList[math.floor(len(theList) / 2) + i + 1] = tempList;
    
#     return theList;

# print(reverseList([1,2,3,4,5,6,7,8,9]));


# -------------------------------------------------------------#
# from bubble_Sort import bubbleSort; 
# x = [6000, 34, 203, 3, 746, 200, 984, 198, 764, 9, 1];

# print(bubbleSort(x));


# -------------------------------------------------------------#
# from bubble_Sort import bubbleSort; 
# import math;
# x = [1,2,3,2,5,2,7,2,3];

# def getMedian(list):
#     bubbleSort(x);
#     median = 0;
#     if (len(list) % 2 != 0):
#         median = list[math.floor(len(list) / 2)];
#     else:
#         mid1 = list[(int(len(list) / 2)) - 1];
#         mid2 = list[int(len(list) / 2)];
#         median = (mid1 + mid2) / 2;
#     return median;

# print(getMedian(x));
# print(x);


# -------------------------------------------------------------#
# from bubble_Sort import bubbleSort; 
# import math;
# x = [1,2,3,2,5,2,7,2];

# def getMean(list):
#     sum = 0;
#     for item in list:
#         sum += item;
#     mean = sum / len(list);
#     return mean;

# avg = getMean(x);
# # error_abs_list = list(map(lambda num : abs(num - avg),x));
# # [abs(item - avg) for item in x];
# squared_error = [(item - avg) ** 2 for item in x];
# sum_se = sum(squared_error);
# variance = sum_se / len(x);
# std_dev = math.sqrt(variance);
# print(avg)
# print(std_dev);

# -------------------------------------------------------------#
x = [1,2,3,2,5,2,7,2];

uniq = list(set(x));
count_num = [x.count(i) for i in uniq]
print(max(count_num));



