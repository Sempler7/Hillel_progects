import sys
sys.path.insert(0, r"C:\Users\sempl\Desktop\Курс AQA Hillel\Home work\17\randominfo\randominfo-master\randominfo")
import randominfo

print("Путь к модулю:", randominfo.__file__)
person = randominfo.Person()
print("Имя:", person.first_name)
