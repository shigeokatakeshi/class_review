# 下記のコードが期待通り動作するようなCustomerクラスを実装してください
# C-1. フルネームを取得できる
# ken = Customer(first_name="Ken", family_name="Tanaka")
# ken.full_name()  # "Ken Tanaka" という値を返す

# tom = Customer(first_name="Tom", family_name="Ford")
# tom.full_name()  # "Tom Ford" という値を返す


class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
    
    def full_name(self):
        return self.first_name + " " + self.family_name

ken = Customer(first_name="Ken", family_name="Tanaka")
tom = Customer(first_name="Tom", family_name="Ford")
print(tom.full_name())
print(ken.full_name())