meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşı cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek,Sinirlenmek",
            }
            
print("Anlamlarını öğrenebileceğiniz kelimeler:", *meme_dict.keys())

for i in range(5):
    x = input("Hangi kelimenin anlamını öğrenmek istersiniz?")
    x = x.upper()

if x in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(x, "kelimesinin anlamı: ", meme_dict[x])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Maalesef yazdığınız kelime sözlükte bulunmamaktadır!")
