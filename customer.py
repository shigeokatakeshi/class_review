# 下記のコードが期待通り動作するようなCustomerクラスを実装してください
# C-1. フルネームを取得できる
# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken.full_name()  # "Ken Tanaka" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford")
# tom.full_name()  # "Tom Ford" という値を返す

# C-2. 年齢という概念の追加
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.age  # 15 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom.age # 57 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.age # 73 という値を返す
# C-3. 年齢に応じた適切な入場料(entry_fee)を計算できる
# 料金の計算ルール
# こども料金(20歳未満): 1000円
# おとな料金(20歳以上65歳未満): 1500円
# シニア料金(65歳以上): 1200円
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.entry_fee()  # 1000 という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# tom.entry_fee() # 1500 という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.entry_fee() # 1200 という値を返す

# C-4. 単一の顧客情報をCSV形式で取得できる
# ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford", age= 57)
# ken.info_csv()  # "Tom Ford,57,1500" という値を返す

# ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


class Customer:
    def __init__(self, first_name, family_name, age=None):
        self.first_name = first_name
        self.family_name = family_name
        self._age = age

    def full_name(self):
        print(self.first_name, self.family_name)
    
    def age(self):
        print(self._age)

    def entry_fee(self):
        if 20 > self._age:
            print(1000)
        if 20 <= self._age < 65:
            print(1500)
        if 65 <= self._age:
            print(1200)

    def info_csv(self):
        self.full_name(), self.age(), self.entry_fee()


ken = Customer(first_name="Ken", family_name="Tanaka")
tom = Customer(first_name="Tom", family_name="Ford")

# tom.full_name()  # "Tom Ford" という値を返す
tom.full_name()
# ken.full_name()  # "Ken Tanaka" という値を返す
ken.full_name()

ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)

# ken.age  # 15 という値を返す
ken.age()
# tom.age # 57 という値を返す
tom.age()
# ieyasu.age # 73 という値を返す
ieyasu.age()

# ken.entry_fee()  # 1000 という値を返す
ken.entry_fee()
# tom.entry_fee() # 1500 という値を返す
tom.entry_fee()
# ieyasu.entry_fee() # 1200 という値を返す
ieyasu.entry_fee()

# ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
ken.info_csv()
# tom.info_csv()  # "Tom Ford,57,1500" という値を返す
tom.info_csv()
# ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
ieyasu.info_csv()