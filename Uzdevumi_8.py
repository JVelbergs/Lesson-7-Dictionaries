# Dictionaries - Darbs Klasē
# 1. Simbolu biežums

# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1} # vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut
# 1b. Uzrakstīt funkciju: get_digit_dict(num), kas saņem veselu skaitli kā parametru(var būt ļoti liels
# funkcija  izvada ciparu izmantojumu skaitlī vārdnīcas formā
# Ievada 599637003 -> {'0':2, '1':0,....'7'':1,'8':0,'9':2} # rādam visiem cipariem izmantojamību
# Ieverojam ka cipariskās atslēgas ir stringi
# PS 1a un 1b var atrisināt ar vienu un to pašu funkciju 1b vajadzībām nedaudz pielāgojot 1a kodu.
#  Var būt arī risinājums ar Counter but tas galīgi nav obligāti, lai gan ir ļoti eleganti :)

# 2. Vārdnīcu labotājs
# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
# clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.


# 3. Vārdnīcu tīrītājs
# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.

# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!
# Divi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu.

# ---------------------------------------------------------------------------------------------------------------------------------

# # 1a. Uzdevums:


# def get_char_count(text):
#     count = {}
#     for c in set(text):
#         count[c] = text.count(c)
#     return count


# print(get_char_count("hubba bubba"))

# # ----------------------------------------------------------------------------------------------------------------------------------

# # 1b. Uzdevums:


# def get_digit_dict(num):
#     num = str(num)
#     count = {}
#     for c in set(num):
#         count[c] = num.count(c)
#     # return count
#     sorted_dict = dict(sorted(count.items()))
#     return sorted_dict

# print(get_digit_dict(599637003))

# ------------------------------------------------


def get_digit_dict(num):
    # empty_dic = {}
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for n in num_list:
    # print(n)
    zero_dic = {c: 0 for c in num_list}
    print(zero_dic)
    num = str(num)
    count = {}
    for c in set(num):
        count[c] = num.count(c)
    # return count
    sorted_dict = dict(sorted(count.items()))
    # return sorted_dict
    val_sorted_list = list(sorted_dict.values())
    # new_d = dict(zip(num_list, val_sorted_list))

    # for x in zero_dic:

    #     # checking if key present in other dictionary
    #     if x in sorted_dict:
    #         zero_dic[x] = sorted_dict[x]
    #         print(zero_dic[x])

    # res = {key: sorted_dict.get(key, zero_dic[key]) for key in zero_dic}
    res = sorted_dict.update(zero_dic)

    new_d = {c: v for c, v in zip(zero_dic, val_sorted_list)}
    # return new_d
    return res


print(get_digit_dict(599637003))

# https://www.geeksforgeeks.org/python-replace-dictionary-value-from-other-dictionary/

# https://www.google.com/search?q=python+update+dictionary+with+another+dictionary&rlz=1C1GCEA_enLV814LV814&sxsrf=AOaemvIvVaJ0wP91Ej_2i3Esswu3IxL47A%3A1631107982867&ei=jrs4YfOhNNuHwPAP-KGP2AY&oq=python+update+dictionary+with+another+dictionary&gs_lcp=Cgdnd3Mtd2l6EAwyBQgAEMsBOgcIIxCwAxAnOgcIABBHELADOgYIABAHEB46CAgAEAgQBxAeOggIABAIEA0QHjoICAAQBxAeEBM6CggAEAgQBxAeEBNKBAhBGABQjkRYzU9g5mJoAXACeACAAXCIAdQFkgEDNy4xmAEAoAEByAEJwAEB&sclient=gws-wiz&ved=0ahUKEwjzoKLfvu_yAhXbAxAIHfjQA2sQ4dUDCA8


# ------------------------------------------------------------------------------------------------------------------------------------

# 2. Uzdevums:


# def replace_dict_value(d, bad_val, good_val):
#     d = {"a": 5, "b": 6, "c": 5}
#     key_list = list(d.keys())
#     val_list = list(d.values())
#     new_val_list = [good_val if x == bad_val else x for x in val_list]
#     new_d = dict(zip(key_list, new_val_list))
#     return new_d


# print(replace_dict_value({"a": 5, "b": 6, "c": 5}, 5, 10))


# ------------------------------------------------------------------------------------------------------------

# 3.a Uzdevums

# 3. Vārdnīcu tīrītājs
# 3.a  Uzrakstīt clean_dict_value(d, bad_val), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtība  bad_val no kuras jāatbrīvojas kopā ar ar tās atslēgu.
# clean_dict_value({'a':5,'b':6,'c':5}, 5) -> {'b':6} , jo 5 bija vērtība gan a gan c atslēgām no kurām jāatbrīvojas.
# 3.b Uzrakstīt clean_dict_values(d, v_list), kas atgriež attīrītu vārdnīcu
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtību saraksts v_list no kurām jāatbrīvojas.
# clean_dict_values({'a':5,'b':6,'c':5}, [3,4,5]) -> {'b':6} , jo 5 bija vieno no vērtībām no kurām jāatbrīvojas.
# PS. Tīram mēs are del d['a'] protams tikai tad ja atslēga 'a' eksistē.

# !! Mainot vārdnīcas izmēru mēs nedrīkstam vienlaicīgi pa šo vārdnīcu staigāt(iterate)!
# Divi varianti: vai nu staigājam pa kopiju my_dict.copy.items(), vai arī būvējam jaunu vārdnīcu.


# def clean_dict_value(d, bad_val):
#     new_dic = {k: v for k, v in d.items() if v != bad_val}
#     if new_dic != d:
#         d = new_dic
#     return d


# print(clean_dict_value({"a": 5, "b": 6, "c": 5}, 5))

# 3.b Uzdevums:


# -----------------------------------------PIEZĪMES-----------------------------------------------------------

# text = "hubba bubba"
# abc = "abcdefghij"
# abc_dict = {v: i for i, v in enumerate(text, start=1)}
# print(abc_dict)

# def replace_dict_value(d, bad_val, good_val):
#     for i in d:
#         print(i)
#     d.stdeafult("key", value)

# print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))

# d = {"a": 5, "b": 6, "c": 5}
# key_list = list(d.keys())
# val_list = list(d.values())
# new_val_list = [10 if x == 5 else x for x in val_list]
# print(new_val_list)
# new_d = dict(zip(key_list, new_val_list))
# print(new_d)


# if list(d.values() == 5:
# zero_dict = {c: 0 for c in d}
# print(zero_dict)

# key_list = list(d.keys())
# val_list = list(d.values())
# print(key_list)
# print(val_list)

# a= [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]
# for n, i in enumerate(a):
#     if i == 1:
#         a[n] = 10

# a = [1, 2, 3, 1, 3, 2, 1, 1]
# print([4 if x == 1 else x for x in a])

# d = {"a": 5, "b": 6, "c": 5}
# my_value = "b"
# if my_value in d:
#     print(d[my_value])
# else:
#     print("Couldn't find this value")

# dictionary = {"george": 16, "amber": 19}
# search_age = input("Provide age ")
# for (
#     name,
#     age,
# ) in dictionary.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
#     if age == search_age:
#         print(name)

# mydict = {"george": 16, "amber": 19}
# key_from_dict = list(mydict.keys())[list(mydict.values()).index(19)]
# print(key_from_dict)
# print(mydict.get(key_from_dict))


# def clean_dict_value(d, bad_val):
#     for key, value in d.items():
#         copy = d.copy()
#         if value == bad_val:
#             return key

#     del copy[key]
#     return copy


# print(clean_dict_value({"a": 5, "b": 6, "c": 5}, 5))


# copy = d.copy()
# del copy[delete]
# return copy
# if any([True for k, v in d.items() if v == bad_val]):
#     print(f"Yes, Value: '{bad_val}' exists in dictionary")
# else:
#     print(f"No, Value: '{bad_val}' does not exists in dictionary")
