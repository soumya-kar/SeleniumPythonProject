"""
Run these tests after completing the setup steps to verify that the framework works.
"""

def test_the_tests():
  assert True

def func2():
  list1= []
  list2=[56, 77, 90, 65]
  for l in list2:
    list1.append(l)
  return list1


print(func2())