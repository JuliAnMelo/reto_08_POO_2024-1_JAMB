class Payment:
  def __init__(self):
    pass

  def to_pay(self, amount):
    raise NotImplementedError("SubClass must implement to_pay()")

class Card(Payment):
  def __init__(self, number, amount_committed):
    super().__init__()
    self.number = number
    self.amount_committed = amount_committed

  def to_pay(self, amount):
    print(f"Paying ${amount} with card:   ****{self.number[-4:]}")
    if self.amount_committed >= amount:
      print(f"Payment made with Card. Change: ${self.amount_committed - amount}")
    else:
      print(f"Insufficient funds. Missing ${amount - self.amount_committed} to complete payment.")

class Cash(Payment):
  def __init__(self, amount_committed):
    super().__init__()
    self.amount_committed = amount_committed

  def to_pay(self, amount):
    if self.amount_committed >= amount:
      print(f"Payment made in cash. Change: ${self.amount_committed - amount}")
    else:
      print(f"Insufficient money. Missing ${amount - self.amount_committed} to complete payment.")