from api.controllers import Tax
from django_mock_queries.query import MockSet, MockModel

def test_SimpleTax():
  #Arrange
  subtotal = 15
  deliveryFee = 4.0
  #Act
  tax = Tax.calculate(subtotal, deliveryFee)
  #Assert
  assert tax == 1.57
