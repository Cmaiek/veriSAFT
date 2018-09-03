from tkinter.filedialog import askopenfilename
from tkinter import *
from lxml import objectify, etree
import os

#  parsuj plik JPK_VAT wskazany przez użytkownika
filename = askopenfilename()
parser = etree.XMLParser(remove_blank_text=True)
tree = etree.parse(filename, parser)
root = tree.getroot()

#  wyczyść przestrzenie nazw
for elem in root.getiterator():
    if not hasattr(elem.tag, 'find'): continue
    i = elem.tag.find('}')
    if i >= 0:
        elem.tag = elem.tag[i + 1:]
objectify.deannotate(root, cleanup_namespaces=True)

# znajdź zawartość wszystkich pól K_XX, dopisz do listy i podsumuj listę
K_10_v = []
for K_10 in root.iter('K_10'):
    K_10_v.append(float(K_10.text))
K_10_tot = round(sum(K_10_v))
print("K_10 = ", K_10_tot)

K_11_v = []
for K_11 in root.iter('K_11'):
    K_11_v.append(float(K_11.text))
K_11_tot = round(sum(K_11_v))
print("K_11 = ", K_11_tot)

K_12_v = []
for K_12 in root.iter('K_12'):
    K_12_v.append(float(K_12.text))
K_12_tot = round(sum(K_12_v))
print("K_12 = ", K_12_tot)

K_13_v = []
for K_13 in root.iter('K_13'):
    K_13_v.append(float(K_13.text))
K_13_tot = round(sum(K_13_v))
print("K_13 = ", K_13_tot)

K_14_v = []
for K_14 in root.iter('K_14'):
    K_14_v.append(float(K_14.text))
K_14_tot = round(sum(K_14_v))
print("K_14 = ", K_14_tot)

K_15_v = []
for K_15 in root.iter('K_15'):
    K_15_v.append(float(K_15.text))
K_15_tot = round(sum(K_15_v))
print("K_15 = ", K_15_tot)

K_16_v = []
for K_16 in root.iter('K_16'):
    K_16_v.append(float(K_16.text))
K_16_tot = round(sum(K_16_v))
print("K_16 = ", K_16_tot)

K_17_v = []
for K_17 in root.iter('K_17'):
    K_17_v.append(float(K_17.text))
K_17_tot = round(sum(K_17_v))
print("K_17 = ", K_17_tot)

K_18_v = []
for K_18 in root.iter('K_18'):
    K_18_v.append(float(K_18.text))
K_18_tot = round(sum(K_18_v))
print("K_18 = ", K_18_tot)

K_19_v = []
for K_19 in root.iter('K_19'):
    K_19_v.append(float(K_19.text))
K_19_tot = round(sum(K_19_v))
print("K_19 = ", K_19_tot)

K_20_v = []
for K_20 in root.iter('K_20'):
    K_20_v.append(float(K_20.text))
K_20_tot = round(sum(K_20_v))
print("K_20 = ", K_20_tot)

K_21_v = []
for K_21 in root.iter('K_21'):
    K_21_v.append(float(K_21.text))
K_21_tot = round(sum(K_21_v))
print("K_21 = ", K_21_tot)

K_22_v = []
for K_22 in root.iter('K_22'):
    K_22_v.append(float(K_22.text))
K_22_tot = round(sum(K_22_v))
print("K_22 = ", K_22_tot)

K_23_v = []
for K_23 in root.iter('K_23'):
    K_23_v.append(float(K_23.text))
K_23_tot = round(sum(K_23_v))
print("K_23 = ", K_23_tot)

K_24_v = []
for K_24 in root.iter('K_24'):
    K_24_v.append(float(K_24.text))
K_24_tot = round(sum(K_24_v))
print("K_24 = ", K_24_tot)

K_25_v = []
for K_25 in root.iter('K_25'):
    K_25_v.append(float(K_25.text))
K_25_tot = round(sum(K_25_v))
print("K_25 = ", K_25_tot)

K_26_v = []
for K_26 in root.iter('K_26'):
    K_26_v.append(float(K_26.text))
K_26_tot = round(sum(K_26_v))
print("K_26 = ", K_26_tot)

K_27_v = []
for K_27 in root.iter('K_27'):
    K_27_v.append(float(K_27.text))
K_27_tot = round(sum(K_27_v))
print("K_27 = ", K_27_tot)

K_28_v = []
for K_28 in root.iter('K_28'):
    K_28_v.append(float(K_28.text))
K_28_tot = round(sum(K_28_v))
print("K_28 = ", K_28_tot)

K_29_v = []
for K_29 in root.iter('K_29'):
    K_29_v.append(float(K_29.text))
K_29_tot = round(sum(K_29_v))
print("K_29 = ", K_29_tot)

K_30_v = []
for K_30 in root.iter('K_30'):
    K_30_v.append(float(K_30.text))
K_30_tot = round(sum(K_30_v))
print("K_30 = ", K_30_tot)

K_31_v = []
for K_31 in root.iter('K_31'):
    K_31_v.append(float(K_31.text))
K_31_tot = round(sum(K_31_v))
print("K_31 = ", K_31_tot)

K_32_v = []
for K_32 in root.iter('K_32'):
    K_32_v.append(float(K_32.text))
K_32_tot = round(sum(K_32_v))
print("K_32 = ", K_32_tot)

K_33_v = []
for K_33 in root.iter('K_33'):
    K_33_v.append(float(K_33.text))
K_33_tot = round(sum(K_33_v))
print("K_33 = ", K_33_tot)

K_34_v = []
for K_34 in root.iter('K_34'):
    K_34_v.append(float(K_34.text))
K_34_tot = round(sum(K_34_v))
print("K_34 = ", K_34_tot)

K_35_v = []
for K_35 in root.iter('K_35'):
    K_35_v.append(float(K_35.text))
K_35_tot = round(sum(K_35_v))
print("K_35 = ", K_35_tot)

K_36_v = []
for K_36 in root.iter('K_36'):
    K_36_v.append(float(K_36.text))
K_36_tot = round(sum(K_36_v))
print("K_36 = ", K_36_tot)

K_37_v = []
for K_37 in root.iter('K_37'):
    K_37_v.append(float(K_37.text))
K_37_tot = round(sum(K_37_v))
print("K_37 = ", K_37_tot)

K_38_v = []
for K_38 in root.iter('K_38'):
    K_38_v.append(float(K_38.text))
K_38_tot = round(sum(K_38_v))
print("K_38 = ", K_38_tot)

K_39_v = []
for K_39 in root.iter('K_39'):
    K_39_v.append(float(K_39.text))
K_39_tot = round(sum(K_39_v))
print("K_39 = ", K_39_tot)

# ZAKUPY

K_43_v = []
for K_43 in root.iter('K_43'):
    K_43_v.append(float(K_43.text))
K_43_tot = round(sum(K_43_v))
print("K_43 = ", K_43_tot)

K_44_v = []
for K_44 in root.iter('K_44'):
    K_44_v.append(float(K_44.text))
K_44_tot = round(sum(K_44_v))
print("K_44 = ", K_44_tot)

K_45_v = []
for K_45 in root.iter('K_45'):
    K_45_v.append(float(K_45.text))
K_45_tot = round(sum(K_45_v))
print("K_45 = ", K_45_tot)

K_46_v = []
for K_46 in root.iter('K_46'):
    K_46_v.append(float(K_46.text))
K_46_tot = round(sum(K_46_v))
print("K_46 = ", K_46_tot)

K_47_v = []
for K_47 in root.iter('K_47'):
    K_47_v.append(float(K_47.text))
K_47_tot = round(sum(K_47_v))
print("K_47 = ", K_47_tot)

K_48_v = []
for K_48 in root.iter('K_48'):
    K_48_v.append(float(K_48.text))
K_48_tot = round(sum(K_48_v))
print("K_48 = ", K_48_tot)

K_49_v = []
for K_49 in root.iter('K_49'):
    K_49_v.append(float(K_49.text))
K_49_tot = round(sum(K_49_v))
print("K_49 = ", K_49_tot)

K_50_v = []
for K_50 in root.iter('K_50'):
    K_50_v.append(float(K_50.text))
K_50_tot = round(sum(K_50_v))
print("K_50 = ", K_50_tot)
# wyświetl w układzie VAT-7

r = 0
# NALEŻNY
Label(text='').grid(row=r, column=0)
Label(text="Podstawa opodatkowania").grid(row=r, column=1)
Label(text="Podatek należny").grid(row=r, column=2)
r = r+1

Label(text='Dostawa towarów oraz świadczenie usług na terytorium kraju, zwolnione od podatku').grid(row=r, column=0)
Label(text=K_10_tot).grid(row=r, column=1)

r = r+1

Label(text='Dostawa towarów oraz świadczenie usług poza terytorium kraju').grid(row=r, column=0)
Label(text=K_11_tot).grid(row=r, column=1)

r = r+1

Label(text='...w tym świadczenie usług, o których mowa w art. 100 ust. 1 pkt 4 ustawy').grid(row=r, column=0)
Label(text=K_12_tot).grid(row=r, column=1)

r = r+1


Label(text='Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 0%').grid(row=r, column=0)
Label(text=K_13_tot).grid(row=r, column=1)

r = r+1

Label(text='...w tym dostawa towarów, o której mowa w art. 129 ustawy').grid(row=r, column=0)
Label(text=K_14_tot).grid(row=r, column=1)

r = r+1

Label(text='Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 5%').grid(row=r, column=0)
Label(text=K_15_tot).grid(row=r, column=1)
Label(text=K_16_tot).grid(row=r, column=2)
r = r+1

Label(text='Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 7% albo 8%').grid(row=r, column=0)
Label(text=K_17_tot).grid(row=r, column=1)
Label(text=K_18_tot).grid(row=r, column=2)
r = r+1

Label(text='Dostawa towarów oraz świadczenie usług na terytorium kraju, opodatkowane stawką 22% albo 23%').grid(row=r, column=0)
Label(text=K_19_tot).grid(row=r, column=1)
Label(text=K_20_tot).grid(row=r, column=2)
r = r+1

Label(text='Wewnątrzwspólnotowa dostawa towarów').grid(row=r, column=0)
Label(text=K_21_tot).grid(row=r, column=1)

r = r+1

Label(text='Eksport towarów').grid(row=r, column=0)
Label(text=K_22_tot).grid(row=r, column=1)

r = r+1

Label(text='Wewnątrzwspólnotowe nabycie towarów').grid(row=r, column=0)
Label(text=K_23_tot).grid(row=r, column=1)
Label(text=K_24_tot).grid(row=r, column=2)
r = r+1

Label(text='Import towarów podlegający rozliczeniu zgodnie z art. 33a ustawy').grid(row=r, column=0)
Label(text=K_25_tot).grid(row=r, column=1)
Label(text=K_26_tot).grid(row=r, column=2)
r = r+1

Label(text='Import usług z wyłączeniem usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28b ustawy').grid(row=r, column=0)
Label(text=K_27_tot).grid(row=r, column=1)
Label(text=K_28_tot).grid(row=r, column=2)
r = r+1

Label(text='Import usług nabywanych od podatników podatku od wartości dodanej, do których stosuje się art. 28b ustawy').grid(row=r, column=0)
Label(text=K_29_tot).grid(row=r, column=1)
Label(text=K_30_tot).grid(row=r, column=2)
r = r+1

Label(text='Dostawa towarów oraz świadczenie usług, dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wypełnia dostawca)').grid(row=r, column=0)
Label(text=K_31_tot).grid(row=r, column=1)

r = r+1

Label(text='Dostawa towarów oraz świadczenie usług, dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 5 ustawy (wypełnia nabywca)').grid(row=r, column=0)
Label(text=K_32_tot).grid(row=r, column=1)
Label(text=K_33_tot).grid(row=r, column=2)
r = r+1

Label(text='Dostawa towarów oraz świadczenie usług, dla których podatnikiem jest nabywca zgodnie z art. 17 ust. 1 pkt 7 lub 8 ustawy (wypełnia nabywca)').grid(row=r, column=0)
Label(text=K_34_tot).grid(row=r, column=1)
Label(text=K_35_tot).grid(row=r, column=2)
r = r+1

Label(text='Kwota podatku należnego od towarów i usług objętych spisem z natury, o którym mowa w art. 14 ust. 5 ustawy').grid(row=r, column=0)

Label(text=K_36_tot).grid(row=r, column=2)
r = r+1

Label(text='Zwrot odliczonej lub zwróconej kwoty wydatkowanej na zakup kas rejestrujących, o którym mowa w art. 111 ust. 6 ustawy').grid(row=r, column=0)

Label(text=K_37_tot).grid(row=r, column=2)
r = r+1

Label(text='Kwota podatku należnego od wewnątrzwspólnotowego nabycia środków transportu, wykazanego w poz. 24, podlegająca wpłacie w terminie, o którym mowa w art. 103 ust. 3, w związku z ust. 4 ustawy').grid(row=r, column=0)

Label(text=K_38_tot).grid(row=r, column=2)
r = r+1

Label(text='Kwota podatku od wewnątrzwspólnotowego nabycia paliw silnikowych, podlegająca wpłacie w terminach, o których mowa w art. 103 ust. 5a i 5b ustawy').grid(row=r, column=0)

Label(text=K_39_tot).grid(row=r, column=2)
r = r+1

# NALICZONY
Label(text='').grid(row=r, column=0)
Label(text="Wartość netto").grid(row=r, column=1)
Label(text="Podatek naliczony").grid(row=r, column=2)
r = r+1

Label(text='Nabycie towarów i usług zaliczanych u podatnika do środków trwałych').grid(row=r, column=0)
Label(text=K_43_tot).grid(row=r, column=1)
Label(text=K_44_tot).grid(row=r, column=2)
r = r+1

Label(text='Nabycie towarów i usług pozostałych').grid(row=r, column=0)
Label(text=K_45_tot).grid(row=r, column=1)
Label(text=K_46_tot).grid(row=r, column=2)

mainloop()